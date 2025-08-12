<template>
  <div class="account-menu__form">
    <form @submit.prevent="handleRegister">
        <div class="account-menu__form-title">Create New Account</div>
        <div class="form-group">
            <label for="header-register-email" class="sr-only">Email address</label>
            <input id="header-register-email" type="email" v-model="email"
                    class="form-control form-control-sm" placeholder="Email address" required>
        </div>
        <div class="form-group">
            <label for="header-register-password" class="sr-only">Password</label>
            <div class="account-menu__form-forgot">
                <input id="header-register-password" v-model="password1"
                        type="password" class="form-control form-control-sm"
                        placeholder="Password" required>
            </div>
        </div>
        <div class="form-group">
            <label for="header-register-confirm" class="sr-only">Confirm Password</label>
            <div class="account-menu__form-forgot">
                <input id="header-register-confirm" v-model="password2"
                        type="password" class="form-control form-control-sm"
                        placeholder="Confirm Password" required>
            </div>
        </div>
        <p v-if="error" class="error text-danger">{{ error }}</p>
        <div class="form-group account-menu__form-button">
            <button type="submit" class="btn btn-primary btn-sm">Register</button>
        </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password1: '',
      password2: '',
      error: ''
    }
  },
  methods: {
    async handleRegister() {
      if (this.password1 !== this.password2) {
        this.error = 'Passwords do not match';
        return;
      }

      try {
        const csrfToken = document.cookie.split('; ')
          .find(row => row.startsWith('csrftoken='))
          ?.split('=')[1];



        const response = await fetch('/api/v1/osc/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken || '',
            'Authorization': process.env.VUE_APP_DJANGO_OSCAR_API_KEY
          },
          body: JSON.stringify({
            email: this.email,
            password1: this.password1,
            password2: this.password2
          }),
          credentials: 'include'
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message || 'Registration failed');
        }

        const data = await response.json();
        this.$emit('register-success', data);
      } catch (err) {
        this.error = err.message;
      }
    }
  }
}
</script>
