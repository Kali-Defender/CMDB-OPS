import request from './request'                                                                                                                                                   
                                                                                                                                                                                     
   export function getRecords() {                                                                                                                                                    
     return request.get('/api/records')                                                                                                                                              
   }