import request from './request'

   export function getServers() {
     return request.get('/api/servers')
   }