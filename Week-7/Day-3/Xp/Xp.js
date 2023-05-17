// Exercise 1
// Part 1

let people = ["Greg", "Mary", "Devon", "James"];

people.splice(people.indexOf("Greg"), 1)

people.splice(people.indexOf("James"), 1, "Jason")

people.push("Kogut")

console.log(people.indexOf("Mary"))

let newPeople = people.slice(1, -1)

console.log(people.indexOf("Foo")) 
// it returns -1 because "Foo" it's not on the list

let last = people[people.length - 1]

// Part 2

for (let i = 0; i<people.length; i++) {
    console.log(people[i])
}

for (let i = 0; i<people.length; i++) {
    if (people[i] == "Jason") {
        break
    }
    console.log(people[i])
}

// Exercise 2

let colors = ["red", "black", "purple", "pink", "blue"]

let position = {
    1: "st",
    2: "nd",
    3: "rd",
}

for (let i = 0; i < colors.length; i++) {
    let index = i + 1
    console.log(`My #${index} choice is ${colors[i]}`)
    if (index in position) {
        console.log(`My ${index + position[index]} choice is ${colors[i]}`)
    } else {
        console.log(`My ${index + "th"} choice is ${colors[i]}`)
    }
}

// Exercise 3

// only works on the DOM

// let number;
// do {
//     number = parseFloat(prompt("Please enter a number:"));
//     if (isNaN(number)) {
//         console.log("You should put a number. Try again")
//     }
//   } while (isNaN(number) || number < 10);

// console.log("Number entered:", number);

// Exercise 4

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building["numberOfFloors"])
console.log(`apartments on floor 1: ${building["numberOfAptByFloor"]["firstFloor"]}`)
console.log(`apartments on floor 3: ${building["numberOfAptByFloor"]["thirdFloor"]}`)

secondTenant = building["nameOfTenants"][1]
console.log(`${secondTenant} has a apartment with ${building["numberOfRoomsAndRent"][secondTenant.toLowerCase()][0]} rooms`)

sarahRent = building["numberOfRoomsAndRent"]["sarah"][1]
danRent = building["numberOfRoomsAndRent"]["dan"][1]
davidRent = building["numberOfRoomsAndRent"]["david"][1]

if ((sarahRent + danRent) > davidRent) {
    building["numberOfRoomsAndRent"]["dan"][1] = 1200
}

console.log(building)

// Exercise 5

let family = {
    members: ["John", "Mary", "Jack", "Bob"],
    lastName: "Doe",
    country: "New Zeland",
}


for (const key of Object.keys(family)){
    console.log(key)
}

for (const value of Object.values(family)){
    console.log(value)
}

// Exercise 6

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}

let message = ""

for (const [key, value] of Object.entries(details)) {
    message += key + " " + value + " "
}

message = message.trim()
console.log(message)

// Exercise 7

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

names.sort()
let secretName = ""

for (let i = 0; i < names.length; i++) {
    secretName += names[i][0]
}

console.log(secretName)