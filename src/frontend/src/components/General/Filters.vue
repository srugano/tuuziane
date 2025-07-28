
<script setup>
import { computed, defineProps } from 'vue';

const props = defineProps({
  pagination: {
    type: Object,
    // Make it not required initially, or provide a default, if it can be null/undefined for a period.
    // If you expect it to eventually always be an object, 'required: true' is fine,
    // but the component itself needs to handle the initial null state.
    required: false, // Changed to false to allow initial null/undefined
    default: null, // Provide a default null to avoid 'undefined' issues
    validator: (value) => {
      // Allow null or undefined if not required
      if (value === null || value === undefined) {
        return true;
      }
      // Basic validation if value is an object
      return (
        typeof value.total_items === 'number' &&
        typeof value.total_pages === 'number' &&
        typeof value.current_page === 'number' &&
        typeof value.per_page === 'number'
      );
    },
  },
});

const itemsOnCurrentPage = computed(() => {
  // Add a guard clause here:
  if (!props.pagination) {
    // If pagination is null or undefined, return a sensible default or 0
    // You might also log a warning if this state is unexpected.
    console.warn("Pagination prop is null or undefined, cannot calculate items on page.");
    return 0; // Or -1, or null, depending on how you want to handle this state
  }

  // Now it's safe to destructure because we've confirmed props.pagination is not null/undefined
  const { total_items, per_page, current_page, total_pages } = props.pagination;

  // Your existing logic
  if (total_pages === 1) {
    return total_items;
  }

  if (current_page === total_pages) {
    const remainingItems = total_items % per_page;
    return remainingItems === 0 ? per_page : remainingItems;
  }

  return per_page;
});
</script>

