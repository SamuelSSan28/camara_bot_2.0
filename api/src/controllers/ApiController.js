const Functions = require('../functions/Functions');
const functions = new Functions();

class ApiController{
    async gerar_imagem(req,res){
        console.log(req.body);
        const processo = req.body;
        try{
            var path = await functions.generate_img(processo);
            return res.status(200).json({ message: path })
        } catch(err) {
            err.message;
            return res.status(400).json({ message: 'Erro em gerar imagens.' })
        }
    }

    async index(req,res){
        var obj = { message: 'Rotas funcionando!' }
        return res.send(obj)
    }
}


module.exports = ApiController;