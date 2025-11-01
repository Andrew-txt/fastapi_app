<template>
    <div class="container">
        <h1>Welcome</h1>
        <button class="google-btn" @click="LoginWithGoogle">
            Login with google
        </button>
    </div>
</template>

<script>
export default {
  name: 'Auth',
  methods: {
    LoginWithGoogle() {
      console.log('Google login clicked')
    }
  }
}</script>
