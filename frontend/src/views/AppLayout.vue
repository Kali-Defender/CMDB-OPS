<template>
  <a-layout style="min-height: 100vh">
    <!-- 顶部：横跨全宽 -->
    <a-layout-header
      style="color: #fff; font-size: 18px; font-weight: 600; padding: 0 24px;
             display: flex; justify-content: space-between; align-items: center"
    >
      <span>CMDB 自动化运维平台</span>
      <a-button type="text" style="color: #fff" @click="logout">退出登录</a-button>
    </a-layout-header>

    <a-layout>
      <!-- 左侧菜单 -->
      <a-layout-sider theme="dark" width="200">
        <a-menu theme="dark" mode="inline" :selected-keys="[activeKey]" @click="onMenuClick">
          <a-menu-item key="/dashboard">首页看板</a-menu-item>
          <a-menu-item key="/servers">服务器列表</a-menu-item>
          <a-menu-item key="/records">执行记录</a-menu-item>
          <a-menu-item key="/users">用户管理</a-menu-item>
          <a-menu-item key="/deploy">配置下发</a-menu-item>
        </a-menu>
      </a-layout-sider>

      <!-- 右侧内容区 -->
      <a-layout-content style="padding: 16px">
        <router-view />
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { message } from 'ant-design-vue'

const route = useRoute()
const router = useRouter()
const activeKey = computed(() => route.path)
const onMenuClick = ({ key }) => router.push(key)

const logout = () => {
  localStorage.removeItem('token')   // 清掉登录凭证
  message.success('已退出登录')
  router.push('/login')
}
</script>
