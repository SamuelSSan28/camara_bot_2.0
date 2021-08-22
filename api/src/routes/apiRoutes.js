var router = require('express').Router();
const ApiController = require('../controllers/ApiController');
const apiController = new ApiController();


router.get('/', apiController.home);
router.get('/teste', apiController.index);

module.exports = router;