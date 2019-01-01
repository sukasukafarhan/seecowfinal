var mongoose = require('mongoose');
var passport = require('passport');
var config = require('../config/database');
require('../config/passport')(passport);
var jwt = require('jsonwebtoken');
var Sapi = require("../models/sapi.model");
var Peternak = require("../models/peternak.model");
var Perangkat = require("../models/perangkat.model");
const axios = require('axios');
const socketApp = require('../socket/socket-app');
var ObjectId = require('mongoose').Types.ObjectId;
var sapiRepositories = require('../repositories/sapi.repositories');
var Token = require('../services/TokenAuthentication');
var Response = require('../services/Response');

module.exports = {
  get_specific_time: async(req, res)=>{
    let token = Token.authorizationToken(req.headers);
      if(token){
        let response = new Response()
        try {
          response.setData(await sapiRepositories.getSapiOnSpecificTime())
        } catch (e) {
          response.setStatus(false)
          response.setMessage(e)
        }
        res.json(response)  
      }else{
        res.json(response.unAuthorized());
      }
  },
  sapi_show_by_farmer: async(req, res)=>{
    let token = Token.authorizationToken(req.headers);
    
    if(token){
      let result_decode = jwt.verify(token, config.secret)
      let response = new Response()
        try {
          response.setData(await sapiRepositories.getSapiByFarmers(result_decode._doc._id))
        } catch (e) {
          response.setStatus(false)
          response.setMessage(e)
        }
        res.json(response) 
    }else{
      res.json(response.unAuthorized());
    }
  },
  data_update: async(req, res)=>{
    let response = new Response()
    try{
      response.setData(await sapiRepositories.streamUpdateData(req.body.suhu,req.body.jantung,req.body.status,req.params.id))
    }catch(e){
      response.setStatus(false)
      response.setMessage(e)
    }
    res.json(response) 
  },
  sapi_update: async(req,res)=>{
    let response = new Response()
    try{
      response.setData(await sapiRepositories.updateSapi(req.params.id, req.body))
    }catch(e){
      response.setStatus(false)
      response.setMessage(e)
    }
    res.json(response)
  },
  sapi_delete: async(req, res)=>{
    let response = new Response();
    try{
      response.setData(await sapiRepositories.deleteSapi(req.params.id))
    }catch(e){
      response.setStatus(false)
      response.setMessage(e)
    }
    res.json(response)
  },
  sapi_detail: async(req,res)=>{
    let token = Token.authorizationToken(req.headers);
      if(token){
        let response = new Response()
        try {
          response.setData(await sapiRepositories.detailSapi(req.params.id))
        } catch (e) {
          response.setStatus(false)
          response.setMessage(e)
        }
        res.json(response)  
      }else{
        res.json(response.unAuthorized());
      }
  },
  create: async(req,res)=>{
    let token = Token.authorizationToken(req.headers);
    
    if(token){
      let result_decode = jwt.verify(token, config.secret)
      let response = new Response()
        try {
          response.setData(await sapiRepositories.createSapi(result_decode._doc._id,req.body.namaSapi))
        } catch (e) {
          response.setStatus(false)
          response.setMessage(e)
        }
        res.json(response) 
    }else{
      res.json(response.unAuthorized());
    }
  }
}
// const io = require('socket.io')(server);

// io.on('connection', function(socket) {
//     console.log(socket.id)
//     setInterval(function(){
//         io.emit('stream', {'title': "A new title via Socket.IO!"});
//     }, 1000);

// });
//Simple version, without validation or sanitation
// exports.create = function (req, res) {
//   var token = getToken(req.headers);
//   if (token) {
//     jwt.verify(token, config.secret, function (err, decoded) {
//       if (err) return res.json({
//         success: false,
//         msg: 'Failed to authenticate token.'
//       });
//       Peternak.findOne({
//         idUser: decoded._doc._id
//       }, function (err, peternak) {
//         if (err) return res.json({
//           success: false,
//           msg: 'There was a problem finding the peternak.'
//         });
//         if (!peternak) return res.json({
//           success: false,
//           msg: 'No peternak found.'
//         });
//         /**
//          * initial first data,
//          * perangkat status
//          * 1 -> active
//          * 0 -> non-active
//          * 2 -> pending
//          * kondisi
//          * 1 -> normal
//          * 0 -> tidak normal
//          */
//         var today = new Date();
//         var initial_suhu = 38;
//         var initial_jantung = 60;
//         var initial_status = 2;
//         var initial_kondisi = 0;
//         let sub_data = {
//           tanggal: today,
//           suhu: initial_suhu,
//           jantung: initial_jantung,
//           kondisi: initial_kondisi
//         }

//         let sub_perangkat = {
//           status: initial_status,
//           data: [sub_data]
//         }
//         var newSapi = new Sapi({
//           idPeternak: peternak._id,
//           namaSapi: req.body.namaSapi,
//           perangkat: sub_perangkat

