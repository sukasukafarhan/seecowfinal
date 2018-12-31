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

const peternakRepositories = {
    getPeternakByIdUser: async(params) => {
        let result = await Peternak.findOne({
            idUser:new ObjectId(params)
        });
        if(result.length>0)
            return result;
        return false;
    }
}
module.exports = peternakRepositories