import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Home from "./modules/Home.vue";

console.log("Mounting Vue app to #dj-vite-home");
const homeApp = createApp(Home)

homeApp.use(createPinia())

homeApp.mount('#dj-vite-home')
