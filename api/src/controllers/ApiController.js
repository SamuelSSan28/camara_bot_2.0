const create_image = require('../utils/createImage');
const post_instagram = require('../utils/postInstagram')

class ApiController{
    async gerar_imagem(req,res){
        try{
            const processo = req.body;
            var path = await create_image(processo);
            return res.status(200).json({ path: path })
        } catch(err) {
            console.log(err.message)
            return res.status(400).json({ error: 'Erro em gerar imagens.' })
        }
    }

    async index(req,res){
        var obj = { message: 'Rotas funcionando!' }
        return res.send(obj)
    }

    async post_inst(req,res){
        try{
            console.log("Postar ->",req.body);
            const path = req.body.path;
            const result = await post_instagram(path);   
            return res.status(200).json({ path: result })
        }catch(err) {
            console.log(err.message)
            return res.status(400).json({ error: 'Erro em postar imagens.' + err.message })
        }  
    }
}


module.exports = ApiController;