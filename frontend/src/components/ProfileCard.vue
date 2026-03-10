<!--
  ProfileCard.vue — shared card used by OurTeamPage and ForCoachPage.

  Props:
    imageSrc   — optional image URL; shows a placeholder block if omitted
    imageAlt   — alt text for the image
    tag        — small label above the name (e.g. "Co-Founder", "Benefit")
    name       — primary heading
    role       — secondary line (subtitle / role)
    body       — paragraph text
    delay      — CSS transition-delay in ms for stagger (default 0)
-->
<template>
  <article
    class="profile-card reveal"
    :style="delay ? `transition-delay: ${delay}ms` : ''"
  >
    <!-- Image column -->
    <div class="profile-card__img-wrap">
      <img
        v-if="imageSrc"
        :src="imageSrc"
        :alt="imageAlt || name"
        class="profile-card__img"
      />
      <div v-else class="profile-card__img-placeholder" aria-hidden="true">
        <span class="profile-card__img-icon">◎</span>
      </div>
    </div>

    <!-- Text column -->
    <div class="profile-card__body">
      <span v-if="tag" class="section-label profile-card__tag">{{ tag }}</span>
      <h3 class="profile-card__name">{{ name }}</h3>
      <p class="profile-card__role">{{ role }}</p>
      <div class="divider profile-card__divider" />
      <p class="profile-card__text">{{ body }}</p>
    </div>
  </article>
</template>

<script setup>
defineProps({
  imageSrc: { type: String,  default: null },
  imageAlt: { type: String,  default: '' },
  tag:      { type: String,  default: '' },
  name:     { type: String,  required: true },
  role:     { type: String,  default: '' },
  body:     { type: String,  default: '' },
  delay:    { type: Number,  default: 0 },
})
</script>

<style scoped>
/* ---- Card shell ---- */
.profile-card {
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: var(--space-md);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-sm);
  transition:
    box-shadow var(--transition),
    transform  var(--transition),
    /* preserve the reveal animation transition */
    opacity    0.7s ease,
    translate  0.7s ease;
}

.profile-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-3px);
}

/* ---- Image column ---- */
.profile-card__img-wrap {
  flex-shrink: 0;
}

.profile-card__img {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: var(--radius-md);
}

.profile-card__img-placeholder {
  width: 100%;
  aspect-ratio: 1;
  background: var(--color-accent-light);
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
}

.profile-card__img-icon {
  font-size: 2.5rem;
  color: var(--color-accent-dark);
  opacity: 0.5;
}

/* ---- Text column ---- */
.profile-card__body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.4rem;
}

.profile-card__tag  { margin-bottom: 0.1rem; }
.profile-card__divider { margin: 0.5rem 0 0.75rem; }

.profile-card__name {
  font-size: 1.4rem;
  font-family: var(--font-display);
  font-weight: 400;
}

.profile-card__role {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--color-accent-dark);
  letter-spacing: 0.03em;
}

.profile-card__text {
  font-size: 0.97rem;
  color: var(--color-text-muted);
  line-height: 1.75;
}

/* ---- Responsive: stack vertically on mobile ---- */
@media (max-width: 640px) {
  .profile-card {
    grid-template-columns: 1fr;
  }

  .profile-card__img-wrap {
    max-width: 160px;
  }
}
</style>
