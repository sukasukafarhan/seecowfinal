/**
 * Author : Faruq
 * List API baseUrl
 * 10.252.175.133
 */
const deviceUrl = function(){
    // return 'http://192.168.100.47:3000/api/perangkat/' 
    // return 'http://192.168.43.108:3000/api/perangkat/'
    return 'http://10.252.175.133:3000/api/perangkat/'
}
const userUrl = function(){
    //  return 'http://192.168.100.47:3000/api/user/'
    //   return 'http://192.168.100.47:3000/api/user/'
    return 'http://10.252.175.133:3000/api/user/'
    // return 'http://192.168.43.108:3000/api/user/'
}
const sapiUrl = function(){
    // return 'http://192.168.100.47:3001/api/sapi/'
    //  return 'http://192.168.100.47:3001/api/sapi/'
    return 'http://10.252.175.133:3001/api/sapi/'
    // return 'http://192.168.43.108:3001/api/sapi/'
}
const intelligentUrl = function(){
    // return 'http://192.168.100.47:4000/api/intelligent/'
    // return 'http://192.168.100.47:4000/api/intelligent/'
    return 'http://10.252.175.133:4000/api/intelligent/'
    // return 'http://192.168.43.108:4000/api/intelligent/'
}
module.exports = {
    deviceUrl,
    userUrl,
    sapiUrl,
    intelligentUrl
}
