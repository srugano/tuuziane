<template>
  <div class="auth-form">
    <form class="account-menu__form" @submit.prevent="handleLogin">
        <div class="account-menu__form-title">Log In to Your Account</div>
        <div class="form-group"><label for="header-signin-email" class="sr-only">Email
            address</label> <input id="header-signin-email" type="email" v-model="username"
                                    class="form-control form-control-sm" placeholder="Email address"></div>
        <div class="form-group"><label for="header-signin-password"
                                        class="sr-only">Password</label>
            <div class="account-menu__form-forgot"><input id="header-signin-password" v-model="password"
                                                          type="password" class="form-control form-control-sm"
                                                          placeholder="Password"> <a href=""
                                            class="account-menu__form-forgot-link">Forgot?</a></div>
        </div>
        <p v-if="error" class="error text-danger">{{ error }}</p>
        <div class="form-group account-menu__form-button"><button type="submit"
                                                                  class="btn btn-primary btn-sm">Login</button></div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      error: ''
    }
  },
  methods: {
    async handleLogin() {
      try {
        const csrfToken = document.cookie.split('; ')
          .find(row => row.startsWith('csrftoken='))
          ?.split('=')[1];

        const response = await fetch('/api/v1/osc/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken || '',
            'Authorization': 'VueTuuzianeApp'
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          }),
          credentials: 'include'
        });

        if (!response.ok) {
          throw new Error('Login failed');
        }

        const data = await response.json();
        this.$emit('login-success', data);
      } catch (err) {
        this.error = err.message;
      }
    }
  }
}
</script>
