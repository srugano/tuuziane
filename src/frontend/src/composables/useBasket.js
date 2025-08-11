import { ref } from 'vue'

const API_BASE = '/api/v1/osc/basket/'

export function useBasket() {
  const loading = ref(true)
  const error = ref(null)
  const basketLines = ref([])
  const basketTotal = ref(0)
  const basketShipping = ref(0)
  const basketTax = ref(0)

  // Get CSRF token from cookie
  const getCookie = (name) => {
    const cookie = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')
    return cookie ? cookie.pop() : ''
  }

  const handleResponse = async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    return response.json()
  }

  const fetchBasket = async () => {
    try {
      loading.value = true
      const response = await fetch(API_BASE, {
        credentials: 'include',
        headers: {
          'Authorization': process.env.VUE_APP_DJANGO_OSCAR_API_KEY,
        }
      })
      const data = await handleResponse(response)
      basketLines.value = data.lines
      basketTotal.value = data.total
      basketShipping.value = data.shipping || 0
      basketTax.value = data.tax || 0
    } catch (err) {
      error.value = 'Failed to load basket'
    } finally {
      loading.value = false
    }
  }

  const addProduct = async (productId, quantity = 1) => {
    try {
      const response = await fetch(API_BASE + 'add-product/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
          'Authorization': process.env.VUE_APP_DJANGO_OSCAR_API_KEY,
        },
        body: JSON.stringify({
          url: `/api/v1/osc/products/${productId}/`,
          quantity
        }),
        credentials: 'include'
      })
      await handleResponse(response)
      await fetchBasket()
    } catch (err) {
      error.value = 'Failed to add product'
    }
  }

  const updateLine = async (line) => {
    try {
      const response = await fetch(`${API_BASE}${line.id}/`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
          'Authorization': process.env.VUE_APP_DJANGO_OSCAR_API_KEY
        },
        body: JSON.stringify({ quantity: line.quantity }),
        credentials: 'include'
      })
      await handleResponse(response)
      await fetchBasket()
    } catch (err) {
      error.value = 'Failed to update item'
    }
  }

  const deleteLine = async (line) => {
    try {
      const response = await fetch(`${API_BASE}${line.id}/`, {
        method: 'DELETE',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'Authorization': process.env.VUE_APP_DJANGO_OSCAR_API_KEY
        },
        credentials: 'include'
      })
      await handleResponse(response)
      await fetchBasket()
    } catch (err) {
      error.value = 'Failed to remove item'
    }
  }

  return {
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
  }
}
