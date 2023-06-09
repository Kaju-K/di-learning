const express = require('express')

const app = express()

app.listen(3000)

const user = {firstname: 'John',lastname: 'Doe'}

app.use("/", express.static(__dirname + '/public'))

app.get('/users', (req, res) => {
    res.json(user)
})