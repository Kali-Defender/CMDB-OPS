import axios from 'axios'
   // 创建 axios 实例
   const request = axios.create({
     baseURL: 'http://127.0.0.1:8000',   // 后端地址
     timeout: 10000,                      // 超时 10 秒
   })
// 请求拦截器：自动带 token
   request.interceptors.request.use(config => {
     const token = localStorage.getItem('token')
     if (token) {
       config.headers.Authorization = `Bearer ${token}`
     }
     return config
   })
   export default request