<template>
  <section id="tip-finder" class="tip-section">
    <div class="section-wrapper">

      <!-- Section header — fades in on scroll -->
      <div ref="headerRef" class="reveal">
        <span class="section-label">Your personalized advice</span>
        <h2 class="tip-section__title">Find a tip that fits right now</h2>
        <div class="divider" />
        <p class="tip-section__lead">
          Tell us in a few words what's weighing on your mind at your competition 
          and get a coach tip tailored to your moment.
        </p>
      </div>

      <!-- Input area -->
      <div ref="inputRef" class="reveal tip-section__input-area">
        <textarea
          v-model="query"
          class="tip-input"
          placeholder="e.g. I feel overwhelmed/I tend to overthink"
          rows="3"
          :disabled="loading"
          @keydown.enter.prevent="handleFindTip"
          aria-label="Describe how you are feeling"
        />
        <button
          class="btn btn-accent tip-section__submit"
          :disabled="loading || !query.trim()"
          @click="handleFindTip"
        >
          <span v-if="!loading">Find a Tip</span>
          <span v-else class="tip-section__spinner" aria-label="Loading…" />
        </button>
      </div>

      <!-- Error state -->
      <Transition name="fade">
        <p v-if="error" class="tip-section__error" role="alert">
          {{ error }}
        </p>
      </Transition>

      <!-- Result card -->
      <Transition name="slide-up">
        <div v-if="result" ref="resultRef" class="tip-card">
          <div class="tip-card__coach-badge">
            <span class="tip-card__avatar" aria-hidden="true">✦</span>
            <span class="tip-card__coach-name">{{ result.coach }} suggests:</span>
          </div>

          <blockquote class="tip-card__suggestion">
            "{{ result.suggestion }}"
          </blockquote>

          <!-- Feedback buttons -->
          <div class="tip-card__feedback">
            <span class="tip-card__feedback-label">Was this helpful?</span>
            <button
              class="feedback-btn"
              :class="{ active: feedback === 'up' }"
              aria-label="Thumbs up"
              @click="submitFeedback('up')"
            >
              <!-- Thumbs up icon -->
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3H14z"/>
                <path d="M7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/>
              </svg>
              <span>Yes</span>
            </button>
            <button
              class="feedback-btn feedback-btn--down"
              :class="{ active: feedback === 'down' }"
              aria-label="Thumbs down"
              @click="submitFeedback('down')"
            >
              <!-- Thumbs down icon -->
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3H10z"/>
                <path d="M17 2h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"/>
              </svg>
              <span>Not quite</span>
            </button>
          </div>

          <!-- Feedback acknowledgement -->
          <Transition name="fade">
            <p v-if="feedback" class="tip-card__thanks">
              {{ feedback === 'up' ? 'Thank you — glad that helped.' : 'Thanks for letting us know. We\'ll keep improving.' }}
            </p>
          </Transition>
        </div>
      </Transition>

    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchTip, submitFeedback as submitFeedbackAPI } from '../api/tipService'
import { useScrollReveal } from '../composables/useScrollReveal'

// --- Scroll reveal ---
const headerRef = ref(null)
const inputRef  = ref(null)
const { observe } = useScrollReveal()
onMounted(() => observe(headerRef.value, inputRef.value))

// --- State ---
const query    = ref('')
const loading  = ref(false)
const error    = ref(null)
const result   = ref(null)
const feedback = ref(null) // 'up' | 'down' | null

// --- Handlers ---
async function handleFindTip() {
  if (!query.value.trim() || loading.value) return

  loading.value = true
  error.value   = null
  result.value  = null
  feedback.value = null

  try {
    result.value = await fetchTip(query.value.trim())
  } catch (err) {
    // Surface a friendly error message regardless of the underlying cause
    error.value =
      err?.response?.data?.detail ??
      'Something went wrong. Please check your connection and try again.'
  } finally {
    loading.value = false
  }
}

