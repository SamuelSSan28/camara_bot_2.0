var router = require('express').Router();
const ApiController = require('../controllers/ApiController');
const apiController = new ApiController();


router.get('/', apiController.index);
router.post('/postar', apiController.post_inst);
router.post('/gerar_imagem', apiController.gerar_imagem);


module.exports = router;