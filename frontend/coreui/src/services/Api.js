/**
 * Author : farhan
 * List API baseUrl
 */
const deviceUrl = function(){
    
    return 'http://34.101.76.171:3000/api/user/'
    // return 'http://192.168.1.194:3000/api/perangkat/' 
    // return 'http://192.168.1.124:3000/api/perangkat/'
    // return 'http://10.252.175.133:3000/api/perangkat/'
}
const userUrl = function(){
     return 'http://34.101.76.171:3000/api/user/'
    //   return 'http://192.168.1.194:3000/api/user/'
    // return 'http://10.252.175.133:3000/api/user/'
    // return 'http://192.168.1.124:3000/api/user/'
}
const sapiUrl = function(){
    return 'http://34.101.76.171:3001/api/sapi/'
    //  return 'http://192.168.1.194:3001/api/sapi/'
    // return 'http://10.252.175.133:3001/api/sapi/'
    // return 'http://192.168.1.124:3001/api/sapi/'
}
const intelligentUrl = function(){
    // return 'http://192.168.1.194:4000/api/intelligent/'
    return 'http://34.101.76.171:4000/api/intelligent/'
    // return 'http://10.252.175.133:4000/api/intelligent/'
    // return 'http://192.168.1.124:4000/api/intelligent/'
}
module.exports = {
    deviceUrl,
    userUrl,
    sapiUrl,
    intelligentUrl
}
