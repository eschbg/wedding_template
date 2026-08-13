<!-- Section 6: w-fi0xg7tu — Gallery + RSVP Form + Countdown -->
<script setup>
import { computed, onMounted, onUnmounted, ref } from "vue";
import axios from "axios";

// --- Local gallery images ---
import gallery5 from "../assets/images/gallery-5.webp";
import gallery6 from "../assets/images/gallery-6.webp";
import gallery0 from "../assets/images/gallery-0.webp";
import gallery1 from "../assets/images/gallery-1.webp";
import gallery2 from "../assets/images/gallery-2.webp";
import gallery3 from "../assets/images/gallery-3.webp";
import gallery4 from "../assets/images/gallery-4.webp";
import gallery7 from "../assets/images/gallery-7.webp";
import gallery8 from "../assets/images/gallery-8.webp";
import gallery9 from "../assets/images/gallery-9.webp";
import gallery10 from "../assets/images/gallery-10.webp";

// --- Calendar image ---
import calendarImg from "../assets/images/calendar.webp";


// === GALLERY ===
const images = [
  gallery5,
  gallery6,
  gallery7,
  gallery8,
  gallery9,
  gallery0,
  gallery1,
  gallery2,
  gallery3,
  gallery4,
  gallery10,
];
const currentIndex = ref(0);
let galleryInterval;

const goTo = (index) => {
  currentIndex.value = (index + images.length) % images.length;
};
const nextSlide = () => goTo(currentIndex.value + 1);
const prevSlide = () => goTo(currentIndex.value - 1);

// === COUNTDOWN ===
// Countdown logic removed – replaced with static calendar image.

// === RSVP FORM ===
const formName = ref("");
const formGuest = ref("");
const formWish = ref("");
const formAttend = ref("");
const isSubmitting = ref(false);
const submitSuccess = ref(false);
const submitError = ref(null);

const api = axios.create({ baseURL: "http://localhost:8080", timeout: 10000 });

const GOOGLE_SCRIPT_URL =
  "https://script.google.com/macros/s/AKfycbybQ-g85SKegO0WAoLW_j5XTtEo61Z_AB_yw-YbvXQoRdu3L2gYFPS4HMhkN5ZoHO3F/exec";

const submitForm = async () => {
  isSubmitting.value = true;
  submitError.value = null;
  try {
    const formData = new FormData();
    formData.append("fullName", formName.value.trim());
    formData.append("guestOf", formGuest.value.trim());
    formData.append("wishContent", formWish.value.trim());
    formData.append(
      "attendanceStatus",
      formAttend.value === "Có, chắc chắn tôi sẽ đến" ? "Có" : "Không",
    );

    // Dùng fetch với mode 'no-cors' để tránh lỗi chặn CORS từ Google Apps Script
    await fetch(GOOGLE_SCRIPT_URL, {
      method: "POST",
      body: formData,
      mode: "no-cors",
    });

    // Lưu ý: với mode 'no-cors' thì fetch sẽ không trả về lỗi rõ ràng nên ta cứ hiện thông báo thành công
    submitSuccess.value = true;
    formName.value = "";
    formGuest.value = "";
    formWish.value = "";
    formAttend.value = "";
  } catch (err) {
    console.warn("Network error or script failure:", err.message);
    // Tùy chọn: vẫn hiện popup báo gửi thành công (vì form đã bay đi) hoặc báo lỗi
    submitSuccess.value = true;
  } finally {
    isSubmitting.value = false;
  }
};

onMounted(() => {
  galleryInterval = setInterval(nextSlide, 4000);
  // Countdown interval removed.
});

onUnmounted(() => {
  clearInterval(galleryInterval);
  // No countdown interval to clear.
});
</script>

