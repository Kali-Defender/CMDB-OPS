<template>
  <div class="login-container">
    <a-card class="login-card" :bordered="false">
      <div class="login-header">
        <h2>服务器资产管理与自动化运维平台</h2>
        <p>运维资产统一管理 · 自动化作业调度</p>
      </div>

      <a-form class="login-form" autocomplete="off" @submit.prevent>
        <a-form-item name="username">
          <a-input v-model:value="username" placeholder="请输入用户名" size="large"/>
        </a-form-item>

        <a-form-item name="password">
          <a-input-password v-model:value="password" placeholder="请输入密码" size="large"/>
        </a-form-item>

        <a-form-item>
          <a-button type="primary" class="login-btn" size="large" block html-type="button" @click="handleLogin">
            登录
          </a-button>
        </a-form-item>
      </a-form>
    </a-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import {message} from 'ant-design-vue'
import {login} from '../api/auth'
import { useRouter } from 'vue-router'
const username = ref('')
const password = ref('')
const loading = ref(false)
const router = useRouter()

const handleLogin = async () => {
  if (!username.value || !password.value) {
    message.error('用户名和密码不能为空')
    return
  }

  loading.value = true
  try {
    const response = await login({ username: username.value, password: password.value })
    
    localStorage.setItem('token', response.data.access_token)
    
    message.success('登录成功')
    // 在这里处理登录成功后的逻辑，例如跳转到首页
    router.push('/servers')
  } catch (error) {
    message.error('登录失败，请检查用户名和密码')
  } finally {
    loading.value = false
  }
}
</script>


<style scoped>
.login-container {
  width: 100vw;
  height: 100vh;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #121212;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  box-sizing: border-box;
  
  background-image:
    linear-gradient(rgba(24, 144, 255, 0.12) 1px, transparent 1px),
    linear-gradient(90deg, rgba(24, 144, 255, 0.12) 1px, transparent 1px);
  background-size: 30px 30px;
}

.login-card {
  width: 420px;
  padding: 32px 28px;
  background-color: #1f1f1f;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  margin: 0;
}

.login-header {
  text-align: center;
  margin-bottom: 28px;
}

.login-header h2 {
  color: #ffffff;
  margin: 0;
  font-size: 22px;
  font-weight: 600;
}

.login-header p {
  color: #b8b8b8;
  margin: 6px 0 0;
  font-size: 13px;
}

.login-form {
  width: 100%;
}

.login-btn {
  background-color: #1890ff;
  border: none;
  height: 42px;
  font-weight: 500;
}
</style>
