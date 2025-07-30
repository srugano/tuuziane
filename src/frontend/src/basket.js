import { createApp } from 'vue';
import { createPinia } from 'pinia';
import BasketApp from './components/Basket/BasketApp.vue';

const basketApp = createApp(BasketApp);
basketApp.use(createPinia());
basketApp.mount('#vue-basket');
