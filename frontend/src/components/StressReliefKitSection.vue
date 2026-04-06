<template>
  <section class="kit-section">
    <div class="section-wrapper">

      <!-- Header -->
      <div ref="headerRef" class="reveal kit-section__header">
        <span class="section-label">Your toolkit</span>
        <h2 class="kit-section__title">The Stress Relief Kit</h2>
        <div class="divider" />
        <p class="kit-section__lead">
          Designed to help skaters manage stress during high-pressure competitions. Every item is carefully chosen to provide stress relief while helping improve competition experiences. 
        </p>
        <br>
        <p class="kit-section__lead">
          Physical kit debuting at the 2026 Picken Dance Classic and U.S. Solo Dance International.
        </p>
      </div>

      <!-- Cards — staggered reveal -->
      <ul ref="cardsRef" class="kit-cards reveal-stagger" role="list">
        <li v-for="item in kitItems" :key="item.id" class="kit-card">
          <div class="kit-card__icon" aria-hidden="true">{{ item.icon }}</div>
          <h3 class="kit-card__title">{{ item.title }}</h3>
          <p class="kit-card__body">{{ item.body }}</p>
          <span class="kit-card__tag">{{ item.tag }}</span>
        </li>
      </ul>

    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useScrollReveal } from '../composables/useScrollReveal'

const headerRef = ref(null)
const cardsRef  = ref(null)
const { observe } = useScrollReveal()
onMounted(() => observe(headerRef.value, cardsRef.value))

// Placeholder kit items — swap content when real copy is ready
const kitItems = [
  {
    id: 1,
    icon: '◎',
    title: 'Stress ball',
    //tag: '2 minutes',
    body: 'Quick, tactile stress relief that’s convenient and safe for all ages.',
    },

  {id: 2,
    icon: '◈',
    title: 'Instruction card',
    //tag: '3 minutes',
    body: 'Includes a quick coach tip and breathing reset exercise. ',
  },

  {id: 3,
    icon: '❤︎⁠',
    title: 'Sensory sticker',
    //tag: '4 minutes',
    body: 'Offer a simple portable way to reset your focus.',
  },

]
</script>

<style scoped>
/* ---- Section ---- */
.kit-section {
  padding: var(--space-xl) 0;
  background-color: var(--color-bg);
}

.kit-section__header { max-width: 600px; }

.kit-section__title {
  font-size: clamp(1.8rem, 4vw, 2.8rem);
}

.kit-section__lead {
  color: var(--color-text-muted);
  font-size: 1.05rem;
  max-width: 540px;
}

/* ---- Cards grid ---- */
.kit-cards {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: var(--space-md);
  margin-top: var(--space-lg);
}

.kit-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2rem 1.75rem 1.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  box-shadow: var(--shadow-sm);
  transition: box-shadow var(--transition), transform var(--transition);
}

.kit-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-3px);
}

/* Number/icon badge */
.kit-card__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: var(--color-accent-light);
  color: var(--color-accent-dark);
  font-size: 1.1rem;
  font-weight: 600;
  flex-shrink: 0;
}

.kit-card__title {
  font-size: 1.15rem;
  font-family: var(--font-display);
  font-weight: 400;
  color: var(--color-text);
}

.kit-card__body {
  font-size: 0.95rem;
  color: var(--color-text-muted);
  line-height: 1.7;
  flex: 1;
}

.kit-card__tag {
  align-self: flex-start;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--color-accent-dark);
  background: var(--color-accent-light);
  padding: 0.2rem 0.7rem;
  border-radius: var(--radius-full);
}

@media (max-width: 600px) {
  .kit-cards { grid-template-columns: 1fr; }
}
</style>
