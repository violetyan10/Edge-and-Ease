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
      <!-- <div ref="contentRef" class="reveal about-section__grid"> -->

        <!-- About -->
        <!-- <div class="about-section__col"> -->
          <!-- <span class="section-label">About Edge & Ease</span>
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
        </div> -->

        <!-- Discussion / CTA column -->
        <!-- <div class="about-section__col">
          <span class="section-label">Join the conversation</span>
          <h2 class="about-section__title">You're not alone in this</h2>
          <div class="divider" />
          <p>
            Stress and overwhelm thrive in silence. Talking about it — even briefly —
            with people who understand can shift something.
          </p> -->

          <!-- Discussion placeholder cards -->
          <!-- <ul class="about-section__threads" role="list">
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

      </div> -->



      <!-- People showcase -->
      <div ref="showcaseRef" class="reveal people-showcase">

        <div class="people-showcase__header">
          <span class="section-label">Our People</span>
          <h2 class="people-showcase__title">The faces behind Edge &amp; Ease</h2>
          <div class="divider" />
          <p class="people-showcase__subtitle">
            Our coaches bring together diverse expertise in mindfulness, somatic therapy,
            and cognitive practices — united by the belief that sustainable calm is possible for everyone.
          </p>
        </div>

        <div class="people-showcase__carousel">

          <button
            class="carousel-btn carousel-btn--prev"
            :class="{ 'carousel-btn--disabled': !canGoPrev }"
            :disabled="!canGoPrev"
            aria-label="Previous group"
            @click="prev"
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <polyline points="15 18 9 12 15 6" />
            </svg>
          </button>

          <div class="people-showcase__cards">
            <div
              v-for="person in visiblePeople"
              :key="person.id"
              class="profile-card"
              :class="{
                'is-flipped':    flippedCardId  === person.id,
                'is-closing':    closingCardId  === person.id,
                'no-transition': snapCardId     === person.id,
              }"
              role="button"
              tabindex="0"
              :aria-label="`${person.name} — click to learn more`"
              @click="toggleFlip(person.id)"
              @keydown.enter.prevent="toggleFlip(person.id)"
              @keydown.space.prevent="toggleFlip(person.id)"
            >
              <div class="profile-card__inner">

                <!-- Front -->
                <div class="profile-card__front">
                  <div class="profile-card__image-wrap">
                    <img
                      :src="person.image"
                      :alt="person.name"
                      class="profile-card__image"
                      loading="lazy"
                    />
                  </div>
                  <div class="profile-card__info">
                    <p class="profile-card__name">{{ person.name }}</p>
                    <p class="profile-card__role">{{ person.role }}</p>
                    <span class="profile-card__hint" aria-hidden="true">click to learn more</span>
                  </div>
                </div>

                <!-- Back -->
                <div class="profile-card__back" aria-hidden="true">
                  <div class="profile-card__back-content">
                    <p class="profile-card__name profile-card__name--back">{{ person.name }}</p>
                    <p class="profile-card__role profile-card__role--back">{{ person.role }}</p>
                    <p class="profile-card__bio">{{ person.bio }}</p>
                  </div>
                </div>

              </div>
            </div>
          </div>

          <button
            class="carousel-btn carousel-btn--next"
            :class="{ 'carousel-btn--disabled': !canGoNext }"
            :disabled="!canGoNext"
            aria-label="Next group"
            @click="next"
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <polyline points="9 18 15 12 9 6" />
            </svg>
          </button>

        </div>

        <!-- Dot indicators -->
        <div v-if="groupStarts.length > 1" class="people-showcase__dots" role="tablist" aria-label="Profile groups">
          <button
            v-for="(start, i) in groupStarts"
            :key="i"
            class="showcase-dot"
            :class="{ 'showcase-dot--active': currentIndex === start }"
            role="tab"
            :aria-selected="currentIndex === start"
            :aria-label="`Group ${i + 1}`"
            @click="goToGroup(start)"
          />
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
const showcaseRef = ref(null)
const footerRef  = ref(null)
const { observe } = useScrollReveal()
onMounted(() => observe(quoteRef.value, contentRef.value, showcaseRef.value, footerRef.value))

const year = computed(() => new Date().getFullYear())

