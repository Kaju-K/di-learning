function makeAllCaps(wordsArray) {
    return new Promise((res, rej) => {
        wordsArray.every(value => typeof(value)=="string") ? res(wordsArray.map(word => word.toUpperCase())) : rej("Not all values from the array are strings")
    })
}

function sortWords(wordsArray) {
    return new Promise((res, rej) => {
        wordsArray.length >= 4 ? res(wordsArray.sort()) : rej("The Array should be bigger or equal to 4")
    })
}

//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, you should see in the console, 
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
      .catch(error => console.log(error))