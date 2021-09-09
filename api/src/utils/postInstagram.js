const Instagram = require('instagram-web-api');
const fs = require('fs');

async function post_instagram(path){

  try{
    console.log(__dirname)
    const { USERNAME_INSTAGRAM, PASSWORD_INSTAGRAM } = process.env; 
    
    const client = new Instagram({ username:USERNAME_INSTAGRAM, password:PASSWORD_INSTAGRAM })
      

    await (async() => {
      await client.login()
      //console.log("Postando no Instagram")
      
        try {    
          
          await client.uploadPhoto({photo: path, caption: "#custopiaui  #leisteresina ", post: 'feed' });
          //console.log("postada")
          fs.unlink(path, (err) => {
              if (err) {
                console.log("Erro ao deletar a imagem"+err)
              }
            });
          return path
        } catch (err) {
          console.log("Erre na requisiçaõ "+err)
        }
        
        
    })()

  }catch(erro){
    throw new Error('Erro ao realizar o post');
  }
  
}

module.exports = post_instagram;