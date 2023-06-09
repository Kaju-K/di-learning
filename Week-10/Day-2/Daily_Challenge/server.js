const express = require('express')

const app = express()

app.listen(3000)

app.use('/', express.static(__dirname + '/public'))

app.get('/aboutMe/:hobby', (req, res) => {
    const hobby = req.params.hobby
    if (isNaN(hobby)){
        res.send(`My hobby is: ${hobby}`)
    } else {
        res.status(404).send('Hobby shouldn\'t be a number')
    }
})

app.get('/pic', (req, res) => {
    res.sendFile(__dirname + '/public/pic.html')
})

app.get('/form', (req, res) => {
    res.sendFile(__dirname + '/public/form.html')
})

app.get('/formData', (req, res) => {
    const informations = req.query
    res.send(`${informations.email} said: ${informations.message}`)
})