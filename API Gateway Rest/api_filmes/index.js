const express = require('express');
const server = express();
const filmes = require('./src/data/filmes.json')

server.get('/', (req,res) => {
    return res.json(filmes)
});

server.listen(3002, () => {
    console.log('Servidor beybleidando...')

});