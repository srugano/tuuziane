import { createApp } from 'vue';
import { createPinia } from 'pinia';
import RegistrationApp from './components/Registration/RegistrationApp.vue';

const registrationApp = createApp(RegistrationApp);
registrationApp.use(createPinia());
registrationApp.mount('#vue-registration');
