import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import ServerListView from '../views/ServerListView.vue'
import RecordListView from '../views/RecordListView.vue' 
const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/', redirect: '/login' },        // 访问根路径 → 跳到登录页
      { path: '/login', component: LoginView },
      { path: '/servers', component: ServerListView },
      { path: '/records', component: RecordListView },  // 添加记录列表路由
    ],
})

export default router