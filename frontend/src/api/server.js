import request from './request'

   export function getServers() {
     return request.get('/api/servers')
   }

export function createServer(data) {
     return request.post('/api/servers', data)
   }

export function updateServer(id, data) {
     return request.put(`/api/servers/${id}`, data)
   }

export function deleteServer(id) {
     return request.delete(`/api/servers/${id}`)
   }