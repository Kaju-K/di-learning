// Exercise 1

// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);
// ['bread', 'carrot', 'potato', 'chicken', 'apple', 'orange']

// ------2------
const country = "USA";
console.log([...country]);
// ['U', 'S', 'A']

// ------Bonus------
let newArray = [...[, ,]];
console.log(newArray);
// apperantly the result is [undefined, undefined], although it seems like it should be 3 undefineds

// Exercise 2

const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
            { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
            { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
            { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
            { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
            { firstName: 'Wes', lastName: 'Reid', role: 'Instructor' },
            { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor' }];

let welcomeStudents = users.map(user => {
    return `Hello ${user.firstName}`
})

console.log(welcomeStudents)

let fullStackResident = users.filter(user => user.role == "Full Stack Resident").map(user => user.lastName)

console.log(fullStackResident)

// Exercise 3

const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

let completeMessage = epic.reduce((partialString, x) => partialString + " " + x, "").trim()

console.log(completeMessage)

// Exercise 4

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];

students.filter(student => student.isPassed).forEach(student => {
    console.log(`Congratulations ${student.name}, you passed the course in ${student.course}`)
})