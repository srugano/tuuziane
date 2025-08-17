<script setup>
import { ref, watchEffect } from 'vue';

// 1. Define Props
const props = defineProps({
  url: {
    type: String,
    required: true, // Keep as required if it's always provided
    // validator: (value) => value && value.startsWith('http'), // Optional: add more robust URL validation
  },
});

// 2. Define Reactive States
const priceData = ref(null); // To store the fetched data
const loading = ref(false);  // To indicate loading status
const error = ref(null);     // To store any error messages

// 3. Create the Asynchronous Fetching Function
const fetchPriceData = async (urlToFetch) => {
  // Reset states before starting a new fetch
  priceData.value = null;
  error.value = null;
  loading.value = true;

  // Basic validation for the URL
  if (!urlToFetch) {
    error.value = "No URL provided for fetching price data.";
    loading.value = false;
    return;
  }

  try {
    const res = await fetch(urlToFetch, {
      method: "GET",
      headers: { 'Authorization': window.VUE_VARS.OSCAR_API_KEY }
    });

    if (!res.ok) {
      // Handle HTTP errors (e.g., 404, 500)
      const errorText = await res.text(); // Get response body for more detail
      throw new Error(`HTTP error! Status: ${res.status} - ${errorText}`);
    }

    const data = await res.json();
    priceData.value = data; // Update the reactive ref with the fetched data

  } catch (err) {
    error.value = err.message || "An unknown error occurred during fetch.";
  } finally {
    loading.value = false; // Always set loading to false when done
  }
};

// 4. Use watchEffect to trigger the fetch when the 'url' prop changes
watchEffect(() => {
  // watchEffect will run immediately when the component mounts
  // and automatically re-run whenever props.url changes.
  fetchPriceData(props.url);
});
</script>

<template>
  <div class="price-display">
    <div v-if="loading">
      <p>Loading ...</p>
    </div>

    <div v-else-if="error">
      <p class="error-message">Error fetching data: {{ error }}</p>
      <p>Please check the URL or your network connection.</p>
    </div>

    <div v-else-if="priceData">

      <p v-if="priceData.tax !== undefined"><span v-if="priceData.currency">{{ priceData.currency }}</span>{{ priceData.tax }}</p>
      <p v-else>Tax data not available.</p>
    </div>

    <div v-else>
      <p>No price data available.</p>
    </div>
  </div>
</template>
