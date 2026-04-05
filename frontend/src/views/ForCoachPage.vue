<template>
  <main class="inner-page">

    <!-- Page header -->
    <section class="inner-page__hero">
      <div class="section-wrapper">
        <span class="section-label">Partner with us</span>
        <h1 class="inner-page__title">For Coach</h1>
        <div class="divider" />
        <p class="inner-page__lead">
          Edge & Ease is a living project which builds a structured library of coach-curated strategies to support athlete mental resilience. 
          The more coaches, the richer of a tool it becomes. If you would like to contribute your expertise, we would be honored to collaborate.
          Please complete this <a href="https://docs.google.com/forms/d/e/1FAIpQLSfPyDpN8FItb1h_l-eMuosLBg1_Uy0tGjAGiT4MX_GvOnAO6A/viewform" target="_blank" 
          rel="noopener noreferrer">form</a>.
        </p>
        <p class="inner-page__lead">
          All contributions will be reviewed and curated before inclusion.
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
      <h2 class="inner_page_cards">Placeholder</h2>
      <div class="divider" />
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
    tag: 'Coaching since 1985',
    name: 'Pamela Gregory',
    role: 'Olympic and World Coach',
    //body: "We vet every coach personally — not to gatekeep, but to ensure quality for our community. Submit your credentials and a short intro, and our team will be in touch within 48 hours. There's no fee to join during our founding-coach period.",
  },
  {
    tag: 'Coaching since 2006',
    name: 'Colin McManus',
    role: 'National and International Coach',
    //body: "We vet every coach personally — not to gatekeep, but to ensure quality for our community. Submit your credentials and a short intro, and our team will be in touch within 48 hours. There's no fee to join during our founding-coach period.",
  },
  {
    tag: 'Coaching since 2008',
    name: 'Jon Nichols',
    role: 'US Junior National and National Coach in Ice Dance',
    //body: "We vet every coach personally — not to gatekeep, but to ensure quality for our community. Submit your credentials and a short intro, and our team will be in touch within 48 hours. There's no fee to join during our founding-coach period.",
  },
  {
    tag: 'Coaching since 2008',
    name: 'Shira Selis',
    role: 'Figure Skating Coach - skating skills, freestyle, and synchronized skating ',
    //body: "We vet every coach personally — not to gatekeep, but to ensure quality for our community. Submit your credentials and a short intro, and our team will be in touch within 48 hours. There's no fee to join during our founding-coach period.",
  },
  {
    tag: 'Coaching since 2010',
    name: 'Anastasia Cannuscio',
    role: 'National and International Coach',
    //body: 'Sessions end. Stress does not. Edge & Ease lets your clients access your curated tips, breathing exercises, and grounding practices any time — keeping your methodology present in their daily life between your scheduled touchpoints.',
  },
  {
    tag: 'Coacing since 2012',
    name: 'Brooklee Han',
    role: 'National and International Singles and Solo Dance Coach',
    //body: "We vet every coach personally — not to gatekeep, but to ensure quality for our community. Submit your credentials and a short intro, and our team will be in touch within 48 hours. There's no fee to join during our founding-coach period.",
  },
  {
    tag: 'Coaching since 2014',
    name: 'Annie Luong',
    role: 'Figure Skating Coach and Choreographer',
    //body: "We vet every coach personally — not to gatekeep, but to ensure quality for our community. Submit your credentials and a short intro, and our team will be in touch within 48 hours. There's no fee to join during our founding-coach period.",
  },
  {
    tag: 'Coaching since 2020',
    name: 'Leah Krauskopf',
    role: 'University of Delaware Collegiate Team Head Coach',
    //body: 'We handle the infrastructure so you can focus on what matters: your clients. Upload your micro-practices, set your availability, and let the platform surface your guidance to the people who need it most — matched by context, not just keyword.',
  },
  {
    tag: 'Coaching since 2021',
    name: 'Anna Lewis',
    role: 'Figure Skating Coach',
    //body: "We vet every coach personally — not to gatekeep, but to ensure quality for our community. Submit your credentials and a short intro, and our team will be in touch within 48 hours. There's no fee to join during our founding-coach period.",
  },
  {
    //tag: '',
    name: 'Evan Bertz',
    role: 'National Junior Solo Dance & International Pattern Dance Medalists; Senior Solo Dance Competitor',
    //body: "We vet every coach personally — not to gatekeep, but to ensure quality for our community. Submit your credentials and a short intro, and our team will be in touch within 48 hours. There's no fee to join during our founding-coach period.",
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
