<script setup>
import { onMounted } from 'vue'
import FloatingAudio from './components/FloatingAudio.vue'
import Hero from './components/Hero.vue'
import StoryTimeline from './components/StoryTimeline.vue'
import RsvpForm from './components/RsvpForm.vue'
import Couple from './components/Couple.vue'
import TransitionPhoto from './components/TransitionPhoto.vue'
import Gallery from './components/Gallery.vue'
import ThankYou from './components/ThankYou.vue'

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animation')
        // Optional: Stop observing once animated
        observer.unobserve(entry.target)
      }
    })
  }, {
    threshold: 0.1
  })

  document.querySelectorAll('.is-animation').forEach((el) => {
    observer.observe(el)
  })
})
</script>

<template>
  <!-- Gate animation + Music player -->
  <FloatingAudio />

  <!-- Main wedding page content — matches eWedding platform structure -->
  <div class="pageview">
    <div id="webcake-alert-msg" class="w-alert-message-wrapper" style="display: none; z-index: 9999999;"></div>

    <!-- Section 1: Hero — Bá Nam & Thùy Dung, 06.06.2026 -->
    <Hero />

    <!-- Section 2: Save The Date — 06.06.2026, Polaroid photos -->
    <StoryTimeline />

    <!-- Section 3: Invitation — Vu Quy + Thanh Hon details -->
    <RsvpForm />

    <!-- Section 4: Couple — Cô Dâu (Thùy Dung) & Chú Rể (Bá Nam) -->
    <Couple />

    <!-- Section 5: Transition — Full-page photo -->
    <TransitionPhoto />

    <!-- Section 6: Gallery + RSVP Form + Countdown -->
    <Gallery />

    <!-- Section 7: Thank You -->
    <ThankYou />
  </div>
</template>
