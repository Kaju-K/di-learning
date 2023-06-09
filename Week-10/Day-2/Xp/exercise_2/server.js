const http = require("http")

const user = {
    firstname: "John",
    lastname: "Doe"
}

const server = http.createServer((req, res) => {
    res.setHeader("Content-Type", "text/html")
    res.write(JSON.stringify(user))
    res.end()
})

server.listen(3000)