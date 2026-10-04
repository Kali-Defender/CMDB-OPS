import axios from 'axios'
   // 创建 axios 实例
   const request = axios.create({
     baseURL: 'http://127.0.0.1:8000',   // 后端地址
     timeout: 10000,                      // 超时 10 秒
   })

   export default request