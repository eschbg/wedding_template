<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import gateLeft from '../assets/images/gate-left.webp'
import gateRight from '../assets/images/gate-right.webp'
import audioSrc from '../assets/audio/background-music.mp3'
import musicDisc from '../assets/images/music-disc.webp'

// --- Gate Animation ---
const gateRef = ref(null)

// --- Audio ---
const audioRef = ref(null)
const playing = ref(false)

const toggleAudio = async () => {
  if (!audioRef.value) return
  if (playing.value) {
    audioRef.value.pause()
    playing.value = false
  } else {
    try {
      await audioRef.value.play()
      playing.value = true
    } catch { playing.value = false }
  }
}

const startMusicOnInteraction = async () => {
  if (playing.value || !audioRef.value) return
  try {
    await audioRef.value.play()
    playing.value = true
    events.forEach(evt => window.removeEventListener(evt, startMusicOnInteraction))
  } catch { /* blocked by browser */ }
}

const events = ['scroll', 'click', 'touchstart']

onMounted(() => {
  // Open gate after 700ms
  setTimeout(() => {
    if (gateRef.value) gateRef.value.classList.add('open')
  }, 700)
  
  // Listen for user interaction to start music
  events.forEach(evt => window.addEventListener(evt, startMusicOnInteraction, { once: true }))
})

onUnmounted(() => {
  events.forEach(evt => window.removeEventListener(evt, startMusicOnInteraction))
})
</script>

<template>
  <!-- Gate Animation -->
  <div id="loading-gate" ref="gateRef" class="gate-overlay">
    <div class="gate-wing left-wing" :style="{ backgroundImage: `url(${gateLeft})` }"></div>
    <div class="gate-wing right-wing" :style="{ backgroundImage: `url(${gateRight})` }"></div>
  </div>

  <!-- Floating Music Button -->
  <button
    class="music-icon"
    :class="{ playing }"
    type="button"
    @click="toggleAudio"
    aria-label="Phát hoặc tạm dừng nhạc nền"
  >
    <img loading="lazy" :src="musicDisc" alt="Music Disc">
    <span v-if="!playing" class="slash-line" aria-hidden="true"></span>
  </button>
  <audio ref="audioRef" :src="audioSrc" preload="auto" loop></audio>
</template>

<style scoped>
.music-icon {
  position: fixed;
  bottom: 24px;
  left: 24px;
  width: 52px;
  height: 52px;
  cursor: pointer;
  z-index: 10000;
  border-radius: 50%;
  background-color: #ffffff;
  border: 1px solid rgba(197, 168, 128, 0.4);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  outline: none;
  transition: transform 0.3s ease;
  overflow: hidden;
}
.music-icon:hover { transform: scale(1.05); }
.music-icon img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}
.music-icon.playing img { animation: spin 6s linear infinite; }
.slash-line {
  position: absolute;
  width: 65%;
  height: 2px;
  background-color: #c0392b;
  transform: rotate(-45deg);
  pointer-events: none;
}
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>
