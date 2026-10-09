import request from './request'

   export function getUsers() {
     return request.get('/api/users')
   }

   export function createUser(data) {
     return request.post('/api/users', data)
   }

   export function deleteUser(id) {
     return request.delete(`/api/users/${id}`)
   }