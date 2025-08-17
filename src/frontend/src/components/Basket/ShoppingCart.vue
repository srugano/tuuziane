<template>
    <div class="indicator indicator--trigger--click"><a href="cart.html" class="indicator__button"><span
        class="indicator__icon"><svg width="32" height="32">
            <circle cx="10.5" cy="27.5" r="2.5" />
            <circle cx="23.5" cy="27.5" r="2.5" />
            <path d="M26.4,21H11.2C10,21,9,20.2,8.8,19.1L5.4,4.8C5.3,4.3,4.9,4,4.4,4H1C0.4,4,0,3.6,0,3s0.4-1,1-1h3.4C5.8,2,7,3,7.3,4.3
                        l3.4,14.3c0.1,0.2,0.3,0.4,0.5,0.4h15.2c0.2,0,0.4-0.1,0.5-0.4l3.1-10c0.1-0.2,0-0.4-0.1-0.4C29.8,8.1,29.7,8,29.5,8H14
                        c-0.6,0-1-0.4-1-1s0.4-1,1-1h15.5c0.8,0,1.5,0.4,2,1c0.5,0.6,0.6,1.5,0.4,2.2l-3.1,10C28.5,20.3,27.5,21,26.4,21z" />
        </svg> <span class="indicator__counter">{{ totalItems }}</span> </span><span
            class="indicator__title">Shopping Cart</span> <span
                class="indicator__value">${{ basketTotal.toFixed(2) }}</span></a>
        <div class="indicator__content">
            <div class="dropcart">
                <ul class="dropcart__list">
                    <template v-for="(line, index) in basketLines" :key="line.id">
                        <li class="dropcart__item">
                            <div class="dropcart__item-image image image--type--product">
                                <a class="image__body" href="product-full.html">
                                    <img class="image__tag" :src="line.product.image" :alt="line.product.title">
                                </a>
                            </div>
                            <div class="dropcart__item-info">
                                <div class="dropcart__item-name">
                                    <a href="product-full.html">{{ line.product.title }}</a>
                                </div>
                                <div class="dropcart__item-meta">
                                    <div class="dropcart__item-quantity">{{ line.quantity }}</div>
                                    <div class="dropcart__item-price">${{ line.price_excl_tax }}</div>
                                </div>
                            </div>
                            <button type="button" class="dropcart__item-remove" @click="deleteLine(line)">
                                <svg width="10" height="10">
                                    <path d="M8.8,8.8L8.8,8.8c-0.4,0.4-1,0.4-1.4,0L5,6.4L2.6,8.8c-0.4,0.4-1,0.4-1.4,0l0,0c-0.4-0.4-0.4-1,0-1.4L3.6,5L1.2,2.6
                                            c-0.4-0.4-0.4-1,0-1.4l0,0c0.4-0.4,1-0.4,1.4,0L5,3.6l2.4-2.4c0.4-0.4,1-0.4,1.4,0l0,0c0.4,0.4,0.4,1,0,1.4L6.4,5l2.4,2.4
                                            C9.2,7.8,9.2,8.4,8.8,8.8z" />
                                </svg>
                            </button>
                        </li>
                        <li v-if="index < basketLines.length - 1" class="dropcart__divider" role="presentation"></li>
                    </template>
                </ul>
                <div class="dropcart__totals">
                    <table>
                        <tbody>
                            <tr>
                                <th>Subtotal</th>
                                <td>${{ basketTotal.toFixed(2) }}</td>
                            </tr>
                            <tr>
                                <th>Shipping</th>
                                <td>${{ basketShipping.toFixed(2) }}</td>
                            </tr>
                            <tr>
                                <th>Tax</th>
                                <td>${{ basketTax.toFixed(2) }}</td>
                            </tr>
                            <tr>
                                <th>Total</th>
                                <td>${{ basketTotal.toFixed(2) }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="dropcart__actions"><a disabled class="btn btn-secondary">View
                    Cart</a> <a disabled class="btn btn-primary">Checkout</a></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useBasket } from '../../composables/useBasket'

const {
  loading,
  error,
  basketLines,
  basketTotal,
  basketShipping,
  basketTax,
  fetchBasket,
  addProduct,
  updateLine,
  deleteLine
} = useBasket()


const totalItems = computed(() => basketLines.value.reduce((sum, item) => sum + item.quantity, 0))

// Test method - replace with actual product ID
const addSampleProduct = () => {
  addProduct(1) // Replace with actual product ID from your API
}

onMounted(async () => {
  await fetchBasket()
})
</script>
