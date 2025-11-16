
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

import Home from './components/Home.vue'
import Auth from './components/Auth.vue'

const routes = [
    { path: '/', component: Home },
    { path: '/auth/google', component: Auth}
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

const app = createApp(App).use(router).mount('#app')

