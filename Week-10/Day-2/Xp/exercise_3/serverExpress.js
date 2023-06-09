const express = require("express")

const app = express()

app.listen(3000, () => {
    console.log("server is running")
})

app.get('/', (req, res) => {
    res.send('<h1>This is a server using express</h1>')
})