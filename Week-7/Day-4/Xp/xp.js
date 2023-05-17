// Exercise 1
function isDivisible(divisor) {
    let sum = 0
    for (let i = 0; i<=500; i++) {
        if (i % divisor === 0) {
            sum += i
            console.log(i)
        }
    }
    console.log(`Sum: ${sum}`)
}

// isDivisible(23)

// Exercise 2

const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

let shoppingList = ['banana', 'orange', 'apple']

function myBill() {
    let bill = 0;
    for (let item of shoppingList) {
        if (stock[item] > 0) {
            bill += prices[item]
            stock[item] -= 1
        }
    }
    return bill
}

// console.log(myBill())

// Exercise 3

let coinsValue = [0.25, 0.1, 0.05, 0.01]

function changeEnough(itemPrice, amountOfChange) {
    let total = 0
    for (let [index, value] of Object.entries(amountOfChange)) {
        total += value*coinsValue[index]
    }
    if (total >= itemPrice) {
        return true
    }
    return false
}

// console.log(changeEnough(0.75, [0,0,20,5]))

// Exercise 4

function hotelCost() {
    const pricePerDay = 140
    let numberDays = Math.floor(Math.random()*16)
    return pricePerDay * numberDays
}

function planeRideCost() {
    const placeCosts = {
        "London": 183,
        "Paris": 220,
    }

    const destinations = ["London", "Paris", "Other"]

    let destination = destinations[Math.floor(Math.random()*destinations.length)]
    return (destination in placeCosts) ? placeCosts[destination] : 300
}

function rentalCarCost() {
    let numberDays = Math.floor(Math.random()*16)
    const pricePerDay = (numberDays <= 10) ? 40 : 40*0.95

    return numberDays*pricePerDay
}

function totalVacationCost() {
    return (
        `The car cost: $${rentalCarCost()}
The hotel cost: $${hotelCost()}
The plane tickets cost: $${planeRideCost()}`
    )
}

// console.log(totalVacationCost())

// Exercise 5

// HTML file

