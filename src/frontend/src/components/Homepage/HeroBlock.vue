<template>
  <div class="block-hero" :style="{ backgroundImage: `url(${backgroundImageUrl})` }">
    <div class="container">
      <div class="block-hero__content">
        <h1 class="block-hero__title">{{ title }}</h1>
        <div class="block-hero__text" v-if="text">{{ text }}</div>
        <a v-if="buttonText && buttonLink" :href="buttonLink" class="btn btn-primary btn-lg">
          {{ buttonText }}
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: String,
  text: String,
  buttonText: String,
  buttonLink: String,
  backgroundImageUrl: String,
});
</script>

<style scoped>
/* Scoped styles from the theme for a hero block */
.block-hero {
  background-size: cover;
  background-position: center;
  padding: 100px 0;
  color: #fff;
  text-align: center;
}

.block-hero__content {
  background-color: rgba(0, 0, 0, 0.5);
  display: inline-block;
  padding: 2.5rem 3rem;
  border-radius: 8px;
  max-width: 600px;
}

.block-hero__title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.block-hero__text {
  font-size: 1.125rem;
  margin-bottom: 2rem;
}
</style>
