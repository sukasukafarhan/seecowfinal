var mongoose = require('mongoose');
var passport = require('passport');
var config = require('../config/database');
require('../config/passport')(passport);
var jwt = require('jsonwebtoken');
var User = require("../models/user");
var Book = require("../models/book");
var Peternak = require("../models/peternak.model");

const userRepositories = {
    peternakSignup: async(username,password,nama,alamat,telp,role)=>{
        let newUser = new User({
            username: username,
            password: password,
            role: role
        });
        let saveUser = await newUser.save()
        if(saveUser){
            let newPeternak = new Peternak({
                idUser: saveUser._id,
                nama: nama,
                alamat: alamat,
                noTelp: telp
            })
            let savePeternak = await newPeternak.save()
            if(savePeternak){
                return savePeternak
            }
        }
    },
    signin: async(username,password)=>{
        let user = await User.findOne({
            username: username
        })
        if(user){
            user.comparePassword(password,function(err,isMatch){
                if(isMatch && !err){
                    let token = jwt.sign(user,config.secret)
                    user.token = token
                    return user
                }
            })
        }
    },
    userDelete: async(id)=>{
        let result = await User.findByIdAndRemove(id)
        return result
    },
    userUpdate:async(id,body)=>{
        let result = await User.findByIdAndUpdate(id,{
            $set:body
        })
        return result
    },
    profile:async(idUser)=>{
        let result = await Peternak.findOne({
            idUser:idUser
        })
        return result
    },
    getAllPeternak: async()=>{
        let result = await Peternak.find()
        return result
    }
}
module.exports = userRepositories