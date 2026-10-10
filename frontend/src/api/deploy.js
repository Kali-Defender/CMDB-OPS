import request from './request'

   export function deployConfig(file, serverIds, remotePath) {
     const fd = new FormData()
     fd.append('file', file)
     fd.append('server_ids', serverIds.join(','))   // 数组转成 "1,2,3"
     fd.append('remote_path', remotePath)
     return request.post('/api/deploy', fd)
   }