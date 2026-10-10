<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'
import { getStats } from '../api/stats'

   const stats = ref({ server_total: 0, server_online: 0, record_total: 0, user_total: 0 })
   const chartRef = ref(null)   // 对应 template 里的 ref="chartRef"

   onMounted(async () => {
     // 1. 拉数据
     const res = await getStats()
     stats.value = res.data

     // 2. 画图（等 DOM 就绪后）
     const chart = echarts.init(chartRef.value)
     chart.setOption({
       title: { text: '服务器状态分布' },
       series: [{
         type: 'pie',
         data: [
           { value: stats.value.server_online, name: '在线' },
           { value: stats.value.server_total - stats.value.server_online, name: '离线/其他' },
         ],
       }],
     })
   })
</script>

<template>
     <div>
       <!-- ① 4 个统计卡片 -->
       <a-row :gutter="16">
         <a-col :span="6"><a-card>服务器总数：{{ stats.server_total }}</a-card></a-col>
         <a-col :span="6"><a-card>在线服务器：{{ stats.server_online }}</a-card></a-col>
         <a-col :span="6"><a-card>执行记录：{{ stats.record_total }}</a-card></a-col>
         <a-col :span="6"><a-card>用户数：{{ stats.user_total }}</a-card></a-col>
       </a-row>

       <!-- ② 图表容器（关键：给个 ref，让 JS 能找到它） -->
       <div ref="chartRef" style="width: 100%; height: 360px; margin-top: 16px"></div>
     </div>
   </template>