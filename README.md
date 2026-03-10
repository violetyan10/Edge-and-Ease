# Edge & Ease

A full-stack wellness web app with a Vue 3 + Vite frontend and a FastAPI backend.

---

## Project structure

```
edge_and_ease/
├── frontend/                  # Vue 3 + Vite SPA
│   ├── src/
│   │   ├── api/
│   │   │   └── tipService.js          # All API calls (axios)
│   │   ├── composables/
│   │   │   └── useScrollReveal.js     # IntersectionObserver scroll-reveal
│   │   ├── components/
│   │   │   ├── HeroSection.vue
│   │   │   ├── TipFinderSection.vue
│   │   │   ├── StressReliefKitSection.vue
│   │   │   └── AboutDiscussionSection.vue
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── style.css
│   ├── index.html
│   ├── .env                   # local dev env vars (not committed)
│   ├── .env.example
│   ├── vite.config.js
│   ├── vercel.json            # Vercel frontend deployment config
│   └── package.json
│
└── backend/                   # FastAPI app
    ├── api/
    │   └── index.py           # Vercel ASGI entry point
    ├── services/
    │   └── tip_service.py     # Tip retrieval logic (swap in RAG here)
    ├── main.py                # FastAPI app + routes
    ├── requirements.txt
    └── vercel.json            # Vercel backend deployment config
```

---

## Local development

### 1. Backend

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API is now running at `http://localhost:8000`.
Interactive docs: `http://localhost:8000/docs`

### 2. Frontend

```bash
cd frontend
npm install
cp .env.example .env   # already done — VITE_API_BASE_URL=http://localhost:8000
npm run dev
```

Site is now running at `http://localhost:5173`.

---

## Deploying to Vercel

The project is split into **two separate Vercel projects** — one for the frontend, one for the backend. This is the recommended approach because Vercel Python serverless functions and Vite SPA builds have different configurations.

### Step 1 — Deploy the backend

1. Push the repo to GitHub (or connect it directly in Vercel).
2. In the Vercel dashboard, click **Add New Project** and import the repo.
3. Set **Root Directory** to `backend`.
4. Vercel auto-detects the Python runtime via `api/index.py`.
5. No build command is needed.
6. Click **Deploy**.
7. Note the deployed URL, e.g. `https://edge-and-ease-api.vercel.app`.

**Environment variable to set in the Vercel backend project:**
| Key | Value |
|-----|-------|
| `ALLOWED_ORIGINS` | `https://your-frontend.vercel.app` |

### Step 2 — Deploy the frontend

1. In the Vercel dashboard, click **Add New Project** again and import the same repo.
2. Set **Root Directory** to `frontend`.
3. Vercel auto-detects the Vite / Vue framework.
4. Set the following environment variable before deploying:

| Key | Value |
|-----|-------|
| `VITE_API_BASE_URL` | `https://edge-and-ease-api.vercel.app` (your backend URL from Step 1) |

5. Click **Deploy**.

> **Important:** `VITE_API_BASE_URL` must be set *before* the build runs because Vite bakes environment variables into the static bundle at build time.

### CORS

The backend reads the `ALLOWED_ORIGINS` environment variable (comma-separated) and passes it to FastAPI's `CORSMiddleware`. Set it to the exact origin of your Vercel frontend — no trailing slash.

---

## API reference

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Liveness check |
| POST | `/api/tip` | Returns a coach tip |

### POST /api/tip

**Request body:**
```json
{ "query": "I feel anxious and can't focus" }
```

**Response:**
```json
{
  "coach": "Coach Maya",
  "suggestion": "Try a 2-minute breathing reset..."
}
```

---

## Adding real RAG later

All retrieval logic is isolated in `backend/services/tip_service.py`.
Replace the body of `retrieve_tip(user_input)` with your RAG pipeline:

```python
def retrieve_tip(user_input: str) -> dict:
    embedding = embed(user_input)                       # 1. embed query
    docs = vector_store.query(embedding, top_k=3)       # 2. retrieve context
    response = llm.generate(user_input, docs)           # 3. generate answer
    return {"coach": response.coach, "suggestion": response.text}
```

The function signature and return shape are unchanged, so `main.py` and the frontend need zero modifications.

---

## Tech stack

| Layer | Tech |
|-------|------|
| Frontend | Vue 3, Vite, Axios |
| Backend | FastAPI, Pydantic, Uvicorn |
| Deployment | Vercel (two projects) |
| Fonts | DM Serif Display + Inter (Google Fonts) |
