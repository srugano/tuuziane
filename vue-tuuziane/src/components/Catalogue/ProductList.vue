<script setup>
import { ref, onMounted } from 'vue'

const products = ref([])
const loading = ref(true)

onMounted(async () => {
  loading.value = true
  const res = await fetch('/api/catalogue/products/')
  const data = await res.json()
  products.value = data.products
  loading.value = false
})
</script>

<template>
  <div class="products-view__list products-list products-list--grid--4" data-layout="list" data-with-features="false">
    <div class="products-list__head">
      <div class="products-list__column products-list__column--image">Image</div>
      <div class="products-list__column products-list__column--meta">SKU</div>
      <div class="products-list__column products-list__column--product">Product</div>
      <div class="products-list__column products-list__column--rating">Rating</div>
      <div class="products-list__column products-list__column--price">Price</div>
    </div>
    <div class="products-list__content">
      <div v-if="loading">Loading products...</div>
      <template v-else>
        <div v-for="product in products" :key="product.id" class="products-list__item">
          <div class="product-card">
            <!-- Actions, image, and other sections can be added here as needed -->
            <div class="product-card__info">
              <div class="product-card__meta">
                <span class="product-card__meta-title">SKU:</span> {{ product.sku || 'N/A' }}
              </div>
              <div class="product-card__name">
                <div>
                  <a href="#">{{ product.title }}</a>
                </div>
              </div>
              <!-- Add more fields as needed -->
            </div>
            <div class="product-card__footer">
              <div class="product-card__prices">
                <div class="product-card__price product-card__price--current">
                  {{ product.price ? '$' + product.price : 'N/A' }}
                </div>
              </div>
              <!-- Add to cart, wishlist, compare buttons as needed -->
            </div>
          </div>
        </div>
      </template>
    </div>
  </div>
</template> 