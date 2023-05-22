let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

const displayGroceries = () => {
    groceries["fruits"].forEach(fruit => {
        console.log(fruit)
    });
}

displayGroceries()

const cloneGroceries = () => {
    let user = client
    client = "Betty"
    console.log(user)   // it won't change user, because a string is a primitive value, so when copied, it addresses a new identity (reference in the memory)
    let shoppings = groceries
    groceries["totalPrice"] = "35$"
    groceries["other"]["payed"] = false
    console.log(shoppings)  // it will also change groceries, because when copying a object (list, dictionary...) it addresses the same identity (reference in the memory)
}

cloneGroceries()