//         });
//         newSapi.save(function (err, sapi) {
//           if (err) {
//             return res.json({
//               success: false,
//               msg: 'Save sapi failed.'
//             });
//           }
//           axios.post('http://10.8.0.10:3000/raspi/perangkat/create', {
//             idPerangkatOnServer: sapi._id
//           }).then(function (response) {
//             console.log(response.data);
//             Sapi.update({
//               _id: sapi._id
//             }, {
//               $set: {
//                 "perangkat.idOnRaspi": response.data.perangkat._id
//               }
//             }, function (err) {
//               if (err) {
//                 return res.json({
//                   success: false,
//                   msg: 'Create sapi failed.'
//                 });
//               };
//               return res.json({
//                 respon: response.data
//               })
//             });
//           }).catch(function (error) {
//             console.log(error);
//             return res.json({
//               success: false,
//               msg: 'failed creating perangkat'
//             });
//           });
//         });
//       });
//     });

//   } else {
//     return res.json({
//       success: false,
//       msg: 'Unauthorized.'
//     });
//   }
// };
// exports.data_update = function (req, res) {
//   var today = new Date();
//   /**
//    * condition dairy cows healty status
//    */
//   var tmpSuhu = Number(req.body.suhu)
//   var tmpJantung = Number(req.body.jantung)
//   var tmpKondisi = 1
//   if (tmpJantung < 20 || tmpJantung > 40 || tmpSuhu < 53 || tmpSuhu > 80) {
//     tmpKondisi = 0
//   }

//   Sapi.update({
//       _id: req.params.id
//     }, {
//       $set: {
//         "perangkat.status": req.body.status
//       },
//       $push: {
//         "perangkat.data": {
//           tanggal: today,
//           suhu: req.body.suhu,
//           jantung: req.body.jantung,
//           kondisi: tmpKondisi
//         }
//       }
//     },
//     function (err, docs) {
//       if (err) return res.json({
//         success: false,
//         msg: 'updated failed'
//       });
//       Sapi.findById(req.params.id, function (err, sapi) {
//         /**
//          * create topic each cows, and emmit when update data..
//          */
//         socketApp.notifyDetailCows(req.params.id, sapi)
//         /**
//          * call function..
//          */
//         this.sapiById(sapi.idPeternak)
//       });
//       res.json({
//         success: true,
//         msg: 'updated successfully!'
//       });

//     }
//   );

// };
/**
 * Get cows by farmers, and emmit to socket.
 */
// sapiById = function (idPeternak) {
//   Sapi.find({
//     idPeternak: idPeternak
//   }, function (err, sapi_2) {
//     if (err) return next(err);
//     socketApp.notifyCowsData(idPeternak, sapi_2)
//   });
//   return true;
// };

// exports.sapi_update = function (req, res) {
//   Sapi.findByIdAndUpdate(req.params.id, {
//     $set: req.body
//   }, function (err, user) {
//     if (err) return res.json({
//       success: false,
//       msg: 'failed updated'
//     });
//     res.json({
//       success: true,
//       msg: 'Successful updated',
//       user: user
//     });
//   });
// };
// exports.sapi_delete = function (req, res) {
//   Sapi.findByIdAndRemove(req.params.id, function (err) {
//     if (err) res.json({
//       success: false,
//       msg: 'Deleted failed'
//     });
//     res.json({
//       success: true,
//       msg: 'Deleted successfully!'
//     });
//   })
// };
// exports.sapi_show_by_farmer = function (req, res) {
//   var token = getToken(req.headers);
//   if (token) {
//     jwt.verify(token, config.secret, function (err, decoded) {
//       if (err) return res.json({
//         success: false,
//         msg: 'Failed to authenticate token.'
//       });
//       Peternak.findOne({
//         idUser: decoded._doc._id
//       }, function (err, peternak) {
//         if (err) return res.json({
//           success: false,
//           msg: 'There was a problem finding the peternak.'
//         });
//         if (!peternak) return res.json({
//           success: false,
//           msg: 'No peternak found.'
//         });
//         Sapi.find({
//           idPeternak: peternak._id
//         }, function (err, sapi) {
//           if (err) return next(err);

//           res.json({
//             success: true,
//             sapi: sapi
//           });
//         });

//       });
//     });

//   } else {
//     return res.status(401).json({
//       success: false,
//       msg: 'Unauthorized.'
//     });
//   }
// };
// exports.get_specific_time = async(req,res)=>{
//   var token = getToken(req.headers);
//   if(token){
//     let anu = await SapiRepo.getSapiOnSpecificTime();
//          res.json({
//           success: true,
//           sapi: anu
//         });

//     // Sapi.aggregate(

