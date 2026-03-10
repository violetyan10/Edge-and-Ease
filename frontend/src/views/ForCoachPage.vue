<template>
  <main class="inner-page">

    <!-- Page header -->
    <section class="inner-page__hero">
      <div class="section-wrapper">
        <span class="section-label">Partner with us</span>
        <h1 class="inner-page__title">For Coach</h1>
        <div class="divider" />
        <p class="inner-page__lead">
          Edge & Ease is built for coaches who want to extend their impact beyond the
          session. Whether you're a licensed therapist, a certified life coach, or a
          somatic practitioner — there's a place for your voice here.
        </p>
      </div>
    </section>

    <!-- Feature cards -->
    <section class="inner-page__cards">
      <div class="section-wrapper cards-stack">
        <ProfileCard
          v-for="(item, i) in features"
          :key="item.name"
          v-bind="item"
          :delay="i * 130"
          :ref="(el) => registerCard(el)"
        />
      </div>
    </section>

  </main>
</template>

<script setup>
import { onMounted } from 'vue'
import ProfileCard from '../components/ProfileCard.vue'
import { useScrollReveal } from '../composables/useScrollReveal'

const { observe } = useScrollReveal()

const cardRefs = []
function registerCard(el) {
  if (el) cardRefs.push(el)
}
onMounted(() => {
  cardRefs.forEach((el) => observe(el.$el ?? el))
})

// Placeholder coach feature content
const features = [
  {
    tag: 'Coaching Support',
    name: 'A Platform Built Around You',
    role: 'Your tools, your tone, your clients',
    body: 'We handle the infrastructure so you can focus on what matters: your clients. Upload your micro-practices, set your availability, and let the platform surface your guidance to the people who need it most — matched by context, not just keyword.',
  },
  {
    tag: 'Platform Benefits',
    name: 'Reach Beyond the Session',
    role: 'Ongoing impact between appointments',
    body: 'Sessions end. Stress does not. Edge & Ease lets your clients access your curated tips, breathing exercises, and grounding practices any time — keeping your methodology present in their daily life between your scheduled touchpoints.',
  },
  {
    tag: 'Joining Process',
    name: 'Simple, Respectful Onboarding',
    role: 'Up and running in under a week',
    body: "We vet every coach personally — not to gatekeep, but to ensure quality for our community. Submit your credentials and a short intro, and our team will be in touch within 48 hours. There's no fee to join during our founding-coach period.",
  },
]
</script>

<style scoped>
.cards-stack {
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
  padding-bottom: var(--space-xl);
}
</style>
