import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '127.0.0.1',   // 显式绑 IPv4，避免 localhost 解析到 IPv6 连不上
    port: 5173,
  },
})
