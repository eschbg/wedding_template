<template>
  <div v-if="isOpen" class="floating-messages-container">
    <div class="messages-wrapper" :class="{ 'paused': isPaused }" @mouseenter="isPaused = true" @mouseleave="isPaused = false">
      <div v-if="loading" class="loading-state">
        <span class="pulse-text">Đang tải lời chúc...</span>
      </div>
      <div v-else-if="error" class="error-state">
        {{ error }}
      </div>
      <div v-else-if="messages.length === 0" class="empty-state">
        Chưa có lời chúc nào.
      </div>
      <div v-else class="scrolling-content">
        <!-- Duplicate messages for infinite scroll effect -->
        <div
          v-for="(msg, index) in duplicatedMessages"
          :key="index"
          class="message-bubble"
        >
          <span class="message-author">{{ msg.name }}:</span> 
          <span class="message-text">{{ msg.wish }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed, onMounted, onUnmounted } from 'vue';
import axios from 'axios';

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false,
  },
  refreshTrigger: {
    type: Number,
    default: 0
  }
});

const emit = defineEmits(['close']);

const messages = ref([]);
const loading = ref(false);
const error = ref(null);
const isPaused = ref(false);

const GOOGLE_SCRIPT_URL =
  "https://script.google.com/macros/s/AKfycbybQ-g85SKegO0WAoLW_j5XTtEo61Z_AB_yw-YbvXQoRdu3L2gYFPS4HMhkN5ZoHO3F/exec";

// Duplicate messages to create infinite scroll effect if there are too few
const duplicatedMessages = computed(() => {
  if (messages.value.length === 0) return [];
  // If we have very few messages, duplicate them many times to fill the screen
  let dups = [...messages.value];
  while (dups.length < 20) {
    dups = dups.concat(messages.value);
  }
  return dups;
});

const fetchMessages = async () => {
  loading.value = true;
  error.value = null;
  try {
    const response = await axios.get(GOOGLE_SCRIPT_URL);
    if (response.data && response.data.status === 'success') {
      messages.value = response.data.data
        .filter((row) => row.wishContent && row.wishContent.trim() !== '')
        .map((row) => ({
          name: row.fullName || 'Khách',
          wish: row.wishContent,
        }))
        .reverse();
    } else {
      throw new Error("API not returning correct format.");
    }
  } catch (err) {
    console.error("Failed to fetch messages", err);
    // Fallback Dummy data
    messages.value = [
      { name: "Lan Anh", wish: "🕊️ Tân hôn hạnh phúc, trăm năm bên nhau!" },
      { name: "Lan Anh", wish: "💍 Chúc cho tình yêu của hai bạn mỗi ngày một lớn mạnh!" },
      { name: "Tùng", wish: "🕊️ Tân hôn hạnh phúc, trăm năm bên nhau!" },
      { name: "Ngọc", wish: "💖 💖 Chúc hai bạn trăm năm hạnh phúc!" },
      { name: "Erik", wish: "🕊️ Tân hôn hạnh phúc, trăm năm bên nhau!" },
    ];
  } finally {
    loading.value = false;
  }
};

watch(() => props.isOpen, (newVal) => {
  if (newVal) {
    fetchMessages();
  }
});

watch(() => props.refreshTrigger, () => {
  if (props.isOpen) {
    fetchMessages();
  }
});

let intervalId;
onMounted(() => {
  // optionally pre-fetch if needed
});
onUnmounted(() => {
  clearInterval(intervalId);
});

</script>

<style scoped>
.floating-messages-container {
  position: fixed;
  bottom: 80px; /* Right above the toggle button */
  right: 20px;
  width: 320px;
  height: 50vh;
  max-height: 400px;
  z-index: 9998;
  pointer-events: none; /* Let clicks pass through empty areas */
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  overflow: hidden;
  /* Fading top and bottom edges */
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, black 20%, black 80%, transparent 100%);
  mask-image: linear-gradient(to bottom, transparent 0%, black 20%, black 80%, transparent 100%);
}

.messages-wrapper {
  position: absolute;
  bottom: 0;
  width: 100%;
  pointer-events: auto; /* Enable hover on messages */
}

.scrolling-content {
  display: flex;
  flex-direction: column;
  gap: 12px;
  animation: marquee-up 30s linear infinite;
  padding-bottom: 20px;
}

.messages-wrapper.paused .scrolling-content {
  animation-play-state: paused;
}

.message-bubble {
  background-color: rgba(244, 187, 196, 0.95); /* Pinkish background matching the image */
  color: #fff;
  padding: 10px 14px;
  border-radius: 12px;
  font-family: 'Roboto', sans-serif;
  font-size: 14px;
  line-height: 1.4;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  margin-left: auto;
  max-width: 90%;
  align-self: flex-end; /* Align bubbles to the right */
}

.message-author {
  font-weight: 700;
  margin-right: 4px;
}

.message-text {
  font-weight: 400;
}

.loading-state, .error-state, .empty-state {
  text-align: right;
  color: #fff;
  background: rgba(0,0,0,0.5);
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 13px;
  align-self: flex-end;
  margin-left: auto;
}

.pulse-text {
  animation: pulse 1.5s infinite;
}

@keyframes marquee-up {
  0% { transform: translateY(0); }
  100% { transform: translateY(-50%); } 
  /* -50% assumes we duplicated content enough to loop seamlessly */
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* Mobile responsive */
@media (max-width: 480px) {
  .floating-messages-container {
    width: 280px;
    height: 60vh;
  }
}
</style>
