<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import Header from './components/utils/Header.vue'
</script>

<template>
  <header>
    <Header></Header>
  </header>

  <RouterView />
</template>
