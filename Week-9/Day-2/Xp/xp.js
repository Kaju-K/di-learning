// Exercise 1

function compareToTen(num) {
    return new Promise((res, rej) => {
        num < 10 ? res(`${num} is  accepted`) : rej(`${num} is rejected`)
    })
}

//In the example, the promise should reject
compareToTen(15)
    .then(result => { console.log(result) })
    .catch(error => {
        console.log(error)
    })

// In the example, the promise should resolve
compareToTen(8)
    .then(result => console.log(result))
    .catch(error => console.log(error))

// Exercise 2

let successPromise = new Promise((res, rej) => {
    setTimeout(() => res("Success"), 4000)
})

successPromise.then(res => console.log(res)).catch(err => console.log(err))

setTimeout(() => Promise.resolve("Success").then(res => console.log(res)).catch(err => console.log("Oops something went wrong")), 4000)

// Exercise 3

let resolvedPromise = Promise.resolve(3)
let rejectedPromise = Promise.reject("Boo")

resolvedPromise.then(res => console.log(res)).catch(err => console.log(err))
rejectedPromise.then(res => console.log(res)).catch(err => console.log(err))