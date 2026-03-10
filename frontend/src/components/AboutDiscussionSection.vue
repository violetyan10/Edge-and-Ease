<template>
  <section class="about-section">
    <div class="section-wrapper">

      <!-- Top quote band -->
      <div ref="quoteRef" class="reveal about-section__quote-band">
        <blockquote class="about-section__quote">
          "Stress is not the enemy. Disconnection from yourself is."
        </blockquote>
      </div>

      <!-- Two-column content block -->
      <div ref="contentRef" class="reveal about-section__grid">

        <!-- About -->
        <div class="about-section__col">
          <span class="section-label">About Edge & Ease</span>
          <h2 class="about-section__title">Built for the quietly overwhelmed</h2>
          <div class="divider" />
          <p>
            Edge &amp; Ease was born from a simple observation: most of us know we need to
            slow down, but the tools available feel either too clinical or too vague.
            We wanted something in between — practical, warm, and genuinely useful
            in the middle of a hard day.
          </p>
          <p>
            Our coaches combine evidence-based techniques from cognitive behavioural
            therapy, somatic practices, and mindfulness research, distilled into tips
            you can actually use in two minutes or less.
          </p>
          <p>
            This is a living project. More coaches, a richer kit, and community
            features are on the way. We'd love to hear what you need most.
          </p>
        </div>

        <!-- Discussion / CTA column -->
        <div class="about-section__col">
          <span class="section-label">Join the conversation</span>
          <h2 class="about-section__title">You're not alone in this</h2>
          <div class="divider" />
          <p>
            Stress and overwhelm thrive in silence. Talking about it — even briefly —
            with people who understand can shift something.
          </p>

          <!-- Discussion placeholder cards -->
          <ul class="about-section__threads" role="list">
            <li v-for="thread in threads" :key="thread.id" class="thread-card">
              <span class="thread-card__dot" aria-hidden="true" />
              <div>
                <p class="thread-card__topic">{{ thread.topic }}</p>
                <p class="thread-card__meta">{{ thread.replies }} replies · {{ thread.time }}</p>
              </div>
            </li>
          </ul>

          <button class="btn btn-ghost about-section__cta" disabled>
            Community coming soon
          </button>
        </div>

      </div>

      <!-- Footer strip -->
      <div ref="footerRef" class="reveal about-section__footer">
        <p class="about-section__footer-copy">
          &copy; {{ year }} Edge &amp; Ease — Made with intention.
        </p>
        <nav class="about-section__footer-links" aria-label="Footer navigation">
          <a href="#" class="about-section__footer-link">Privacy</a>
          <a href="#" class="about-section__footer-link">Terms</a>
          <a href="#" class="about-section__footer-link">Contact</a>
        </nav>
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useScrollReveal } from '../composables/useScrollReveal'

const quoteRef   = ref(null)
const contentRef = ref(null)
const footerRef  = ref(null)
const { observe } = useScrollReveal()
onMounted(() => observe(quoteRef.value, contentRef.value, footerRef.value))

const year = computed(() => new Date().getFullYear())

// Placeholder discussion threads — replace with real data from the backend later
const threads = [
  { id: 1, topic: "What's your go-to reset when nothing else works?", replies: 24, time: '2 h ago' },
  { id: 2, topic: "Does the 4-7-8 breath actually help anyone else?", replies: 17, time: '5 h ago' },
  { id: 3, topic: 'Tips for managing stress during big life transitions', replies: 41, time: '1 d ago' },
]
</script>

<style scoped>
/* ---- Section ---- */
.about-section {
  padding: var(--space-xl) 0 0;
  background-color: var(--color-surface-alt);
  border-top: 1px solid var(--color-border);
}

/* ---- Quote band ---- */
.about-section__quote-band {
  text-align: center;
  padding: var(--space-lg) 0;
}

.about-section__quote {
  font-family: var(--font-display);
  font-size: clamp(1.3rem, 3vw, 1.9rem);
  font-style: italic;
  color: var(--color-text-muted);
  max-width: 680px;
  margin: 0 auto;
  line-height: 1.5;
}

/* ---- Two-column grid ---- */
.about-section__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-lg);
  padding: var(--space-lg) 0;
}

.about-section__col {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.about-section__title {
  font-size: clamp(1.5rem, 3vw, 2rem);
}

.about-section__col p {
  font-size: 0.97rem;
  color: var(--color-text-muted);
  line-height: 1.75;
}

/* ---- Thread placeholder cards ---- */
.about-section__threads {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.thread-card {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.85rem 1rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  transition: box-shadow var(--transition);
}

.thread-card:hover {
  box-shadow: var(--shadow-sm);
}

.thread-card__dot {
  flex-shrink: 0;
  width: 8px;
  height: 8px;
  background-color: var(--color-accent);
  border-radius: 50%;
  margin-top: 6px;
}

.thread-card__topic {
  font-size: 0.9rem;
  color: var(--color-text);
  font-weight: 500;
  line-height: 1.4;
}

.thread-card__meta {
  font-size: 0.78rem;
  color: var(--color-text-light);
  margin-top: 2px;
}

.about-section__cta {
  align-self: flex-start;
  margin-top: 0.5rem;
  cursor: not-allowed;
  opacity: 0.7;
}

/* ---- Footer strip ---- */
.about-section__footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: var(--space-sm);
  padding: var(--space-md) 0;
  border-top: 1px solid var(--color-border);
  margin-top: var(--space-md);
}

.about-section__footer-copy {
  font-size: 0.82rem;
  color: var(--color-text-light);
}

.about-section__footer-links {
  display: flex;
  gap: 1.5rem;
}

.about-section__footer-link {
  font-size: 0.82rem;
  color: var(--color-text-muted);
  text-decoration: none;
  transition: color var(--transition);
}

.about-section__footer-link:hover {
  color: var(--color-accent-dark);
}

/* ---- Responsive ---- */
@media (max-width: 720px) {
  .about-section__grid {
    grid-template-columns: 1fr;
    gap: var(--space-md);
  }

  .about-section__footer {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
