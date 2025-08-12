import { createApp } from 'vue';
import { createPinia } from 'pinia';
import CatalogueApp from './components/Catalogue/CatalogueApp.vue';

const catalogueApp = createApp(CatalogueApp);
catalogueApp.use(createPinia());
catalogueApp.mount('#vue-catalogue');
