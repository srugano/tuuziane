import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import RegistrationApp from './components/Registration/RegistrationApp.vue'

const app = createApp(RegistrationApp)
app.use(createPinia())
app.mount('#tuuziane-vue-app')
