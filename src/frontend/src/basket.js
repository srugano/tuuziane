import { createApp } from 'vue';
import { createPinia } from 'pinia';
import BasketApp from './components/Basket/BasketApp.vue';

const app = createApp(BasketApp);
app.use(createPinia());
app.mount('#vue-basket');
