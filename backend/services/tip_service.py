"""
tip_service.py — RAG-based tip retrieval using TF-IDF cosine similarity.

Pipeline:
  1. Validate / clean the user's input.
  2. Embed the query with TF-IDF (pre-fitted on the reference questions).
  3. Find the best-matching question via cosine similarity.
  4. Randomly pick one coach answer from that question's answer pool.
  5. Return {coach, suggestion}.
"""

import json
import random
import re
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------------------------
# Load data once at module startup
# ---------------------------------------------------------------------------
_BASE = Path(__file__).parent.parent  # backend/

with open(_BASE / "qa_dataset.json", encoding="utf-8") as _f:
    # List of {id, Your Name, Title/Coaching Level, question, answer}
    _QA_DATA = json.load(_f)

with open(_BASE / "only_qa_dataset.json", encoding="utf-8") as _f:
    # List of {question, id} where id is pipe-separated e.g. "1|2|3|..."
    _ONLY_QA = json.load(_f)

_REF_QUESTIONS = [item["question"] for item in _ONLY_QA]
_REF_ID_LISTS = [
    [int(x) for x in item["id"].split("|")]
    for item in _ONLY_QA
]

# Pre-fit vectorizer on reference questions so transform() is fast per request
_VECTORIZER = TfidfVectorizer()
_REF_MATRIX = _VECTORIZER.fit_transform(_REF_QUESTIONS)

INPUT_MAX_LEN = 1000


# ---------------------------------------------------------------------------
# Input validation (ported from prepare_rag.ipynb)
# ---------------------------------------------------------------------------
def _validate_input(text: str) -> str:
    """
    Strip, collapse whitespace, and flag bad inputs.
    Returns the cleaned string, or raises ValueError with an issue code.
    """
    if not text or str(text).strip() == "":
        raise ValueError("empty_error")

    cleaned = re.sub(r"\s+", " ", str(text)).strip()
    
    if len(cleaned) > INPUT_MAX_LEN:
        raise ValueError("limit_exceeded_error")
    if re.fullmatch(r"\d+", cleaned):
        raise ValueError("digits_only_error")
    if re.fullmatch(r"[^\w\s]+", cleaned):
        raise ValueError("symbols_only_error")
    if re.search(r"[\x00-\x1F\x7F]", cleaned):
        raise ValueError("other_error")

    return cleaned


# ---------------------------------------------------------------------------
# Retrieval
# ---------------------------------------------------------------------------
def retrieve_tip(user_input: str) -> dict:
    """
    Return a coach tip relevant to the user's input.

    Steps:
      1. Validate & clean input.
      2. TF-IDF transform the query.
      3. Cosine-similarity against all reference questions.
      4. Pick a random answer from the best-matching question's pool.
      5. Return {"coach": <name>, "suggestion": <answer text>}.
    """
    print(f"[retrieve_tip] raw input: {repr(user_input)}")

    cleaned = _validate_input(user_input)
    print(f"[retrieve_tip] cleaned input: {repr(cleaned)}")

    query_vec = _VECTORIZER.transform([cleaned])
    scores = cosine_similarity(query_vec, _REF_MATRIX).flatten()
    print(f"[retrieve_tip] similarity scores: {dict(zip(_REF_QUESTIONS, scores.round(4)))}")

    best_idx = int(np.argmax(scores))
    best_score = float(scores[best_idx])
    matched_question = _REF_QUESTIONS[best_idx]
    print(f"[retrieve_tip] best match: '{matched_question}' (score={best_score:.4f})")

    possible_ids = _REF_ID_LISTS[best_idx]   # e.g. [1, 2, 3, ..., 10]
    selected_id = random.choice(possible_ids)  # 1-based
    print(f"[retrieve_tip] possible_ids={possible_ids}, selected_id={selected_id}")

    record = _QA_DATA[selected_id - 1]  # list is 0-indexed, id is 1-based
    print(f"[retrieve_tip] returning coach='{record['Your Name']}', answer preview='{record['answer'][:80]}...'")

    return {
        "coach": record["Your Name"],
        "suggestion": record["answer"],
    }
