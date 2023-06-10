let fs = require('fs')
const { type } = require('os')

fs.readFile(__dirname + '/RightLeft.txt', 'utf-8', (err, data) => {
    let position = 0
    let steps_to_minus_one = []
    for (let [index, value] of Object.entries(data)) {
        if (value == ">") {
            position += 1
        } else if (value == "<") {
            position -= 1
        }
        if (position == -1) {
            steps_to_minus_one.push(parseInt(index)+1)
        }
    }

    if (position) {
        console.log(`Total steps: ${Math.abs(position)} to the ${(position >= 0) ? "right" : "left" }`)
    } else {
        console.log(`Total steps: ${position}`)
    }
    
    console.log(`First time in the left side is in: ${steps_to_minus_one[0]}`)
})
