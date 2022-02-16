const nodeHtmlToImage = require('node-html-to-image');

async function createImage(processo){
    try{
        var autores_li = "";
    const path = `./src/images/image_${processo.protocolo}.jpeg`


    for (const element of processo.autores){
        autores_li += `<li class="item">${element}</li>`
    }
    
    await nodeHtmlToImage({
        output: path,
        html: `
        <html>
        <meta charset="utf-8"/>
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
        <head>
        <style type = "text/css">
            p { font-family: 'Roboto', sans-serif; color: #FFF; font-size: 35px; text-align: justify; }
            li { font-family: 'Roboto', sans-serif; color: #FFF; font-size: 35px; }
            body{
                background-image: url("https://i.imgur.com/3iS3ZrO.jpg");
                -webkit-flex: 1; flex: 1;
                height: 1080px;
                width: 1080px;
                padding: 20px;
                background-size: cover;
            }
            #top{
                margin-top: 20px;
                padding: 50px;
                height: 20%;
                -webkit-flex: 1; flex: 1;
                width: 100%;
            }
            
            #mid{
                font-weight:bold;
                background: rgba(0, 0, 0, 0.75);
                display: -webkit-flex; 
                flex-direction: row-center;
                align-items: center;
                justify-content: center;
                padding: 50px;
                height: 50%;
                -webkit-flex: 1; flex: 1;
                width: 100%;
            }
            #bot{
                padding: 50px;
                height: 30%;
                -webkit-flex: 1; flex: 1;
                width: 100%;
            }
            * {
                -webkit-box-sizing: border-box;
                }
                .flexrow {
                display: -webkit-flex;
                display: flex;
                flex-direction: column;
                flex-wrap: wrap;
                justify-content: space-between;
                }
                .flexrow2 {
                
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                }
                .item {
                margin: 5px;
                text-align: center;
                font-size: 1.8em;
                }
        
            </style>
        </head>
        <body class="flexrow">
        
        <div id="top">
        <p>Data: ${processo.data}</p>
            
        <p>${processo.tipo}</p>
        <p>Situação: ${processo.situacao}</p>
        </div>
        <div id="mid">
        <div id="texto">
            <p>${processo.resumo}</p>
        </div>
        </div>
        <div id="bot">
            <p>Autor(es) da Proposição: </p>
        <ul class="flexrow2">
            ${autores_li}
        </ul>
        </div>
        </body>
        </html>
        `
    }).then(() => {
        
    })
    return path;
    }catch (err){
        throw new Error('Erro ao gerar a imagem: ' + err);
    }
    
}
      
module.exports=createImage;