<template>
  <div>
    <!-- Filters UI goes here -->
    <!-- product view options start -->
  <div class="products-view__options view-options view-options--offcanvas--mobile">
      <div class="view-options__body">
          <button type="button" class="view-options__filters-button filters-button">
              <span class="filters-button__icon">
                  <svg width="16" height="16">
                      <path d="M7,14v-2h9v2H7z M14,7h2v2h-2V7z M12.5,6C12.8,6,13,6.2,13,6.5v3c0,0.3-0.2,0.5-0.5,0.5h-2 C10.2,10,10,9.8,10,9.5v-3C10,6.2,10.2,6,10.5,6H12.5z M7,2h9v2H7V2z M5.5,5h-2C3.2,5,3,4.8,3,4.5v-3C3,1.2,3.2,1,3.5,1h2 C5.8,1,6,1.2,6,1.5v3C6,4.8,5.8,5,5.5,5z M0,2h2v2H0V2z M9,9H0V7h9V9z M2,14H0v-2h2V14z M3.5,11h2C5.8,11,6,11.2,6,11.5v3 C6,14.8,5.8,15,5.5,15h-2C3.2,15,3,14.8,3,14.5v-3C3,11.2,3.2,11,3.5,11z" />
                  </svg>
              </span>
              <span class="filters-button__title">Filters</span> <span class="filters-button__counter">3</span>
          </button>
          <div class="view-options__layout layout-switcher">
              <div class="layout-switcher__list">
                  <button type="button"
                          class="layout-switcher__button"
                          data-layout="grid"
                          data-with-features="false">
                      <svg width="16" height="16">
                          <path d="M15.2,16H9.8C9.4,16,9,15.6,9,15.2V9.8C9,9.4,9.4,9,9.8,9h5.4C15.6,9,16,9.4,16,9.8v5.4C16,15.6,15.6,16,15.2,16z M15.2,7 H9.8C9.4,7,9,6.6,9,6.2V0.8C9,0.4,9.4,0,9.8,0h5.4C15.6,0,16,0.4,16,0.8v5.4C16,6.6,15.6,7,15.2,7z M6.2,16H0.8 C0.4,16,0,15.6,0,15.2V9.8C0,9.4,0.4,9,0.8,9h5.4C6.6,9,7,9.4,7,9.8v5.4C7,15.6,6.6,16,6.2,16z M6.2,7H0.8C0.4,7,0,6.6,0,6.2V0.8 C0,0.4,0.4,0,0.8,0h5.4C6.6,0,7,0.4,7,0.8v5.4C7,6.6,6.6,7,6.2,7z" />
                      </svg>
                  </button>
                  <button type="button"
                          class="layout-switcher__button"
                          data-layout="grid"
                          data-with-features="true">
                      <svg width="16" height="16">
                          <path d="M16,0.8v14.4c0,0.4-0.4,0.8-0.8,0.8H9.8C9.4,16,9,15.6,9,15.2V0.8C9,0.4,9.4,0,9.8,0l5.4,0C15.6,0,16,0.4,16,0.8z M7,0.8 v14.4C7,15.6,6.6,16,6.2,16H0.8C0.4,16,0,15.6,0,15.2L0,0.8C0,0.4,0.4,0,0.8,0l5.4,0C6.6,0,7,0.4,7,0.8z" />
                      </svg>
                  </button>
                  <button type="button"
                          class="layout-switcher__button layout-switcher__button--active"
                          data-layout="list"
                          data-with-features="false">
                      <svg width="16" height="16">
                          <path d="M15.2,16H0.8C0.4,16,0,15.6,0,15.2V9.8C0,9.4,0.4,9,0.8,9h14.4C15.6,9,16,9.4,16,9.8v5.4C16,15.6,15.6,16,15.2,16z M15.2,7 H0.8C0.4,7,0,6.6,0,6.2V0.8C0,0.4,0.4,0,0.8,0h14.4C15.6,0,16,0.4,16,0.8v5.4C16,6.6,15.6,7,15.2,7z" />
                      </svg>
                  </button>
                  <button type="button"
                          class="layout-switcher__button"
                          data-layout="table"
                          data-with-features="false">
                      <svg width="16" height="16">
                          <path d="M15.2,16H0.8C0.4,16,0,15.6,0,15.2v-2.4C0,12.4,0.4,12,0.8,12h14.4c0.4,0,0.8,0.4,0.8,0.8v2.4C16,15.6,15.6,16,15.2,16z M15.2,10H0.8C0.4,10,0,9.6,0,9.2V6.8C0,6.4,0.4,6,0.8,6h14.4C15.6,6,16,6.4,16,6.8v2.4C16,9.6,15.6,10,15.2,10z M15.2,4H0.8 C0.4,4,0,3.6,0,3.2V0.8C0,0.4,0.4,0,0.8,0h14.4C15.6,0,16,0.4,16,0.8v2.4C16,3.6,15.6,4,15.2,4z" />
                      </svg>
                  </button>
              </div>
          </div>
          <div class="view-options__legend">Showing {{ itemsOnCurrentPage }} of {{ pagination?.total_items }} products</div>
          <div class="view-options__spring"></div>
          <div class="view-options__select">
              <label for="view-option-sort">Sort:</label>
              <select id="view-option-sort" class="form-control form-control-sm" name="">
                  <option value="">Price</option>
              </select>
          </div>
          <div class="view-options__select">
              <label for="view-option-limit">Show:</label>
              <select id="view-option-limit" class="form-control form-control-sm" name="">
                  <option :value="pagination?.per_page">{{ pagination?.per_page }}</option>
              </select>
          </div>
      </div>
      <div class="view-options__body view-options__body--filters">
          <div class="view-options__label">Active Filters</div>
          <div class="applied-filters">
              <ul class="applied-filters__list">
                  <li class="applied-filters__item">
                      <a href=""
                        class="applied-filters__button applied-filters__button--filter">Sales: Top Sellers
                          <svg width="9" height="9">
                              <path d="M9,8.5L8.5,9l-4-4l-4,4L0,8.5l4-4l-4-4L0.5,0l4,4l4-4L9,0.5l-4,4L9,8.5z" />
                          </svg>
                      </a>
                  </li>
                  <li class="applied-filters__item">
                      <a href=""
                        class="applied-filters__button applied-filters__button--filter">Color: True Red
                          <svg width="9" height="9">
                              <path d="M9,8.5L8.5,9l-4-4l-4,4L0,8.5l4-4l-4-4L0.5,0l4,4l4-4L9,0.5l-4,4L9,8.5z" />
                          </svg>
                      </a>
                  </li>
                  <li class="applied-filters__item">
                      <button type="button"
                              class="applied-filters__button applied-filters__button--clear">Clear All</button>
                  </li>
              </ul>
          </div>
      </div>
  </div>
  <!-- product view options end -->
  </div>
</template>
