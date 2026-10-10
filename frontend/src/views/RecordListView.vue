<template>
     <div>                                                                                                                                                                             
     <router-link to="/servers">服务器列表</router-link> |                                                                                                                           
     <router-link to="/records">执行记录</router-link> |
      <router-link to="/users">用户管理</router-link>
      <router-link to="/deploy">部署</router-link>                                                                                                                               
   </div>                                                                                                                                                                         
     <div>                                                                                                                                                                           
       <h2>执行记录</h2>                                                                                                                                                             
       <a-table :columns="columns" :data-source="records" row-key="id" />                                                                                                            
     </div>                                                                                                                                                                          
   </template>                                                                                                                                                                       
                                                                                                                                                                                     
   <script setup>                                                                                                                                                                    
   import { ref, onMounted } from 'vue'                                                                                                                                              
   import { getRecords } from '../api/record'                                                                                                                                        
                                                                                                                                                                                     
   const records = ref([])                                                                                                                                                           
   const columns = [                                                                                                                                                                 
     { title: '执行人', dataIndex: 'executor' },                                                                                                                                     
     { title: '服务器', dataIndex: 'servers' },                                                                                                                                      
     { title: '命令', dataIndex: 'command' },                                                                                                                                        
     { title: '结果', dataIndex: 'result' },                                                                                                                                         
     { title: '状态', dataIndex: 'status' },                                                                                                                                         
     { title: '执行时间', dataIndex: 'executed_at' },                                                                                                                                
   ]                                                                                                                                                                                 
                                                                                                                                                                                     
   onMounted(async () => {                                                                                                                                                           
     const res = await getRecords()                                                                                                                                                  
     records.value = res.data                                                                                                                                                        
   })                                                                                                                                                                                
   </script>