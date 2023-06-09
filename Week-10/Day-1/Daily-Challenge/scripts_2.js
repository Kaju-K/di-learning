const {getCurrentDate} = require("./main.js");

let http = require("http");


const server = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/html')
    res.end(`<p>The current date and time is ${getCurrentDate()}</p>`)
})

server.listen(8080)