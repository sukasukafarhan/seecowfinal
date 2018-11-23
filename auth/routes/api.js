var passport = require('passport');
require('../config/passport')(passport);
var jwt = require('jsonwebtoken');
var express = require('express');
var router = express.Router();
const user_controller = require('../controllers/user.controller');
var VerifyToken = require('../config/VerifyToken');

router.post('/ptsignup', user_controller.peternak_signup);
router.post('/signin', user_controller.signin);
router.get('/me',VerifyToken, user_controller.me);
router.get('/logout',user_controller.logout);
router.delete('/:id/delete',passport.authenticate('jwt', { session: false}), user_controller.user_delete);
router.put('/:id/update',passport.authenticate('jwt', { session: false}),user_controller.user_update);
// router.post('/book', passport.authenticate('jwt', { session: false}),user_controller.book_post);
// router.get('/book', passport.authenticate('jwt', { session: false}), user_controller.book_get);

module.exports = router;
