"""
tip_service.py — Core tip retrieval logic.

Currently returns mock data. Replace `retrieve_tip` with real RAG logic later:
  1. Embed the user query with an embeddings model (e.g. OpenAI, Cohere, local)
  2. Query a vector store (e.g. Pinecone, Chroma, Weaviate) for relevant docs
  3. Pass retrieved docs + user query to an LLM for a contextual response
  4. Return the LLM response as the suggestion
"""

import random

# ---------------------------------------------------------------------------
# Mock coach personas — swap this list out or load from a DB later
# ---------------------------------------------------------------------------
COACHES = [
    {
        "name": "Coach Maya",
        "suggestions": [
            "Try a 2-minute breathing reset: inhale for 4 counts, hold for 4, exhale for 6. Repeat three times and step away from your screen.",
            "Place one hand on your heart and take three slow, intentional breaths. Remind yourself: this moment will pass.",
            "Write down the one thing that is weighing on you most right now. Seeing it on paper makes it smaller.",
        ],
    },
    {
        "name": "Coach Ren",
        "suggestions": [
            "Stand up, roll your shoulders back, and take a short 5-minute walk — even just around the room. Movement clears mental fog.",
            "Drink a full glass of water right now. Dehydration amplifies stress by more than most people realize.",
            "Close your eyes and name five things you can feel physically — the chair, the floor, your breath. Ground yourself in the present.",
        ],
    },
    {
        "name": "Coach Seren",
        "suggestions": [
            "Lower the brightness on your screen, put on soft ambient sound, and give yourself permission to work at 80% pace for the next 20 minutes.",
            "Send one short, kind message to someone you trust. Connection is one of the fastest antidotes to overwhelm.",
            "Block out a 15-minute buffer in your calendar today with no agenda. Protect that time fiercely.",
        ],
    },
]


def retrieve_tip(user_input: str) -> dict:
    """
    Return a coach tip relevant to the user's input.

    --- HOW TO PLUG IN RAG LATER ---
    Replace the body of this function with:

        embedding = embed(user_input)                     # step 1: embed query
        docs = vector_store.query(embedding, top_k=3)    # step 2: retrieve
        response = llm.generate(user_input, docs)        # step 3: generate
        return {"coach": response.coach, "suggestion": response.text}

    The function signature and return shape stay the same, so the API layer
    (`main.py`) never needs to change.
    """
    coach = random.choice(COACHES)
    suggestion = random.choice(coach["suggestions"])
    return {
        "coach": coach["name"],
        "suggestion": suggestion,
    }
