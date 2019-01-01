var mongoose = require('mongoose');
var passport = require('passport');
var config = require('../config/database');
require('../config/passport')(passport);
var jwt = require('jsonwebtoken');
var Sapi = require("../models/sapi.model");
const socketApp = require('../socket/socket-app');
var ObjectId = require('mongoose').Types.ObjectId;
var peternakRepositories = require('../repositories/peternak.repositories');
var ConnectRaspi = require('../services/ConnectRaspi');

const sapiRepositories = {
  getSapiOnSpecificTime: async(id,start,end)=>{
    let result = await Sapi.aggregate(

        // Pipeline
        [
          // Stage 1
          {
            $match: {
                _id: new ObjectId(id)
            
            }
          },
      
          // Stage 2
          {
            $unwind: {
                path : "$perangkat.data",
                includeArrayIndex : "arrayIndex", // optional
                preserveNullAndEmptyArrays : false // optional
            }
          },
      
          // Stage 3
          {
            $match: {
                "perangkat.data.tanggal": {
                    $gte: new Date("2019-01-01T14:58:21.042Z"),
                    $lte : new Date("2019-01-02T14:58:21.042Z")
                    }
            }
          },
      
          // Stage 4
          {
            $group: {
                _id:{_id : "$_id",idPeternak: "$idPeternak",namaSapi: "$namaSapi",status: "$perangkat.status",idOnRaspi:"$perangkat.idOnRaspi"},
                listResult : {$push: "$perangkat.data"}
                
            }
          },
      
          // Stage 5
          {
            $project: {
                // specifications
                _id : "$_id._id",
                idPeternak: "$_id.idPeternak",
                namaSapi: "$_id.namaSapi",
                perangkat:{
                  status : "$_id.status",
                  data: "$listResult",
                  idOnRaspi: "$_id.idOnRaspi"
                  
                }
                
            }
          }
      
        ])
        return result;
  },
  getSapiByFarmers: async(id)=>{
    let checkPeternak = await peternakRepositories.getPeternakByIdUser(id)
      if(checkPeternak){
        let result = await Sapi.find({
          idPeternak:checkPeternak._id
        })
        return result;
      }
  },
  streamUpdateData : async(suhu, jantung, status,id) => {
    var today = new Date();
    /**
     * condition dairy cows healty status
     */
    var tmpSuhu = Number(suhu)
    var tmpJantung = Number(jantung)
    var tmpKondisi = 1
    if (tmpJantung < 20 || tmpJantung > 40 || tmpSuhu < 53 || tmpSuhu > 80) {
      tmpKondisi = 0
    }
    let sapiOnUpdate =  await 
    Sapi.update({
      _id:id
    },
    {
      $set: {
        "perangkat.status": status
      },
      $push: {
        "perangkat.data": {
          tanggal: today,
          suhu: suhu,
          jantung: jantung,
          kondisi: tmpKondisi
          }
        }
      }
    )
    if(sapiOnUpdate){
      let sapiAfterUpdated = await Sapi.findById(id)
      if(sapiAfterUpdated){
        /**
         * create topic each cows, and emmit when update data..
         */
        socketApp.notifyDetailCows(id, sapiAfterUpdated)
        /**
         * get cows by farmers and emit
         */
        let emitToSocket = await Sapi.find({
          idPeternak: sapiAfterUpdated.idPeternak
        })
        if(emitToSocket){
          /**
           * emit data
           */
          socketApp.notifyCowsData(sapiAfterUpdated.idPeternak, emitToSocket)
          return sapiAfterUpdated
        }

      }
    }
  },
  updateSapi : async(id, body)=>{
    let result = await Sapi.findByIdAndUpdate(id, {
      $set: body
    })
    return result
  },
  deleteSapi: async(id)=>{
    let result = await Sapi.findByIdAndRemove(id)
    return result
  },
  detailSapi: async(id)=>{
    let result = await Sapi.findById(id)
    return result
  },
  createSapi: async(id, namaSapi)=>{
    let checkPeternak = await peternakRepositories.getPeternakByIdUser(id)
    if(checkPeternak){
      /**
         * initial first data,
         * perangkat status
         * 1 -> active
         * 0 -> non-active
         * 2 -> pending
         * kondisi
         * 1 -> normal
         * 0 -> tidak normal
         */
        var today = new Date();
        var initial_suhu = 38;
        var initial_jantung = 60;
        var initial_status = 2;
        var initial_kondisi = 0;
        let sub_data = {
          tanggal: today,
          suhu: initial_suhu,
          jantung: initial_jantung,
          kondisi: initial_kondisi
        }

        let sub_perangkat = {
          status: initial_status,
          data: [sub_data]
        }
        var newSapi = new Sapi({
          idPeternak: checkPeternak._id,
          namaSapi: namaSapi,
          perangkat: sub_perangkat

        });
        let saveSapi = await newSapi.save()
        if(saveSapi){
          let createOnRaspi = await ConnectRaspi.createInitial(saveSapi._id)
          if(createOnRaspi){
            let updateSapi = await 
            Sapi.update({
              _id: saveSapi._id
            },{
              $set: {
                "perangkat.idOnRaspi": createOnRaspi.data.perangkat._id
              }
            }
          )
          if(updateSapi){
            return createOnRaspi.data
          }
          }
        }
     
    }
  }

}

module.exports = sapiRepositories