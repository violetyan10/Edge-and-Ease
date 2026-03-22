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
    cleaned = _validate_input(user_input)

    query_vec = _VECTORIZER.transform([cleaned])
    scores = cosine_similarity(query_vec, _REF_MATRIX).flatten()

    best_idx = int(np.argmax(scores))
    possible_ids = _REF_ID_LISTS[best_idx]   # e.g. [1, 2, 3, ..., 10]
    selected_id = random.choice(possible_ids)  # 1-based

    record = _QA_DATA[selected_id - 1]  # list is 0-indexed, id is 1-based

    return {
        "coach": record["Your Name"],
        "suggestion": record["answer"],
    }
