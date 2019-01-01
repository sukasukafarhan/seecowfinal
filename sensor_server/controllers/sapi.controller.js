var mongoose = require('mongoose');
var passport = require('passport');
var config = require('../config/database');
require('../config/passport')(passport);
var jwt = require('jsonwebtoken');
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
