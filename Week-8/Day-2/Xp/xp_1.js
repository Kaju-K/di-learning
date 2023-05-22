// Exercise 2

const winBattle = () => true

let experiencePoints;

winBattle() ? experiencePoints = 10 : experiencePoints = 1

console.log(experiencePoints)

// Exercise 3

const isString = (parameters) => {
    return (typeof(parameters) == "string") ? true : false
}

console.log(isString('hello')); 
//true
console.log(isString([1, 2, 4, 0]));
//false

// Exercise 4

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

const orders = (listParameters) => {
    listParameters.forEach((color, index, arr) => {
        arr[index] = `${index+1}${(index+1==1)?"st":(index+1)==2?"nd":(index+1)==3?"rd":"th"} choice is ${color}`
    })
    return listParameters.join(", ")
}

console.log(orders(colors))

// Exercise 6

let bankAmount; 
const VAT = 0.17
let details = ["+200", "-100", "+146", "+167", "-2900"]

const changeDetails = (listParameters) => {
    listParameters.every((value,index,array) => array[index] = value*(1 + VAT))
}

changeDetails(details)
bankAmount = details.reduce((partialSum, x) => partialSum + x, 0)

console.log(details)
console.log(bankAmount)