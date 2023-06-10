let express = require('express')
let knex = require('knex');
let p4ssw0rd = require('p4ssw0rd')


let app = express()
app.listen(3000)
// use public folder with the static files
app.use('/', express.static(__dirname + '/public'))
// use post method
app.use(express.urlencoded({extended:true}))
app.use(express.json())

app.set('view engine', 'ejs');

// connect to the database
let db = knex({
    client: 'pg',
    connection: {
        host: 'localhost',
        port: '5433',
        user: 'postgres',
        password: '271828',
        database: 'di-login-register'
    }
})

app.get('/login', (req, res) => {
    let informations = req.query
    db
        .select('username', 'password')
        .from('users')
        .where({username: informations.username_login})
        .then( res2 => {
            if (p4ssw0rd.check(informations.password_login, res2[0].password)) {
                return res.render(__dirname + '/public/login', { message: "", login_message: `Welcome ${res2[0].username}`})
            } 
            return res.render(__dirname + '/public/login', { message: "", login_message: `Invalid Password`})
        })
        .catch( err => {
            return res.render(__dirname + '/public/login', { message: "", login_message: `Invalid Username`})

        })
})

app.post('/login', (req, res) => {
    let information = req.body
    let date = new Date()
    let month = date.getUTCMonth() + 1
    let day = date.getUTCDate()
    let year = date.getUTCFullYear()
    let message = "";
    db('users')
        .insert({
            first_name: information.first_name,
            last_name: information.last_name,
            email: information.email,
            username: information.username_register,
            password: p4ssw0rd.hash(information.password_register),
            created_date: year + "/" + month + "/" + day
        })
        .then( res2 => {
            db
                .select('user_id', 'first_name', 'last_name')
                .from('users').where({username: information.username_register})
                .then(res3 => {
                    console.log(res3)
                    message = `Ok. Hello, ${res3[0].first_name} ${res3[0].last_name}. Your user id is ${res3[0].user_id}`
                    res.render(__dirname + '/public/login', { message: message, login_message: "" })
                })
            }
            )
            .catch(err => {
                console
                message = err.detail
                res.render(__dirname + '/public/login', { message: message, login_message: "" })
        })
})

app.get('/users', (req, res) => {
    db.select().from('users').then(rows => res.json(rows))
})