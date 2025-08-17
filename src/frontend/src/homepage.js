import { createApp } from 'vue';
import HeroBlock from './components/Homepage/HeroBlock.vue';

const componentRegistry = {
  'vue-hero-block': HeroBlock,
  // 'vue-featured-products': FeaturedProductsBlock, // We'll add this later
};

document.addEventListener('DOMContentLoaded', () => {
  for (const componentName in componentRegistry) {
    // Find all potential mount points for this component
    const elements = document.querySelectorAll(`[id^="${componentName}-"]`);

    elements.forEach(el => {
      const dataScript = document.getElementById(`${el.id}-data`);
      const props = dataScript ? JSON.parse(dataScript.textContent) : {};

      const app = createApp(componentRegistry[componentName], props);
      app.mount(el);
    });
  }
});
