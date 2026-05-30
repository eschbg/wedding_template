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
      <div v-else class="content-wrapper" :class="{ 'is-scrolling': shouldScroll }">
        <!-- Duplicate messages for infinite scroll effect -->
        <div
          v-for="(msg, index) in displayMessages"
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
import Papa from 'papaparse';

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

const GOOGLE_SHEET_CSV_URL =
  "https://docs.google.com/spreadsheets/d/1qLyN6E3APjHWTShALFNqDBAlrF6Fz_2vxpDw0DcIS1A/export?format=csv&gid=0";

const shouldScroll = computed(() => messages.value.length > 3);

// Duplicate messages to create infinite scroll effect if there are too few
const displayMessages = computed(() => {
  if (messages.value.length === 0) return [];
  if (!shouldScroll.value) return messages.value;
  
  let dups = [...messages.value];
  while (dups.length < 20) {
    dups = dups.concat(messages.value);
  }
  return dups;
});

const fetchMessages = () => {
  loading.value = true;
  error.value = null;

  Papa.parse(`${GOOGLE_SHEET_CSV_URL}&t=${Date.now()}`, {
    download: true,
    header: true,
    complete: (results) => {
      loading.value = false;
      const data = results.data;
      if (data && data.length > 0) {
        messages.value = data
          .filter((row) => row['Lời chúc'] && row['Lời chúc'].trim() !== '')
          .map((row) => ({
            name: row['Tên khách mời'] || 'Khách',
            wish: row['Lời chúc'],
          }))
          .reverse();
      } else {
        messages.value = [];
      }
    },
    error: (err) => {
      console.error("Failed to fetch messages", err);
      error.value = "Không thể tải lời chúc lúc này.";
      loading.value = false;
    }
  });
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

.content-wrapper {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding-bottom: 20px;
}

.content-wrapper.is-scrolling {
  animation: marquee-up 30s linear infinite;
}

.messages-wrapper.paused .content-wrapper.is-scrolling {
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
