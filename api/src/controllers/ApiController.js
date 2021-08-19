class ApiController{

    async home(req,res){
        var obj = { message: 'Api funcionando!' }
        return res.send(obj)
    }

    async index(req,res){
        var obj = { message: 'Rotas funcionando!' }
        return res.send(obj)
    }
}


module.exports = ApiController;