// Placeholder discussion threads — replace with real data from the backend later
const threads = [
  { id: 1, topic: "What's your go-to reset when nothing else works?", replies: 24, time: '2 h ago' },
  { id: 2, topic: "Does the 4-7-8 breath actually help anyone else?", replies: 17, time: '5 h ago' },
  { id: 3, topic: 'Tips for managing stress during big life transitions', replies: 41, time: '1 d ago' },
]

// ---- People showcase ----

// Placeholder people — replace with real data from the backend later
// Avatars: DiceBear "adventurer" style (clipart illustrated faces, consistent style family)
// Gender distribution: 7 female, 3 male, in a naturally mixed order
const people = [
  {
    id: 1,
    name: 'Priya Nair',
    role: 'CBT Specialist',
    image: 'https://api.dicebear.com/7.x/adventurer/svg?seed=PriyaNair',
    bio: 'Priya draws on cognitive behavioural therapy and acceptance-based techniques to help clients untangle unhelpful thought patterns. She has a particular interest in workplace stress and burnout recovery.',
  },
  {
    id: 2,
    name: 'Marcus Webb',
    role: 'Mindfulness Educator',
    image: 'https://api.dicebear.com/7.x/adventurer/svg?seed=MarcusWebb',
    bio: 'Marcus spent years teaching mindfulness in schools and corporate settings before joining Edge & Ease. He has a rare gift for making contemplative practice feel immediately accessible and genuinely useful.',
  },
  {
    id: 3,
    name: 'Jordan Lee',
    role: 'Somatic Therapist',
    image: 'https://api.dicebear.com/7.x/adventurer/svg?seed=JordanLee',
    bio: 'Jordan integrates body-based practices with cognitive techniques, helping clients reconnect with their natural sense of ease and resilience. She believes the body holds the answers our minds often overlook.',
  },
  {
    id: 4,
    name: 'Leila Osei',
    role: 'Group Facilitator',
    image: 'https://api.dicebear.com/7.x/adventurer/svg?seed=LeilaOsei',
    bio: 'Leila creates the kind of group spaces where people feel genuinely heard. She specialises in facilitating community sessions that turn shared vulnerability into lasting connection and calm.',
  },
  {
    id: 5,
    name: 'Sam Rivera',
    role: 'Breathwork Facilitator',
    image: 'https://api.dicebear.com/7.x/adventurer/svg?seed=SamRivera',
    bio: 'Sam has guided thousands of people through breath-based practices rooted in both ancient traditions and modern neuroscience. His sessions are calm, structured, and quietly transformative.',
  },
  {
    id: 6,
    name: 'Cleo Adeyemi',
    role: 'Wellness Researcher',
    image: 'https://api.dicebear.com/7.x/adventurer/svg?seed=CleoAdeyemi',
    bio: 'Cleo bridges academic research and everyday practice, curating the evidence base that informs everything at Edge & Ease. She is passionate about making science legible without losing its nuance.',
  },
  {
    id: 7,
    name: 'Alex Morgan',
    role: 'Lead Coach',
    image: 'https://api.dicebear.com/7.x/adventurer/svg?seed=AlexMorgan',
    bio: 'Alex brings over a decade of mindfulness coaching experience, specialising in helping professionals navigate high-pressure environments with clarity and calm. Her approach is direct, practical, and grounded in compassion.',
  },
  {
    id: 8,
    name: 'Finn Halvorsen',
    role: 'Movement & Recovery',
    image: 'https://api.dicebear.com/7.x/adventurer/svg?seed=FinnHalvorsen',
    bio: "Finn's work centres on the relationship between physical movement and emotional regulation. He brings a warm, no-pressure energy to sessions that helps people feel safe enough to slow down.",
  },
  {
    id: 9,
    name: 'Yuki Tanaka',
    role: 'Sleep & Rhythm Coach',
    image: 'https://api.dicebear.com/7.x/adventurer/svg?seed=YukiTanaka',
    bio: 'Yuki specialises in sleep health and circadian rhythm, working with clients who find that exhaustion sits at the root of their stress. Her guidance is gentle, evidence-informed, and quietly effective.',
  },
  {
    id: 10,
    name: 'Nora Fenn',
    role: 'Community Lead',
    image: 'https://api.dicebear.com/7.x/adventurer/svg?seed=NoraFenn',
    bio: 'Nora shapes the community layer of Edge & Ease — the conversations, connections, and quiet support structures that make sustainable wellbeing possible beyond the one-on-one session.',
  },
]

