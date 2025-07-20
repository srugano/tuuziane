import { createApp } from 'vue';
import { createPinia } from 'pinia';
import CatalogueApp from './components/Catalogue/CatalogueApp.vue';

const app = createApp(CatalogueApp);
app.use(createPinia());
app.mount('#vue-catalogue');