<template>
  <div id="w-fi0xg7tu" class="com-section" data-section>
    <div class="section-wrapper full-width full-height p-relative">
      <div class="section-background p-absolute full-width full-height"></div>
      <div class="section-container full-height p-relative">
        <!-- Background image -->
        <div id="w-vnqw8o3l" class="com-image-block p-absolute">
          <div class="full-width full-height">
            <div
              class="image-block-css p-relative full-width full-height full-mask-size mask-position"
            >
              <div
                class="image-background p-absolute"
                role="img"
                aria-label=""
              ></div>
              <div class="image-gradient-border"></div>
            </div>
          </div>
        </div>

        <!-- "album" text -->
        <div id="w-kpdm3hjm" class="com-text-block p-absolute is-animation">
          <div class="text-block">
            <h1 class="text-block-css full-width">album&nbsp;<br /></h1>
          </div>
        </div>

        <!-- "of" text -->
        <div id="w-twb2y15g" class="com-text-block p-absolute is-animation">
          <div class="text-block">
            <h1 class="text-block-css full-width">of<br /></h1>
          </div>
        </div>

        <!-- "love" text -->
        <div id="w-gvinnq2p" class="com-text-block p-absolute is-animation">
          <div class="text-block">
            <h1 class="text-block-css full-width">love<br /></h1>
          </div>
        </div>

        <!-- Gallery -->
        <div id="w-9d3y5ld4" class="com-gallery p-absolute">
          <div class="gallery-wrapper full-width full-height p-absolute">
            <div class="gallery-view p-absolute">
              <!-- Gallery view items — bound to local images via :style -->
              <div
                v-for="(image, index) in images"
                :key="index"
                class="gallery-view-item p-absolute"
                :class="{
                  active: index === currentIndex,
                  right: index === (currentIndex + 1) % images.length,
                  left:
                    index ===
                    (currentIndex - 1 + images.length) % images.length,
                }"
                :data-index="index"
                role="img"
                :aria-label="`Album ảnh ${index + 1}`"
                :style="{ backgroundImage: `url(${image})` }"
              ></div>

              <!-- Next arrow -->
              <div class="gallery-view-icon-next" @click="nextSlide">
                <img
                  loading="lazy"
                  src="https://content.pancake.vn/1/d8/88/b5/1f/ce7bea1db3f2c535a89a2c99988aeba8d3a361b2c72c9d08950d10e7.svg"
                  alt="navigation"
                />
                <div class="icon-next"></div>
              </div>
              <!-- Prev arrow -->
              <div class="gallery-view-icon-prev" @click="prevSlide">
                <img
                  loading="lazy"
                  src="https://content.pancake.vn/1/31/23/51/e5/41806a12b05813bfc36f3ad3d1a580aa060a9d8f1736cc38e197a61f.svg"
                  alt="navigation"
                />
                <div class="icon-prev"></div>
              </div>
            </div>

            <!-- Thumbnail controls -->
            <div class="gallery-controls">
              <div class="gallery-scroll full-height">
                <div class="gallery-controls-wrap">
                  <div
                    v-for="(image, index) in images"
                    :key="index"
                    class="gallery-controls-item"
                    :class="{ active: index === currentIndex }"
                    :data-index="index"
                    :style="{ backgroundImage: `url(${image})` }"
                    @click="goTo(index)"
                  ></div>
                </div>
              </div>
              <div class="gallery-controls-icon-next" @click="nextSlide">
                <img
                  loading="lazy"
                  src="https://content.pancake.vn/1/d8/88/b5/1f/ce7bea1db3f2c535a89a2c99988aeba8d3a361b2c72c9d08950d10e7.svg"
                  alt="navigation"
                />
                <div class="control-next"></div>
              </div>
              <div class="gallery-controls-icon-prev" @click="prevSlide">
                <img
                  loading="lazy"
                  src="https://content.pancake.vn/1/31/23/51/e5/41806a12b05813bfc36f3ad3d1a580aa060a9d8f1736cc38e197a61f.svg"
                  alt="navigation"
                />
                <div class="control-prev"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- RSVP invitation text -->
        <div id="w-4plf6j0b" class="com-text-block p-absolute is-animation">
          <div class="text-block">
            <h1 class="text-block-css full-width">
              Hãy xác nhận sự có mặt của bạn trước để chúng mình chuẩn bị đón
              tiếp một cách chu đáo nhất. <br />Trân trọng!&nbsp;<br />
            </h1>
          </div>
        </div>

        <!-- Calendar image -->
        <div
          id="w-5x709miw"
          class="com-calendar p-absolute is-animation"
          style="
            z-index: 10;
            overflow: hidden;
            position: absolute;
            border-radius: 8px;
          "
        >
          <img
            :src="calendarImg"
            alt="Wedding Calendar"
            style="width: 100%; height: 100%; object-fit: cover; display: block"
          />
        </div>

        <!-- Decorative image near countdown -->
        <div id="w-fzfk974a" class="com-image-block p-absolute">
          <div class="full-width full-height">
            <div
              class="image-block-css p-relative full-width full-height full-mask-size mask-position"
            >
              <div
                class="image-background p-absolute"
                role="img"
                aria-label=""
              ></div>
              <div class="image-gradient-border"></div>
            </div>
          </div>
        </div>

        <!-- Countdown label removed -->

        <!-- Decorative flower -->
        <div id="w-7otz6ju6" class="com-image-block p-absolute is-animation">
          <div class="full-width full-height">
            <div
              class="image-block-css p-relative full-width full-height full-mask-size mask-position"
            >
              <div
                class="image-background p-absolute"
                role="img"
                aria-label=""
              ></div>
              <div class="image-gradient-border"></div>
            </div>
          </div>
        </div>

        <!-- RSVP Form -->
        <div id="w-npnmha4s" class="p-absolute">
          <form
            id="npnmha4s"
            class="full-width full-height"
            @submit.prevent="submitForm"
          >
            <!-- Name input -->
            <div id="w-2tm81wbn" class="p-absolute">
              <div class="input-css full-width full-height">
                <input
                  id="wi-2tm81wbn"
                  v-model="formName"
                  type="text"
                  class="full-width full-height"
                  placeholder="Tên của bạn là gì ?"
                  name="full_name"
                  aria-label="Input full_name"
                  required
                />
              </div>
            </div>

            <!-- Submit button -->
            <div
              id="w-t0wvktbp"
              class="com-button p-absolute"
              @click="submitForm"
            >
              <div class="button-css full-height full-width">
                <span class="button-loader"></span>
                <div class="button-text full-width u-select-none">
                  {{ isSubmitting ? "ĐANG GỬI..." : "GỬI LỜI CHÚC & XÁC NHẬN" }}
                </div>
              </div>
            </div>

            <!-- "Bạn là khách mời của ai?" -->
            <div id="w-idepxkfd" class="p-absolute">
              <div class="input-css full-width full-height">
                <input
                  id="wi-idepxkfd"
                  v-model="formGuest"
                  type="text"
                  class="full-width full-height"
                  placeholder="Bạn là khách mời của ai ?"
                  name="bancuadaure"
                  aria-label="Input bancuadaure"
                />
              </div>
            </div>

            <!-- Wish textarea -->
            <div id="w-zy3vjshg" class="p-absolute">
              <div class="textarea-css">
                <textarea
                  v-model="formWish"
                  class="full-width full-height"
                  :placeholder="`                                                                                                           Gửi lời chúc đến Đức Dương & Thanh Hằng nhé!`"
                  name="guiloichuc"
                ></textarea>
              </div>
            </div>

            <!-- Attendance select -->
            <div id="w-kb774q8m" class="p-absolute">
              <div class="select-css full-width full-height p-relative">
                <select
                  v-model="formAttend"
                  class="full-width full-height"
                  name="ban_se_tham_du_chu"
                  aria-label="Bạn sẽ tham dự chứ ?"
                >
                  <option selected disabled value="">
                    Bạn sẽ tham dự chứ ?
                  </option>
                  <option id="rsoiiuah" value="Có, chắc chắn tôi sẽ đến">
                    Có, chắc chắn tôi sẽ đến
                  </option>
                  <option id="urkd0rlj" value="Xin lỗi, tôi bận mất rồi">
                    Xin lỗi, tôi bận mất rồi
                  </option>
                </select>
                <div class="chevron"><span class="icon"></span></div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

  <!-- Submit Success Popup -->
  <div
    v-if="submitSuccess"
    class="com-popup popup-center"
    style="
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      z-index: 1000001;
      display: flex;
      align-items: center;
      justify-content: center;
    "
  >
    <div
      class="popup-backdrop"
      @click="submitSuccess = false"
      style="position: fixed; inset: 0; background: transparent"
    ></div>
    <div
      style="
        position: relative;
        background: #fff;
        border-radius: 12px;
        padding: 32px 24px;
        max-width: 320px;
        width: 90%;
        text-align: center;
        z-index: 1;
      "
    >
      <p
        style="
          font-size: 18px;
          font-weight: bold;
          color: #6d583d;
          font-family: &quot;Taviraj&quot;, sans-serif;
          margin-bottom: 8px;
        "
      >
        Thank you
      </p>
      <p
        style="
          font-size: 13px;
          color: #555;
          font-family: &quot;Roboto&quot;, sans-serif;
          margin-bottom: 16px;
        "
      >
        Cảm ơn bạn đã xác nhận và gửi lời chúc! Chúng mình rất mong được gặp
        bạn.
      </p>
      <button
        @click="submitSuccess = false"
        style="
          background: #6d583d;
          color: #fff;
          border: none;
          padding: 10px 24px;
          border-radius: 8px;
          cursor: pointer;
          font-size: 13px;
        "
      >
        Đóng
      </button>
    </div>
  </div>

</template>

<style scoped>
@keyframes pulse {
  0% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.6;
    transform: scale(1.02);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
.qr-zoom-container {
  aspect-ratio: 1 / 1;
  width: 100%;
  border-radius: 8px;
  border: 2px solid #e5e7eb;
  overflow: hidden;
  cursor: pointer;
  background: #fff;
  position: relative;
}
.qr-zoom-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: transform 0.2s ease;
  position: absolute;
  top: 0;
  left: 0;
}
.qr-zoom-container:hover .qr-zoom-img {
  transform: scale(1.05);
}
</style>
