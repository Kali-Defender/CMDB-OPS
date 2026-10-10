<template>
  <!-- 外层容器 -->
  <div
    style="
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      background-color: #121212;
      background-image:
        linear-gradient(rgba(24, 144, 255, 0.12) 1px, transparent 1px),
        linear-gradient(90deg, rgba(24, 144, 255, 0.12) 1px, transparent 1px);
      background-size: 30px 30px;
      background-repeat: repeat;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: center;
    "
  >
    <!-- 卡片容器 -->
    <div
      style="
        width: 100%;
        min-height: calc(100vh - 130px);
        padding: 24px 28px;
        background: #1f1f1f;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
      "
    >
      
      <h2 style="color:#fff;margin:8px 0 16px 0;">执行记录</h2>
      <a-table
        :columns="columns"
        :data-source="records"
        row-key="id"
        :pagination="{ pageSize: 12, showSizeChanger: false }"
      />
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { getRecords } from '../api/record'

const records = ref([])
const columns = [
  { title: '执行人', dataIndex: 'executor' },
  { title: '服务器', dataIndex: 'servers' },
  { title: '命令', dataIndex: 'command' },
  { title: '结果', dataIndex: 'result' },
  { title: '状态', dataIndex: 'status' },
  { title: '执行时间', dataIndex: 'executed_at' },
]

onMounted(async () => {
  const res = await getRecords()
  records.value = res.data
})
</script>
