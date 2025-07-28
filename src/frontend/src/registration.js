import { createApp } from 'vue';
import { createPinia } from 'pinia';
import CatalogueApp from './components/Registration/RegistrationApp.vue';

const app = createApp(CatalogueApp);
app.use(createPinia());
app.mount('#vue-registration');
