<template>
     <div>
       <!-- 导航（3 个链接）-->
       <div style="margin-bottom: 12px">
         <router-link to="/servers">服务器列表</router-link> |
         <router-link to="/records">执行记录</router-link> |
         <router-link to="/users">用户管理</router-link>
       </div>

       <a-button type="primary" @click="openCreate" style="margin-bottom: 16px">新增用户</a-button>

       <a-table :columns="columns" :data-source="users" row-key="id">
         <template #bodyCell="{ column, record }">
           <template v-if="column.key === 'action'">
             <a-button type="link" size="small" danger @click="handleDelete(record)">删除</a-button>
           </template>
         </template>
       </a-table>

       <a-modal v-model:open="modalOpen" title="新增用户" @ok="handleSubmit">
         <a-form layout="vertical">
           <a-form-item label="用户名"><a-input v-model:value="form.username" /></a-form-item>
           <a-form-item label="密码"><a-input-password v-model:value="form.password" /></a-form-item>
           <a-form-item label="姓名"><a-input v-model:value="form.name" /></a-form-item>
           <a-form-item label="角色">
             <a-select v-model:value="form.role">
               <a-select-option value="管理员">管理员</a-select-option>
               <a-select-option value="普通运维">普通运维</a-select-option>
             </a-select>
           </a-form-item>
         </a-form>
       </a-modal>
     </div>
   </template>

   <script setup>
   import { ref, onMounted } from 'vue'
   import { message } from 'ant-design-vue'
   import { getUsers, createUser, deleteUser } from '../api/user'

   const users = ref([])
   const modalOpen = ref(false)
   const form = ref({ username: '', password: '', name: '', role: '普通运维' })

   const columns = [
     { title: '用户名', dataIndex: 'username' },
     { title: '姓名', dataIndex: 'name' },
     { title: '角色', dataIndex: 'role' },
     { title: '状态', dataIndex: 'status' },
     { title: '操作', key: 'action' },
   ]

   const fetchUsers = async () => {
     const res = await getUsers()
     users.value = res.data
   }

   const openCreate = () => {
     form.value = { username: '', password: '', name: '', role: '普通运维' }
     modalOpen.value = true
   }

   const handleSubmit = async () => {
     if (!form.value.username || !form.value.password) {
       message.warning('请填写用户名和密码')
       return
     }
     try {
       await createUser(form.value)
       message.success('新增成功')
       modalOpen.value = false
       fetchUsers()
     } catch (err) {
       message.error(err.response?.data?.detail || '新增失败')
     }
   }

   const handleDelete = async (record) => {
     try {
       await deleteUser(record.id)
       message.success('删除成功')
       fetchUsers()
     } catch (err) {
       message.error(err.response?.data?.detail || '删除失败')
     }
   }

   onMounted(fetchUsers)
   </script>