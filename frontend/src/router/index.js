import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import ServerListView from '../views/ServerListView.vue'
import RecordListView from '../views/RecordListView.vue' 
import UserListView from '../views/UserListView.vue'
const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/', redirect: '/login' },        // 访问根路径 → 跳到登录页
      { path: '/login', component: LoginView },
      { path: '/servers', component: ServerListView },
      { path: '/records', component: RecordListView }, 
      { path: '/users', component: UserListView },      // 添加用户管理路由
      { path: '/deploy', component: DeployView },      // 添加部署路由
    ],
})

export default router