<script setup>
import FloatingAudio from './components/FloatingAudio.vue'
import Hero from './components/Hero.vue'
import StoryTimeline from './components/StoryTimeline.vue'
import RsvpForm from './components/RsvpForm.vue'
import Couple from './components/Couple.vue'
import TransitionPhoto from './components/TransitionPhoto.vue'
import Gallery from './components/Gallery.vue'
import ThankYou from './components/ThankYou.vue'
</script>

<template>
  <!-- Gate animation + Music player -->
  <FloatingAudio />

  <!-- Main wedding page content — matches eWedding platform structure -->
  <div class="pageview">
    <div id="webcake-alert-msg" class="w-alert-message-wrapper" style="display: none; z-index: 9999999;"></div>

    <!-- Section 1: Hero — Đức Dương & Thanh Hằng, 20.09.2026 -->
    <Hero />

    <!-- Section 2: Save The Date — 20.09.2026, Polaroid photos -->
    <StoryTimeline />

    <!-- Section 3: Invitation — Vu Quy + Thanh Hon details -->
    <RsvpForm />

    <!-- Section 4: Couple — Cô Dâu (Thanh Hằng) & Chú Rể (Đức Dương) -->
    <Couple />

    <!-- Section 5: Transition — Full-page photo -->
    <TransitionPhoto />

    <!-- Section 6: Gallery + RSVP Form + Countdown -->
    <Gallery />

    <!-- Section 7: Thank You -->
    <ThankYou />
  </div>
</template>
