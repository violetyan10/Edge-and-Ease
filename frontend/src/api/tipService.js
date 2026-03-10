/**
 * tipService.js — all backend API calls live here.
 *
 * The base URL is pulled from the Vite environment variable VITE_API_BASE_URL,
 * which you set in:
 *   - .env               (local dev)
 *   - Vercel dashboard   (production)
 *
 * To add real endpoints later, just add more exported async functions below.
 */

import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  headers: { 'Content-Type': 'application/json' },
  timeout: 15_000,
})

/**
 * Fetch a coach tip for the given user query.
 *
 * @param {string} query — user's free-text input
 * @returns {Promise<{ coach: string, suggestion: string }>}
 */
export async function fetchTip(query) {
  const { data } = await api.post('/api/tip', { query })
  return data
}

/**
 * Health check — useful for verifying the backend is reachable.
 * @returns {Promise<{ status: string }>}
 */
export async function checkHealth() {
  const { data } = await api.get('/health')
  return data
}

// ---------------------------------------------------------------------------
// Future endpoints (placeholders — wire up when backend is ready)
// ---------------------------------------------------------------------------

/**
 * Submit feedback for a tip result.
 * @param {object} payload — { tipId, vote: 'up' | 'down' }
 */
export async function submitFeedback(payload) {
  // TODO: implement when POST /api/feedback is added to the backend
  console.info('[tipService] submitFeedback (stub):', payload)
}
