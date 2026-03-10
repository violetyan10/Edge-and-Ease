import { createRouter, createWebHistory } from 'vue-router'
import HomePage     from '../views/HomePage.vue'
import OurTeamPage  from '../views/OurTeamPage.vue'
import ForCoachPage from '../views/ForCoachPage.vue'

const routes = [
  { path: '/',          component: HomePage,     meta: { title: 'Edge & Ease — Find Your Calm' } },
  { path: '/our-team',  component: OurTeamPage,  meta: { title: 'Our Team — Edge & Ease' } },
  { path: '/for-coach', component: ForCoachPage, meta: { title: 'For Coach — Edge & Ease' } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  // Always scroll to top on route change
  scrollBehavior: () => ({ top: 0, behavior: 'smooth' }),
})

// Update the document title on every navigation
router.afterEach((to) => {
  document.title = to.meta.title ?? 'Edge & Ease'
})

export default router
