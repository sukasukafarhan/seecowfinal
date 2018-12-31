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
var peternakRepositories = require('../repositories/peternak.repositories');

const sapiRepositories = {
  getSapiOnSpecificTime: async()=>{
    let result = await Sapi.aggregate(

        // Pipeline
        [
          // Stage 1
          {
            $match: {
                _id: new ObjectId("5c24e8ca4c7cde0016387815")
            
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
                    $gte: new Date(),
                    $lte : new Date(new Date().setDate(new Date().getDate()+1))
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
          },
      
        ])
        return result;
  },
  getSapiByFarmers: async(token)=>{
   
        var checkPeternak = await peternakRepositories.getPeternakByIdUser(token)
        if(checkPeternak != false){
            var result = await Sapi.find({
                idPeternak:checkPeternak._id
            })
            return result;
        }
     
  },

}

module.exports = sapiRepositories