<template>
  <div class="registration-app">
    <Login v-if="showLogin" @login-success="handleAuthSuccess" />
    <Register v-else @register-success="handleAuthSuccess" />

    <div class="account-menu__form-link mb-4 mt-0 pt-0" ><a @click="showLogin = !showLogin">
        {{ showLogin ? 'Create An Account' : 'Login to your account' }}
    </a></div>
  </div>
</template>

<script>
import Login from './Login.vue'
import Register from './Register.vue'

export default {
  components: {
    Login,
    Register
  },
  data() {
    return {
      showLogin: true
    }
  },
  methods: {
    handleAuthSuccess(userData) {
    //   this.$emit('auth-success', userData);
      location.reload();
    }
  }
}
</script>
