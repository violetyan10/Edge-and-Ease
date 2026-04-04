<template>
  <!-- ── Sticky nav ──────────────────────────────────────────── -->
  <header class="nav" :class="{ 'nav--scrolled': scrolled }">
    <div class="nav__inner">

      <!-- Logo → always goes home -->
      <RouterLink to="/" class="nav__logo-link" aria-label="Edge & Ease home">
        <img :src="logo" alt="Edge & Ease" class="nav__logo-img" />
      </RouterLink>

      <!-- Right-side nav -->
      <nav class="nav__links" aria-label="Site navigation">
        <RouterLink to="/our-team"  class="nav__btn" active-class="nav__btn--active">About Us</RouterLink>
        <span class="nav__sep" aria-hidden="true" />
        <RouterLink to="/for-coach" class="nav__btn" active-class="nav__btn--active">For Coach</RouterLink>
      </nav>

    </div>
  </header>

  <!-- ── Page content ────────────────────────────────────────── -->
  <RouterView v-slot="{ Component }">
    <Transition name="page" mode="out-in">
      <component :is="Component" />
    </Transition>
  </RouterView>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import logo from './Edge & Ease - Logo.jpg'

const scrolled = ref(false)
function handleScroll() { scrolled.value = window.scrollY > 60 }
onMounted(()        => window.addEventListener('scroll', handleScroll, { passive: true }))
onBeforeUnmount(()  => window.removeEventListener('scroll', handleScroll))
</script>

<style>
/* ══════════════════════════════════════════════════════════════
   Navigation bar
   ══════════════════════════════════════════════════════════════ */
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 1rem var(--space-md);
  transition: background-color 0.35s ease, box-shadow 0.35s ease, padding 0.35s ease;
}

.nav--scrolled {
  background-color: rgba(249, 246, 242, 0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  box-shadow: 0 1px 0 var(--color-border);
  padding: 0.65rem var(--space-md);
}

.nav__inner {
  max-width: 960px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* ── Logo ── */
.nav__logo-link {
  display: flex;
  align-items: center;
  text-decoration: none;
  flex-shrink: 0;
}

.nav__logo-img {
  height: 44px;
  width: 44px;
  object-fit: cover;
  border-radius: 50%;
  transition: opacity var(--transition);
}
.nav__logo-img:hover { opacity: 0.82; }

/* ── Nav buttons ── */
.nav__links {
  display: flex;
  align-items: center;
  gap: 0.35rem;           /* tight gap; visual spacing comes from btn padding */
}

/* Vertical separator */
.nav__sep {
  display: block;
  width: 1px;
  height: 16px;
  background-color: var(--color-border);
  margin: 0 0.4rem;
  flex-shrink: 0;
}

.nav__btn {
  /* Reset */
  font-family: var(--font-body);
  font-size: 0.875rem;
  font-weight: 500;
  text-decoration: none;
  background: none;
  border: none;
  cursor: pointer;

  /* Layout */
  display: inline-flex;
  align-items: center;
  padding: 0.45rem 1rem;
  border-radius: var(--radius-full);

  /* Default colour */
  color: var(--color-text-muted);

  /* Smooth hover */
  transition:
    background-color 0.22s ease,
    color            0.22s ease;
}

/* Hover — same for both buttons */
.nav__btn:hover {
  background-color: rgba(196, 135, 107, 0.1);
  color: var(--color-clay-dark);
}

/* Active / current route */
.nav__btn--active {
  background-color: var(--color-clay);
  color: #fff !important;
}

.nav__btn--active:hover {
  background-color: var(--color-clay-dark);
}

/* ── Page transition ── */
.page-enter-active,
.page-leave-active {
  transition: opacity 0.22s ease, transform 0.22s ease;
}
.page-enter-from { opacity: 0; transform: translateY(10px); }
.page-leave-to   { opacity: 0; transform: translateY(-6px); }

/* ── Mobile ── */
@media (max-width: 500px) {
  .nav__btn  { font-size: 0.8rem; padding: 0.4rem 0.75rem; }
  .nav__sep  { margin: 0 0.2rem; }
}
</style>
