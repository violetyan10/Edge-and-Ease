"""
tip_service.py — RAG-based tip retrieval using TF-IDF cosine similarity.

TWO IMPLEMENTATIONS AVAILABLE:
  [COMMENTED] scikit-learn version  — works locally, fast to develop with
  [ACTIVE]    Pure-Python version   — use for Vercel (no native compilation)

To switch: comment out the ACTIVE block and uncomment the COMMENTED block.
"""

import json
import random
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Load data once at module startup
# ---------------------------------------------------------------------------
_BASE = Path(__file__).parent.parent  # backend/

with open(_BASE / "qa_dataset.json", encoding="utf-8") as _f:
    _QA_DATA = json.load(_f)

with open(_BASE / "only_qa_dataset.json", encoding="utf-8") as _f:
    _ONLY_QA = json.load(_f)

_REF_QUESTIONS = [item["question"] for item in _ONLY_QA]
_REF_ID_LISTS = [
    [int(x) for x in item["id"].split("|")]
    for item in _ONLY_QA
]

INPUT_MAX_LEN = 1000


# ===========================================================================
# [COMMENTED] scikit-learn implementation — works locally
# ===========================================================================
# import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
#
# _VECTORIZER = TfidfVectorizer()
# _REF_MATRIX = _VECTORIZER.fit_transform(_REF_QUESTIONS)
#
# def _find_best_match(cleaned: str):
#     query_vec = _VECTORIZER.transform([cleaned])
#     scores = cosine_similarity(query_vec, _REF_MATRIX).flatten()
#     best_idx = int(np.argmax(scores))
#     return best_idx, float(scores[best_idx]), scores
# ===========================================================================


# ===========================================================================
# [ACTIVE] Pure-Python implementation — Vercel deployment
# (no scikit-learn / numpy → no native compilation → fast builds)
# ===========================================================================
import math
from collections import Counter

def _tokenize(text: str) -> list[str]:
    return re.findall(r"\b\w+\b", text.lower())

def _build_tfidf_model(corpus: list[str]):
    tokenized = [_tokenize(doc) for doc in corpus]
    n_docs = len(corpus)
    doc_freq: Counter = Counter()
    for tokens in tokenized:
        for word in set(tokens):
            doc_freq[word] += 1
    idf = {
        word: math.log((n_docs + 1) / (df + 1)) + 1
        for word, df in doc_freq.items()
    }
    ref_vectors = []
    for tokens in tokenized:
        if not tokens:
            ref_vectors.append({})
            continue
        counts = Counter(tokens)
        total = len(tokens)
        vec = {w: (cnt / total) * idf[w] for w, cnt in counts.items()}
        norm = math.sqrt(sum(v * v for v in vec.values()))
        if norm:
            vec = {w: v / norm for w, v in vec.items()}
        ref_vectors.append(vec)
    return idf, ref_vectors

def _transform_query(text: str, idf: dict) -> dict:
    tokens = _tokenize(text)
    if not tokens:
        return {}
    counts = Counter(tokens)
    total = len(tokens)
    vec = {w: (cnt / total) * idf[w] for w, cnt in counts.items() if w in idf}
    norm = math.sqrt(sum(v * v for v in vec.values()))
    if norm:
        vec = {w: v / norm for w, v in vec.items()}
    return vec

def _cosine(query_vec: dict, ref_vec: dict) -> float:
    return sum(query_vec.get(w, 0.0) * v for w, v in ref_vec.items())

_IDF, _REF_VECTORS = _build_tfidf_model(_REF_QUESTIONS)

def _find_best_match(cleaned: str):
    query_vec = _transform_query(cleaned, _IDF)
    scores = [_cosine(query_vec, rv) for rv in _REF_VECTORS]
    best_idx = max(range(len(scores)), key=lambda i: scores[i])
    return best_idx, scores[best_idx], scores
# ===========================================================================


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------
def _validate_input(text: str) -> str:
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
    print(f"[retrieve_tip] raw input: {repr(user_input)}")

    cleaned = _validate_input(user_input)
    print(f"[retrieve_tip] cleaned input: {repr(cleaned)}")

    best_idx, best_score, scores = _find_best_match(cleaned)
    matched_question = _REF_QUESTIONS[best_idx]
    print(f"[retrieve_tip] best match: '{matched_question}' (score={best_score:.4f})")

    possible_ids = _REF_ID_LISTS[best_idx]
    selected_id = random.choice(possible_ids)
    print(f"[retrieve_tip] possible_ids={possible_ids}, selected_id={selected_id}")

    record = _QA_DATA[selected_id - 1]
    print(f"[retrieve_tip] returning coach='{record['Your Name']}', answer preview='{record['answer'][:80]}...'")

    return {
        "coach": record["Your Name"],
        "suggestion": record["answer"],
    }
