<template>
  <div>
    <a-button type="primary" @click="openCreate" style="margin-bottom: 16px">
      新增服务器
    </a-button>

    <a-table :columns="columns" :data-source="servers" row-key="id">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'action'">
          <a-button type="link" size="small" @click="openEdit(record)">编辑</a-button>
          <a-button type="link" size="small" danger @click="handleDelete(record)">删除</a-button>
        </template>
      </template>
    </a-table>

    <a-modal v-model:open="modalOpen" :title="editingId ? '编辑服务器' : '新增服务器'" @ok="handleSubmit">
      <a-form layout="vertical">
        <a-form-item label="服务器名称"><a-input v-model:value="form.name" /></a-form-item>
        <a-form-item label="IP 地址"><a-input v-model:value="form.ip" /></a-form-item>
        <a-form-item label="端口"><a-input-number v-model:value="form.port" /></a-form-item>
        <a-form-item label="登录账号"><a-input v-model:value="form.username" /></a-form-item>
        <a-form-item label="密码"><a-input-password v-model:value="form.password" placeholder="编辑时留空表示不改密码" /></a-form-item>
        <a-form-item label="类型"><a-input v-model:value="form.type" /></a-form-item>
        <a-form-item label="环境"><a-input v-model:value="form.env" /></a-form-item>
        <a-form-item label="负责人"><a-input v-model:value="form.owner" /></a-form-item>
        <a-form-item label="状态"><a-input v-model:value="form.status" /></a-form-item>
        <a-form-item label="备注"><a-input v-model:value="form.remark" /></a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import { getServers, createServer, updateServer, deleteServer } from '../api/server'

const servers = ref([])
const modalOpen = ref(false)
const editingId = ref(null)   // null = 新增，有值 = 编辑

const form = ref({
  name: '', ip: '', port: 22, username: '', password: '',
  type: '', env: '', owner: '', status: '在线', remark: '',
})

const columns = [
  { title: '服务器名称', dataIndex: 'name' },
  { title: 'IP', dataIndex: 'ip' },
  { title: '端口', dataIndex: 'port' },
  { title: '类型', dataIndex: 'type' },
  { title: '环境', dataIndex: 'env' },
  { title: '负责人', dataIndex: 'owner' },
  { title: '状态', dataIndex: 'status' },
  { title: '操作', key: 'action' },
]

const fetchServers = async () => {
  const res = await getServers()
  servers.value = res.data
}

const resetForm = () => {
  form.value = {
    name: '', ip: '', port: 22, username: '', password: '',
    type: '', env: '', owner: '', status: '在线', remark: '',
  }
}

const openCreate = () => {
  editingId.value = null
  resetForm()
  modalOpen.value = true
}

const openEdit = (record) => {
  editingId.value = record.id
  form.value = { ...record, password: '' }   // 填整行数据，密码清空（留空=不改）
  modalOpen.value = true
}

const handleSubmit = async () => {
  if (!form.value.name || !form.value.ip || !form.value.username) {
    message.warning('请填写服务器名称、IP 地址和登录账号')
    return
  }
  if (!editingId.value && !form.value.password) {
    message.warning('请填写密码')
    return
  }
  try {
    if (editingId.value) {
      await updateServer(editingId.value, form.value)
      message.success('修改成功')
    } else {
      await createServer(form.value)
      message.success('新增成功')
    }
    modalOpen.value = false
    fetchServers()
  } catch (err) {
    message.error(err.response?.data?.detail || '操作失败')
  }
}

const handleDelete = async (record) => {
  try {
    await deleteServer(record.id)
    message.success('删除成功')
    fetchServers()
  } catch (err) {
    message.error(err.response?.data?.detail || '删除失败')
  }
}

onMounted(fetchServers)
</script>
