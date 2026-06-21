var express = require('express');
var router = express.Router();
var controller = require('../controllers/meals.js');

/* GET meals page */
router.get('/', controller.meals);

module.exports = router;