//     //   // Pipeline
//     //   [
//     //     // Stage 1
//     //     {
//     //       $match: {
//     //           _id: new ObjectId("5c24e8ca4c7cde0016387815")
          
//     //       }
//     //     },
    
//     //     // Stage 2
//     //     {
//     //       $unwind: {
//     //           path : "$perangkat.data",
//     //           includeArrayIndex : "arrayIndex", // optional
//     //           preserveNullAndEmptyArrays : false // optional
//     //       }
//     //     },
    
//     //     // Stage 3
//     //     {
//     //       $match: {
//     //           "perangkat.data.tanggal": {
//     //               $gte: new Date(),
//     //               $lte : new Date(new Date().setDate(new Date().getDate()+1))
//     //               }
//     //       }
//     //     },
    
//     //     // Stage 4
//     //     {
//     //       $group: {
//     //           _id:{_id : "$_id",idPeternak: "$idPeternak",namaSapi: "$namaSapi",status: "$perangkat.status",idOnRaspi:"$perangkat.idOnRaspi"},
//     //           listResult : {$push: "$perangkat.data"}
              
//     //       }
//     //     },
    
//     //     // Stage 5
//     //     {
//     //       $project: {
//     //           // specifications
//     //           _id : "$_id._id",
//     //           idPeternak: "$_id.idPeternak",
//     //           namaSapi: "$_id.namaSapi",
//     //           perangkat:{
//     //             status : "$_id.status",
//     //             data: "$listResult",
//     //             idOnRaspi: "$_id.idOnRaspi"
                
//     //           }
              
//     //       }
//     //     },
    
//     //   ],function(err,result){
//     //     if (err) return res.json({
//     //       success: false,
//     //       error : err,
//     //       msg: 'There was a problem finding the peternak.'
//     //     });

//     //     res.json({
//     //       success: true,
//     //       sapi: result
//     //     });

//     //   });    
//   }else {
//     return res.status(401).json({
//       success: false,
//       msg: 'Unauthorized.'
//     });
//   }
// };
// exports.sapi_detail = function (req, res) {
//   var token = getToken(req.headers);
//   if (token) {
//     Sapi.findById(req.params.id, function (err, sapi) {
//       // if (err) return next(err);
//       if (err) return res.json({
//         success: false,
//         msg: 'There was a problem finding the cow.'
//       });
//       if (!sapi) return res.json({
//         success: false,
//         msg: 'No cow found.'
//       });
//       res.json({
//         success: true,
//         sapi: sapi
//       });
//     });
//   } else {
//     return res.status(403).send({
//       success: false,
//       msg: 'Unauthorized.'
//     });
//   }
// };
// getToken = function (headers) {
//   if (headers && headers.authorization) {
//     var parted = headers.authorization.split(' ');
//     if (parted.length === 2) {
//       return parted[1];
//     } else {
//       return null;
//     }
//   } else {
//     return null;
//   }
// };
// const postAction = function (perangkat) {
//   axios.post('http://10.8.0.10:3000/raspi/perangkat/create', {
//     idPerangkatOnServer: perangkat._id
//   }).then(function (response) {
//     console.log("uploading successfully");
//     return true;
//   }).catch(function (error) {
//     console.log(error);
//     return false;
//   });
// }
// getPerangkat = function (req, sapi) {
//   /**
//    * initial first data,
//    * perangkat status
//    * 1 -> active
//    * 0 -> non-active
//    */
//   var today = new Date();
//   var initial_suhu = 38;
//   var initial_jantung = 60;
//   var initial_status = 0;
//   let sub_data = {
//     tanggal: today,
//     suhu: initial_suhu,
//     jantung: initial_jantung
//   }
//   var newPerangkat = new Perangkat({
//     idSapi: sapi._id,
//     status: initial_status,
//     data: [sub_data]
//   });
//   newPerangkat.save(function (err, docs) {
//     if (err) {
//       return false;
//     }
//     // creating perangkat on raspi
//     axios.post('http://192.168.43.100:3000/raspi/perangkat/create', {
//       idPerangkatOnServer: docs._id
//     }).then(function (response) {
//       console.log(response);
//       return response;
//     }).catch(function (error) {
//       console.log(error);
//       return false;
//     });
//   });
// };
// getToday = function () {
//   var today = new Date();
//   var dd = today.getDate();
//   var mm = today.getMonth() + 1; //January is 0!
//   var yyyy = today.getFullYear();

//   if (dd < 10) {
//     dd = '0' + dd
//   }

//   if (mm < 10) {
//     mm = '0' + mm
//   }

//   today = mm + '-' + dd + '-' + yyyy;
//   return today;
// };
// getTimeToday = function () {
//   var d = new Date(),
//     h = (d.getHours() < 10 ? '0' : '') + d.getHours(),
//     m = (d.getMinutes() < 10 ? '0' : '') + d.getMinutes();
//   d = h + ':' + m;
//   return d;

// };