<template>
<div> 
    <div style="margin-bottom: 12px">
     <router-link to="/servers">服务器列表</router-link> |
     <router-link to="/records">执行记录</router-link> |
     <router-link to="/users">用户管理</router-link> |
     <router-link to="/deploy">配置下发</router-link>
   </div>  
    <a-select v-model:value="selectedIds" mode="multiple" placeholder="选择服务器" size="large" style="width: 100%; margin-bottom: 12px">
     <a-select-option v-for="s in servers" :key="s.id" :value="s.id">
       {{ s.name }}（{{ s.ip }}）
     </a-select-option>
   </a-select>
   <a-upload :before-upload="beforeUpload" :max-count="1">
     <a-button>选择文件</a-button>
   </a-upload>
   <a-input v-model:value="remotePath" placeholder="远程路径，如 /tmp/nginx.conf"
            style="margin: 12px 0" />
    <a-button type="primary" @click="handleDeploy">开始下发</a-button>        
</div>
</template> 

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { getServers } from '../api/server'
import { deployConfig } from '../api/deploy'

const servers = ref([])
const selectedIds = ref([])
const selectedFile = ref(null)
const remotePath = ref('')

const beforeUpload = (file) => { selectedFile.value = file; return false }

const handleDeploy = async () => {
     if (!selectedIds.value.length || !selectedFile.value || !remotePath.value) {
       message.warning('请选择服务器、文件和远程路径')
       return
     }
     try {
       const res = await deployConfig(selectedFile.value, selectedIds.value, remotePath.value)
       message.success('下发完成')
     } catch (err) {
       message.error(err.response?.data?.detail || '下发失败')
     }
   }

   onMounted(async () => {
     const res = await getServers()
     servers.value = res.data
   })
</script>