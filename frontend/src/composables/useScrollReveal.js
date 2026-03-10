/**
 * useScrollReveal — composable that watches a list of elements and adds
 * the "visible" class when they enter the viewport.
 *
 * Usage in a component:
 *
 *   import { useScrollReveal } from '@/composables/useScrollReveal'
 *   const { observe } = useScrollReveal()
 *
 *   // In template: <div ref="el" class="reveal"> ... </div>
 *   // In setup:    onMounted(() => observe(el.value))
 *
 * The composable uses a single shared IntersectionObserver instance so it is
 * cheap to call from many components.
 */

import { onBeforeUnmount } from 'vue'

// One shared observer for the whole app — created lazily.
let _observer = null

function getObserver() {
  if (_observer) return _observer

  _observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
          // Once revealed, stop watching this element.
          _observer.unobserve(entry.target)
        }
      })
    },
    {
      threshold: 0.12,       // trigger when 12% of the element is visible
      rootMargin: '0px 0px -40px 0px', // slight bottom offset for a nicer feel
    }
  )

  return _observer
}

export function useScrollReveal() {
  const observed = []

  /**
   * Start observing one or more elements.
   * Accepts an Element, a Ref, or an array of either.
   */
  function observe(...targets) {
    const obs = getObserver()
    targets.flat().forEach((t) => {
      const el = t?.$el ?? t  // support component refs
      if (el instanceof Element) {
        obs.observe(el)
        observed.push(el)
      }
    })
  }

  // Clean up when the component that called this composable unmounts.
  onBeforeUnmount(() => {
    const obs = getObserver()
    observed.forEach((el) => obs.unobserve(el))
  })

  return { observe }
}
