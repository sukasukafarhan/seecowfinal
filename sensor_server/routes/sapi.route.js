var passport = require('passport');
require('../config/passport')(passport);
var jwt = require('jsonwebtoken');
var express = require('express');
var router = express.Router();
const sapi_controller = require('../controllers/sapi.controller');

router.post('/create',passport.authenticate('jwt', { session: false}), sapi_controller.create);
router.delete('/:id/delete',passport.authenticate('jwt', { session: false}), sapi_controller.sapi_delete);
router.put('/:id/update',passport.authenticate('jwt', { session: false}),sapi_controller.sapi_update);
router.get('/showsapi',passport.authenticate('jwt', { session: false}),sapi_controller.sapi_show_by_farmer);
router.get('/:id/sapidetail',passport.authenticate('jwt', { session: false}),sapi_controller.sapi_detail);
router.put('/:id/updatedata',sapi_controller.data_update);
router.post('/dataToday',passport.authenticate('jwt', { session: false}), sapi_controller.getDataToday);
module.exports = router;
