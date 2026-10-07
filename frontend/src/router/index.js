import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import ServerListView from '../views/ServerListView.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/', redirect: '/login' },        // 访问根路径 → 跳到登录页
      { path: '/login', component: LoginView },
      { path: '/servers', component: ServerListView },
    ],
})

export default router