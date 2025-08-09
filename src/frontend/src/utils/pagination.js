export const paginationProp = {
  pagination: {
    type: Object,
    required: false,
    default: null,
    validator: (value) => {
      if (value === null || value === undefined) {
        return true;
      }
      return (
        typeof value.total_items === 'number' &&
        typeof value.total_pages === 'number' &&
        typeof value.current_page === 'number' &&
        typeof value.per_page === 'number'
      );
    },
  },
};

export function calculateItemsOnCurrentPage(pagination) {
    if (!pagination) {
        return 0;
    }
    const { total_items, per_page, current_page, total_pages } = pagination;
    if (total_pages === 1) {
        return total_items;
    }
    if (current_page === total_pages) {
        const remainingItems = total_items % per_page;
        return remainingItems === 0 ? per_page : remainingItems;
    }
    return per_page;
}