function submitFeedback(vote) {
  feedback.value = vote
  // Wire submitFeedbackAPI here when the backend endpoint is ready:
  // submitFeedbackAPI({ vote, query: query.value, suggestion: result.value?.suggestion })
}
</script>

<style scoped>
/* ---- Section shell ---- */
.tip-section {
  padding: var(--space-xl) 0;
  background-color: var(--color-surface-alt);
  border-top: 1px solid var(--color-border);
  border-bottom: 1px solid var(--color-border);
}

.tip-section__title {
  font-size: clamp(1.8rem, 4vw, 2.8rem);
  margin-bottom: 0;
}

.tip-section__lead {
  color: var(--color-text-muted);
  max-width: 560px;
  font-size: 1.05rem;
}

/* ---- Input area ---- */
.tip-section__input-area {
  margin-top: var(--space-lg);
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
  max-width: 620px;
}

.tip-input {
  width: 100%;
  padding: 1rem 1.25rem;
  font-family: var(--font-body);
  font-size: 1rem;
  color: var(--color-text);
  background: var(--color-surface);
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-md);
  resize: vertical;
  transition: border-color var(--transition), box-shadow var(--transition);
  line-height: 1.6;
}

.tip-input:focus {
  outline: none;
  border-color: var(--color-accent);
  box-shadow: 0 0 0 3px rgba(124,158,138,.2);
}

.tip-input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.tip-section__submit {
  align-self: flex-start;
  min-width: 140px;
  justify-content: center;
}

.tip-section__submit:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

/* ---- Spinner ---- */
.tip-section__spinner {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255,255,255,.35);
  border-top-color: #fff;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

/* ---- Error ---- */
.tip-section__error {
  margin-top: var(--space-sm);
  color: #b94a48;
  font-size: 0.9rem;
  background: #fdf2f2;
  border: 1px solid #f5c6c6;
  padding: 0.75rem 1rem;
  border-radius: var(--radius-sm);
  max-width: 620px;
}

/* ---- Result card ---- */
.tip-card {
  margin-top: var(--space-lg);
  max-width: 640px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2rem 2.25rem;
  box-shadow: var(--shadow-md);
}

.tip-card__coach-badge {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 1rem;
}

.tip-card__avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  background-color: var(--color-accent-light);
  color: var(--color-accent-dark);
  border-radius: 50%;
  font-size: 0.9rem;
}

.tip-card__coach-name {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--color-accent-dark);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.tip-card__suggestion {
  font-family: var(--font-display);
  font-size: 1.2rem;
  font-style: italic;
  line-height: 1.65;
  color: var(--color-text);
  border-left: 3px solid var(--color-accent);
  padding-left: 1.1rem;
  margin: 0 0 1.5rem;
}

/* ---- Feedback buttons ---- */
.tip-card__feedback {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.tip-card__feedback-label {
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.feedback-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 1rem;
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-full);
  background: transparent;
  font-family: var(--font-body);
  font-size: 0.85rem;
  color: var(--color-text-muted);
  cursor: pointer;
  transition: all var(--transition);
}

.feedback-btn:hover,
.feedback-btn.active {
  border-color: var(--color-accent);
  color: var(--color-accent-dark);
  background: var(--color-accent-light);
}

.feedback-btn--down:hover,
.feedback-btn--down.active {
  border-color: var(--color-clay);
  color: var(--color-clay-dark);
  background: #fce8de;
}

.tip-card__thanks {
  margin-top: 0.75rem;
  font-size: 0.85rem;
  color: var(--color-text-muted);
  font-style: italic;
}

/* ---- Vue transitions ---- */
.fade-enter-active, .fade-leave-active { transition: opacity 0.35s ease; }
.fade-enter-from, .fade-leave-to       { opacity: 0; }

.slide-up-enter-active { transition: opacity 0.5s ease, transform 0.5s ease; }
.slide-up-enter-from   { opacity: 0; transform: translateY(20px); }

/* ---- Responsive ---- */
@media (max-width: 600px) {
  .tip-card { padding: 1.5rem 1.25rem; }
  .tip-card__suggestion { font-size: 1.05rem; }
}
</style>
