<template>
  <!-- Full-viewport hero with a layered background and fade-in entrance -->
  <section class="hero">
    <div class="hero__bg-layer" aria-hidden="true" />

    <div class="hero__content">
      <!-- Eyebrow label -->
      <span class="section-label hero__label">Wellness for the modern mind</span>

      <!-- Main headline -->
      <h1 class="hero__title">
        Find your edge.<br />
        <em>Ease into calm.</em>
      </h1>

      <!-- Subtitle -->
      <p class="hero__subtitle">
        Personalised stress-relief guidance, grounding rituals, and a community
        that understands — all in one quiet corner of the internet.
      </p>

      <!-- CTA -->
      <a href="#tip-finder" class="btn btn-primary hero__cta">
        Find my calm
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
          <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </a>

      <!-- Scroll indicator -->
      <div class="hero__scroll-hint" aria-hidden="true">
        <span class="hero__scroll-line" />
        <span class="hero__scroll-text">scroll</span>
      </div>
    </div>
  </section>
</template>

<script setup>
// Hero section — no scroll-reveal needed here since it's always visible above the fold.
// The fade-in is handled purely by CSS animation below.
</script>

<style scoped>
/* ---- Layout ---- */
.hero {
  position: relative;
  min-height: 100svh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background-color: var(--color-bg);
}

/* Decorative background blobs */
.hero__bg-layer {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 60% 50% at 70% 30%, rgba(124,158,138,.18) 0%, transparent 70%),
    radial-gradient(ellipse 45% 45% at 20% 75%, rgba(196,135,107,.12) 0%, transparent 65%);
  pointer-events: none;
}

/* ---- Content ---- */
.hero__content {
  position: relative;
  z-index: 1;
  max-width: 720px;
  padding: 5rem var(--space-md) var(--space-xl);
  text-align: center;
  animation: heroFadeUp 0.9s ease both;
}

.hero__label {
  display: block;
  margin-bottom: var(--space-sm);
}

.hero__title {
  font-size: clamp(2.6rem, 6vw, 4.2rem);
  font-weight: 400;
  margin-bottom: var(--space-md);
  color: var(--color-text);
}

.hero__title em {
  font-style: italic;
  color: var(--color-accent-dark);
}

.hero__subtitle {
  font-size: 1.125rem;
  color: var(--color-text-muted);
  max-width: 520px;
  margin: 0 auto var(--space-lg);
  line-height: 1.75;
}

.hero__cta {
  font-size: 1rem;
  padding: 0.9rem 2.2rem;
}

/* ---- Scroll hint ---- */
.hero__scroll-hint {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  margin-top: var(--space-lg);
  opacity: .45;
  animation: heroFadeUp 1.2s ease 0.6s both;
}

.hero__scroll-line {
  display: block;
  width: 1px;
  height: 42px;
  background: linear-gradient(to bottom, transparent, var(--color-text-muted));
  animation: scrollPulse 2s ease-in-out infinite;
}

.hero__scroll-text {
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--color-text-muted);
}

/* ---- Animations ---- */
@keyframes heroFadeUp {
  from { opacity: 0; transform: translateY(28px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes scrollPulse {
  0%, 100% { opacity: .4; transform: scaleY(1); }
  50%       { opacity: .9; transform: scaleY(1.15); }
}

/* ---- Responsive ---- */
@media (max-width: 600px) {
  .hero__title { font-size: 2.2rem; }
  .hero__subtitle { font-size: 1rem; }
}
</style>
