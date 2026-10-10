import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import ServerListView from '../views/ServerListView.vue'
import RecordListView from '../views/RecordListView.vue' 
import UserListView from '../views/UserListView.vue'
import DeployView from '../views/DeployView.vue'  // 导入部署视图组件
import DashboardView from '../views/DashboardView.vue'
import AppLayout from '../views/AppLayout.vue'
const router = createRouter({
    history: createWebHistory(),
    routes: [
      {
     path: '/',
     component: AppLayout,
     redirect: '/dashboard',
     children: [
       { path: 'dashboard', component: DashboardView },
       { path: 'servers', component: ServerListView },
       { path: 'records', component: RecordListView },
       { path: 'users', component: UserListView },
       { path: 'deploy', component: DeployView },
     ],
   },
   { path: '/login', component: LoginView },      // 添加部署路由
    ],
})

// 登录守卫：没 token 就踢回登录页（新版写法：直接 return，不用 next()）
router.beforeEach((to) => {
  const token = localStorage.getItem('token')
  if (to.path !== '/login' && !token) {
    return '/login'
  }
})

export default router