const PAGE_SIZE = 3

const currentIndex = ref(0)
const flippedCardId  = ref(null) // card currently showing its back
const closingCardId  = ref(null) // card mid-clockwise-close animation
const snapCardId     = ref(null) // card that needs a silent transition:none reset
let   closeTimer     = null      // plain JS timer — no need for reactivity

// After the clockwise-close animation ends, silently snap the card
// from rotateY(-360deg) back to rotateY(0deg) with no visible motion.
function scheduleSnap(id) {
  snapCardId.value  = id   // disables transition on this card
  closingCardId.value = null
  // Two rAF passes: first lets Vue commit the transition:none style,
  // second lets the browser paint it before we remove the class.
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      if (snapCardId.value === id) snapCardId.value = null
    })
  })
}

function resetFlipState() {
  clearTimeout(closeTimer)
  flippedCardId.value = null
  closingCardId.value = null
  snapCardId.value    = null
}

// Compute all valid group start indices
const groupStarts = computed(() => {
  const total = people.length
  if (total <= PAGE_SIZE) return [0]
  const starts = []
  let i = 0
  while (i < total) {
    if (i + PAGE_SIZE >= total) {
      starts.push(total - PAGE_SIZE)
      break
    }
    starts.push(i)
    i += PAGE_SIZE
  }
  return starts
})

const visiblePeople = computed(() =>
  people.slice(currentIndex.value, currentIndex.value + PAGE_SIZE)
)

const canGoPrev = computed(() => currentIndex.value > 0)
const canGoNext = computed(() => currentIndex.value < people.length - PAGE_SIZE)

function next() {
  if (!canGoNext.value) return
  currentIndex.value = Math.min(currentIndex.value + PAGE_SIZE, people.length - PAGE_SIZE)
  resetFlipState()
}

function prev() {
  if (!canGoPrev.value) return
  currentIndex.value = Math.max(0, currentIndex.value - PAGE_SIZE)
  resetFlipState()
}

function goToGroup(start) {
  currentIndex.value = start
  resetFlipState()
}

function toggleFlip(clickedId) {
  const prevId = flippedCardId.value
  clearTimeout(closeTimer)

  if (prevId === clickedId) {
    // Same card clicked again — close it clockwise (–180° → –360°)
    closingCardId.value = clickedId
    flippedCardId.value = null
    closeTimer = setTimeout(() => scheduleSnap(clickedId), 760)
  } else {
    if (prevId !== null) {
      // Different card clicked — close the old one clockwise simultaneously
      closingCardId.value = prevId
      closeTimer = setTimeout(() => scheduleSnap(prevId), 760)
    }
    // Open the new card clockwise (0° → –180°) at the same instant
    flippedCardId.value = clickedId
  }
}
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

/* ================================================================
   People showcase
   ================================================================ */

.people-showcase {
  padding: var(--space-xl) 0 var(--space-lg);
  border-top: 1px solid var(--color-border);
}

/* ---- Section header ---- */
.people-showcase__header {
  text-align: center;
  max-width: 620px;
  margin: 0 auto var(--space-lg);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
}

.people-showcase__title {
  font-size: clamp(1.5rem, 3vw, 2rem);
  color: var(--color-text);
  margin: 0;
}

.people-showcase__subtitle {
  font-size: 0.97rem;
  color: var(--color-text-muted);
  line-height: 1.75;
  margin: 0;
}

/* ---- Carousel row ---- */
.people-showcase__carousel {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

/* ---- Cards grid ---- */
.people-showcase__cards {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  min-height: 400px;
  /* Shared perspective so all cards flip toward the same vanishing point */
  perspective: 1200px;
  perspective-origin: 50% 40%;
}

/* ---- Navigation buttons ---- */
.carousel-btn {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 1px solid var(--color-border);
  background: var(--color-surface);
  color: var(--color-text-muted);
  cursor: pointer;
  transition:
    background var(--transition),
    color var(--transition),
    border-color var(--transition),
    box-shadow var(--transition),
    opacity var(--transition);
}

.carousel-btn svg {
  width: 18px;
  height: 18px;
}

.carousel-btn:hover:not(:disabled) {
  background: var(--color-surface);
  border-color: var(--color-accent);
  color: var(--color-accent);
  box-shadow: var(--shadow-sm);
}

.carousel-btn--disabled,
.carousel-btn:disabled {
  opacity: 0.28;
  cursor: default;
  pointer-events: none;
}

/* ---- Dot indicators ---- */
.people-showcase__dots {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-top: var(--space-md);
}

.showcase-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  border: none;
  background: var(--color-border);
  cursor: pointer;
  padding: 0;
  transition:
    background var(--transition),
    transform var(--transition);
}

