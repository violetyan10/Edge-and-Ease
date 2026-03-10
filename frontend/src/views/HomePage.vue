<template>
  <main>
    <HeroSection />
    <TipFinderSection />
    <div id="kit"><StressReliefKitSection /></div>
    <div id="about"><AboutDiscussionSection /></div>
  </main>
</template>

<script setup>
import HeroSection            from '../components/HeroSection.vue'
import TipFinderSection       from '../components/TipFinderSection.vue'
import StressReliefKitSection from '../components/StressReliefKitSection.vue'
import AboutDiscussionSection from '../components/AboutDiscussionSection.vue'
</script>
