<template>
    <div class="container">
        <h1>Welcome</h1>
        <button class="google-btn" @click="LoginWithGoogle">
            Sign up with Google
        </button>
        <button class="signin-btn" @click="LoginToProfile">
            Sign in
        </button>
        <div v-if="message" class="message">
          {{ message }}
        </div>
        
    </div>
</template>

<script>
export default {
  methods: {
    LoginWithGoogle() {
      window.location.href = 'http://127.0.0.1:8000/auth/google/url';
    },
    LoginToProfile() {
      window.location.href = ''
    }
  }
}
</script>