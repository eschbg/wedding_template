<template>
  <div
    v-if="isOpen"
    class="guestbook-modal-overlay"
    @click.self="close"
  >
    <div class="guestbook-modal-content">
      <div class="modal-header">
        <h3>Sổ Lưu Bút</h3>
        <button class="close-btn" @click="close">&times;</button>
      </div>
      <div class="modal-body">
        <div v-if="loading" class="loading-state">
          Đang tải lời chúc...
        </div>
        <div v-else-if="error" class="error-state">
          {{ error }}
        </div>
        <div v-else-if="messages.length === 0" class="empty-state">
          Chưa có lời chúc nào. Hãy là người đầu tiên gửi lời chúc nhé!
        </div>
        <div v-else class="messages-list">
          <div
            v-for="(msg, index) in messages"
            :key="index"
            class="message-card"
          >
            <div class="message-header">
              <span class="message-author">{{ msg.name }}</span>
              <span class="message-time" v-if="msg.time">{{ msg.time }}</span>
            </div>
            <div class="message-content">
              {{ msg.wish }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(['close']);

const messages = ref([]);
const loading = ref(false);
const error = ref(null);

const GOOGLE_SCRIPT_URL =
  "https://script.google.com/macros/s/AKfycbybQ-g85SKegO0WAoLW_j5XTtEo61Z_AB_yw-YbvXQoRdu3L2gYFPS4HMhkN5ZoHO3F/exec";

const fetchMessages = async () => {
  loading.value = true;
  error.value = null;
  try {
    const response = await axios.get(GOOGLE_SCRIPT_URL);
    if (response.data && response.data.status === 'success') {
      // Map data from Google Sheets format
      // Expecting response.data.data to be an array of objects: { timestamp, fullName, guestOf, wishContent, attendanceStatus }
      messages.value = response.data.data
        .filter((row) => row.wishContent && row.wishContent.trim() !== '')
        .map((row) => {
          let formattedTime = '';
          if (row.timestamp) {
            const date = new Date(row.timestamp);
            formattedTime = date.toLocaleDateString('vi-VN');
          }
          return {
            name: row.fullName || 'Khách ẩn danh',
            wish: row.wishContent,
            time: formattedTime,
          };
        })
        .reverse(); // Show latest first
    } else {
      // Fallback for when the Google Apps Script hasn't been updated yet
      throw new Error("API not returning correct format.");
    }
  } catch (err) {
    console.error("Failed to fetch messages", err);
    // Dummy data while testing / waiting for user to update App Script
    messages.value = [
      { name: "Người bạn thân", wish: "Chúc hai bạn trăm năm hạnh phúc, răng long đầu bạc nhé!", time: "Hôm nay" },
      { name: "Anh Chị Đồng Nghiệp", wish: "Chúc gia đình nhỏ luôn ngập tràn tiếng cười và niềm vui.", time: "Hôm qua" },
    ];
    // error.value = "Không thể tải lời chúc lúc này."; // Optional: Show error instead of dummy
  } finally {
    loading.value = false;
  }
};

watch(() => props.isOpen, (newVal) => {
  if (newVal) {
    fetchMessages();
  }
});

const close = () => {
  emit('close');
};
</script>

<style scoped>
.guestbook-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: 1000002;
  display: flex;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(3px);
}

.guestbook-modal-content {
  background: #fff;
  width: 90%;
  max-width: 400px;
  max-height: 80vh;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
  animation: slideUp 0.3s ease-out;
}

.modal-header {
  padding: 16px 20px;
  border-bottom: 1px solid #f0f0f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fdfbf7;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
}

.modal-header h3 {
  margin: 0;
  font-family: 'Taviraj', serif;
  color: #6d583d;
  font-size: 20px;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  line-height: 1;
  color: #888;
  cursor: pointer;
  padding: 0;
}

.modal-body {
  padding: 20px;
  overflow-y: auto;
  flex: 1;
  background: #faf8f5;
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
}

.loading-state, .error-state, .empty-state {
  text-align: center;
  color: #888;
  padding: 20px 0;
  font-family: 'Roboto', sans-serif;
  font-size: 14px;
}

.messages-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.message-card {
  background: #fff;
  padding: 14px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  border: 1px solid #f0eae1;
}

.message-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  align-items: center;
}

.message-author {
  font-weight: bold;
  color: #555;
  font-size: 14px;
  font-family: 'Roboto', sans-serif;
}

.message-time {
  font-size: 11px;
  color: #aaa;
}

.message-content {
  color: #444;
  font-size: 13px;
  line-height: 1.5;
  font-family: 'Roboto', sans-serif;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
