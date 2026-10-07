 <template>
     <a-table :columns="columns" :data-source="servers" row-key="id" />
   </template>

   <script setup>
   import { ref, onMounted } from 'vue'
   import { getServers } from '../api/server'

   const servers = ref([])
   const columns = [
     { title: '服务器名称', dataIndex: 'name' },
     { title: 'IP', dataIndex: 'ip' },
     { title: '端口', dataIndex: 'port' },
     { title: '类型', dataIndex: 'type' },
     { title: '环境', dataIndex: 'env' },
     { title: '负责人', dataIndex: 'owner' },
     { title: '状态', dataIndex: 'status' },
   ]

   onMounted(async () => {
     const res = await getServers()
     servers.value = res.data
   })
   </script>