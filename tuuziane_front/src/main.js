import './assets/main.css'
import '../node_modules/bootstrap/dist/css/bootstrap.css'
// import '../node_modules/@fortawesome/fontawesome-free/css/all.min.css'
import '../node_modules/boxicons/css/boxicons.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
