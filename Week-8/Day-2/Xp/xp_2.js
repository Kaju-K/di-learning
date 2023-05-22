// Exercise 1

const sumNumbers = (x, y) => x + y

// Exercise 2

function kiloToGram1(parameter) {
    return parameter*1000
}

const kiloToGram2 = function (parameter) {
    return parameter*1000
}

const kiloToGram3 = (parameter) => parameter*1000

// Exercise 3

console.log((function (numberChildren, partnerName, location, job) {
    return `You will be a ${job} in ${location}, and married to ${partnerName} with ${numberChildren} kids.`
})(10, "John Doe", "Atlantis", "writer"))

// Exercise 5

function makeJuice(size) {
    let ingredients = []
    function addIngredients(one, two, three) {
        ingredients.push(one)
        ingredients.push(two)
        ingredients.push(three)
    }
    
    function displayJuice() {
        let message = `The client wants a ${size} juice, containing `
        ingredients.forEach(ingredient => message += `${ingredient}, `)
        console.log(message.substring(0, message.length-2))
    }

    addIngredients("strawberry", "lemon", "orange")
    addIngredients("grapes", "ice", "watermelon")
    displayJuice()
}

makeJuice("medium")
