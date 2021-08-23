const create_image = require('../utils/createImage');

class ApiController{
    async gerar_imagem(req,res){
        console.log(req.body);
        const processo = req.body;
        try{
            var path = await create_image(processo);
            return res.status(200).json({ path: path })
        } catch(err) {
            err.message;
            return res.status(400).json({ error: 'Erro em gerar imagens.' })
        }
    }

    async index(req,res){
        var obj = { message: 'Rotas funcionando!' }
        return res.send(obj)
    }
}


module.exports = ApiController;