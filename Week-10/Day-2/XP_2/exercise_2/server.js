const express = require('express')

const app = express()

app.listen(3000)

app.get('/:id', (req, res) => {
    const jsonId = req.params
    console.log(jsonId)
    res.json(jsonId)
})