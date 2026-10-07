import { createApp } from 'vue'
import Antd from 'ant-design-vue'
//导入组件
import 'ant-design-vue/dist/reset.css'
//导入样式
import './style.css'
import App from './App.vue'
import router from './router'
const app = createApp(App)
app.use(Antd)
app.use(router)
//全局注册
app.mount('#app')