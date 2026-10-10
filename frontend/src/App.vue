<template>
  <!-- 全局暗色主题：所有 Ant Design 组件（表格/弹窗/输入框）自动变暗 -->
  <a-config-provider :theme="{ algorithm: theme.darkAlgorithm }">
    <router-view />
  </a-config-provider>
</template>

<script setup>
import { theme } from 'ant-design-vue'
</script>