.showcase-dot--active {
  background: var(--color-accent);
  transform: scale(1.3);
}

/* ================================================================
   Profile card — flip effect
   ================================================================ */

.profile-card {
  /* No individual perspective — shared perspective set on parent */
  transform-style: preserve-3d;
  cursor: pointer;
  min-height: 400px;
  outline: none;
}

.profile-card__inner {
  position: relative;
  width: 100%;
  height: 100%;
  min-height: 400px;
  transform-style: preserve-3d;
  /* Smoother, more natural easing — gentle ease-out on both halves of the flip */
  transition: transform 0.75s cubic-bezier(0.35, 0.0, 0.25, 1.0);
  will-change: transform;
  border-radius: var(--radius-md, 12px);
}

/* Clockwise open: right edge comes toward viewer */
.profile-card.is-flipped .profile-card__inner {
  transform: rotateY(-180deg);
}

/* Clockwise close: continue rotating past back-face to full 360 */
.profile-card.is-closing .profile-card__inner {
  transform: rotateY(-360deg);
}

/* Silent snap — disables transition so the card can reset from
   –360deg back to 0deg without any visible motion */
.profile-card.no-transition .profile-card__inner {
  transition: none !important;
}

/* ---- Shared face styles ---- */
.profile-card__front,
.profile-card__back {
  position: absolute;
  inset: 0;
  border-radius: var(--radius-md, 12px);
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}

/* ---- Front face ---- */
.profile-card__front {
  display: flex;
  flex-direction: column;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
  transition: box-shadow var(--transition);
}

.profile-card:hover .profile-card__front {
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.1);
}

.profile-card__image-wrap {
  /* Square avatar area — width is set by the card column; height matches it */
  width: 100%;
  aspect-ratio: 1 / 1;
  flex-shrink: 0;
  overflow: hidden;
  background: var(--color-surface-alt);
  display: flex;
  align-items: center;
  justify-content: center;
}

.profile-card__image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  padding: 0.75rem;
}

.profile-card__info {
  padding: 1.1rem 1rem 0.9rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.2rem;
  background: var(--color-surface);
}

.profile-card__name {
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-text);
  margin: 0;
  line-height: 1.3;
}

.profile-card__role {
  font-size: 0.8rem;
  color: var(--color-text-muted);
  margin: 0;
  letter-spacing: 0.02em;
}

.profile-card__hint {
  font-size: 0.72rem;
  color: var(--color-text-light);
  margin-top: 0.35rem;
  opacity: 0.7;
  letter-spacing: 0.03em;
  transition: opacity 0.15s ease;
}

.profile-card.is-flipped .profile-card__hint,
.profile-card.is-closing .profile-card__hint {
  opacity: 0;
}

/* ---- Back face ---- */
.profile-card__back {
  transform: rotateY(180deg);
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(145deg, var(--color-accent, #6c8ebf) 0%, var(--color-accent-dark, #4a6fa5) 100%);
  padding: 2rem 1.5rem;
}

.profile-card__back-content {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  text-align: center;
}

.profile-card__name--back {
  color: #fff;
  font-size: 1.05rem;
}

.profile-card__role--back {
  color: rgba(255, 255, 255, 0.75);
  font-size: 0.8rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.profile-card__bio {
  margin: 0.5rem 0 0;
  font-size: 0.88rem;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.7;
}

/* ================================================================
   Footer strip
   ================================================================ */

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

/* ================================================================
   Responsive
   ================================================================ */

@media (max-width: 900px) {
  .people-showcase__cards {
    gap: 1rem;
  }
}

@media (max-width: 720px) {
  .about-section__grid {
    grid-template-columns: 1fr;
    gap: var(--space-md);
  }

  .people-showcase__cards {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }

  .carousel-btn {
    display: none;
  }

  .about-section__footer {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
