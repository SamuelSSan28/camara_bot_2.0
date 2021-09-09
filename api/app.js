const express = require('express');
const cors = require('cors');
const routes = require('./src/routes/apiRoutes');
const app = express();
require("dotenv").config({path: __dirname + '/.env'});
app.use(express.urlencoded({ extended: true }));

app.use(express.json());

app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Credentials", "true");
    res.setHeader("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT");
    res.setHeader("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers");
    app.use(cors());
    next();
});

app.use(routes);

module.exports = app;