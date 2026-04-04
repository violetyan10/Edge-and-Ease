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
          <span class="section-label">Our Coaches</span>
          <h2 class="people-showcase__title">The Faces behind Our Tips</h2>
          <div class="divider" />
          <p class="people-showcase__subtitle">
            Our experienced coaches bring together diverse competition advices.
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
    name: 'Leah Krauskopf',
    //role: ‘CBT Specialist’,
    image: '/coachimages/WhiteSkate.jpg',
    bio: 'Trust yourself and just go out and enjoy it. Remind yourself why you do this and just focus on that. If you go out there and focus on enjoying what you do, you will be able to skate well.',
  },
  {
    id: 2,
    name: 'Anastasia Cannuscio',
    //role: ‘Mindfulness Educator’,
    image: '/coachimages/WhiteSkate.jpg',
    bio: 'Before you even get to the competition the hard work is done. You have put in so many training hours so you can be at your best in this moment. All that is left is to show everyone what you are capable of and enjoy it. Trust your training, I know you can do this. ',
  },
  {
    id: 3,
    name: 'Anna Lewis',
    //role: ‘Somatic Therapist’,
    image: '/coachimages/WhiteSkate.jpg',
    bio: 'Fake it till you make it. Everyone may seem very confident, even if they are all faking it, so just act confident even if you do not feel that way. Control what you can control, and focus in on things you can control. Do not let any other external factors impact ur experience and performance.',
  },
  {
    id: 4,
    name: 'Jon Nichols',
    //role: ‘Group Facilitator’,
    image: '/coachimages/BlackSkate.jpg',
    bio: 'Be in the moment. When your music comes on, connect with what you are doing in that moment. Do not think ahead about the end of the program, what other competitors did on ice before you, your score, or how others might think about you. The preparation is done and just connect with what you are doing in that moment.',
  },
  {
    id: 5,
    name: 'Brooklee Han',
    //role: ‘Breathwork Facilitator’,
    image: '/coachimages/WhiteSkate.jpg',
    bio: 'Trust yourself and your training. Make sure you stay focused on what you can control. Take one element at a time, stay locked into the present and do not let your thoughts run rampage. Make sure you take measured approach and trust yourself.',
  },
  {
    id: 6,
    name: 'Shira Selis',
    //role: ‘Wellness Researcher’,
    image: '/coachimages/WhiteSkate.jpg',
    bio: 'Skate for you. Skate because you love it. Do not worry about the outcome. Just enjoy the process! There will always be more opportunities if this one was not your favorite. ',
  },
  {
    id: 7,
    name: 'Pamela Gregory',
    //role: ‘Lead Coach’,
    image: '/coachimages/WhiteSkate.jpg',
    bio: 'Focus on the performance you are giving because if you try to enjoy your work and the time you put it, then it is your time to shine. That is why you do all the work at home, so you could enjoy your time at the competition.',
  },
  {
    id: 8,
    name: 'Annie Luong',
    //role: ‘Movement & Recovery’,
    image: '/coachimages/WhiteSkate.jpg',
    bio: 'When you are nervous, just accept it. In general, when people try to fight how nervous they are, the anxiety increases. Accept that it happens instead of pushing it away. Learn to work with it and work through it.',
  },
  {
    id: 9,
    name: 'Evan Bertz',
    //role: ‘Sleep & Rhythm Coach’,
    image: '/coachimages/BlackSkate.jpg',
    bio: 'Perform. Skating is such a beautiful thing and everybody is so different. You just need to go out there, enjoy what you are doing and have fun with it. Do not get too caught up in scores and placements because it tends to make you loose focus on what skating really is, which is an art. ',
  },
  {
    id: 10,
    name: 'Colin McManus',
    //role: ‘Community Lead’,
    image: '/coachimages/BlackSkate.jpg',
    bio: 'There is no reason one cannot show up to a competition most prepared. One thing you can bet on is the work you put in beforehand. When you stand on ice and your music is about to start, you can say to yourself that you’ve done everything you can to be prepared. This will carry you further and give you confidence.',
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
