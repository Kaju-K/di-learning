const {largeNumber} = require("./main.js");
let http = require("http");

const b = 5;

const c = largeNumber + b

const server = http.createServer( (req, res) => {
    console.log("I'm listening")
    res.setHeader('Content-Type', 'text/html')
    res.end(`My Module is\n ${c}\n<h1>Hi there at the frontend</h1> `)
})

server.listen(3000)