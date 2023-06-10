// Exercise 1

let fs = require('fs')

fs.readFile(__dirname + '/text.txt', 'utf-8', (err, data) => {
    if (err) {
        console.log(err)
    } else {
        console.log(data)
    }
})

// Exercise 2

fs.writeFile(__dirname + "/exercise_2.txt", "Creating file\n", (err) => {
    if (err) {
        console.log(err)
    } else {
        console.log("File created")
    }
})

fs.appendFile(__dirname + "/exercise_2.txt", "Appending to the file\n", (err) => {
    if (err) {
        console.log(err)
    }
})

fs.unlink(__dirname + "/exercise_2.txt", (err) => {
    if (err) {
        console.log(err)
        return
    }
    console.log("File deleted")
})