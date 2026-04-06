<template>
  <main class="inner-page">

    <!-- Page header -->
    <section class="inner-page__hero">
      <div class="section-wrapper">
        <span class="section-label">The people behind it</span>
        <h1 class="inner-page__title">About Us</h1>
        <div class="divider" />
        <p class="inner-page__lead">
          Edge & Ease is a student-led initiative supporting mental wellness in
          competitive skating through coach-curated guidance and digital tools.
        </p>
        <br>
        <p class="inner-page__lead">
          This tool provides general advice and is not a substitute for professional
          mental health services.
        </p>

      </div>
    </section>

    <!-- Team cards -->
    <section class="inner-page__cards">
      <div class="section-wrapper cards-stack">
        <ProfileCard
          v-for="(member, i) in team"
          :key="member.name"
          v-bind="member"
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

// Collect card refs and observe them for scroll-reveal
const cardRefs = []
function registerCard(el) {
  if (el) cardRefs.push(el)
}
onMounted(() => {
  cardRefs.forEach((el) => observe(el.$el ?? el))
})

// Placeholder team data — replace with real content
// Images live in frontend/public/team/ and are referenced as /team/filename.jpg
const team = [
  {
    tag: 'Founder',
    name: 'Violet Yan',
    role: 'Student and Skater',
    imageSrc: '/team/violet.jpeg',
    imageAlt: 'Violet Yan ice skating', 
    body: 'Violet is a competitive solo ice dancer and high school student passionate about integrating technology and athlete wellness. She founded Edge & Ease to provide accessible, coach-guided mental support for skaters navigating competitive pressure.',
  },
  // {
  //   tag: 'Co-Founder & CTO',
  //   name: 'Mike Yan',
  //   role: 'Engineer & Mindfulness Practitioner',
  //   imageSrc: '/team/mike.jpg',
  //   imageAlt: 'Mike Yan ice skating',
  //   body: 'Mike blends 12 years of full-stack engineering with a daily mindfulness practice rooted in Zen tradition. He leads the technical vision for the platform and ensures every interaction feels considered — never rushed.',
  // },
  // {
  //   tag: 'Head of Coaching',
  //   name: 'Seren Williams',
  //   role: 'Clinical Psychologist & CBT Specialist',
  //   body: 'Seren brings rigorous clinical grounding to every tip and practice on the platform. With a background in cognitive behavioural therapy and somatic work, she oversees the quality and integrity of all coaching content.',
  // },
  // {
  //   tag: 'Design Lead',
  //   name: 'Isla Park',
  //   role: 'Product Designer & Visual Storyteller',
  //   body: "Isla shapes the look, feel, and flow of Edge & Ease. She believes design is an act of care — every colour choice, every animation, every word exists to make you feel a little more at ease the moment you arrive.",
  // },
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
