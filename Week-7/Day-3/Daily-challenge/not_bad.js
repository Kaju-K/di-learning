let sentence = "The movie is not that bad, I like it"

let wordNot = sentence.indexOf("not")
let wordBad = sentence.indexOf("bad")

let message;

if ((wordNot >=0) & (wordBad >= 0) & (wordBad > wordNot)) {
    message = sentence.slice(0,wordNot) + "good" + sentence.slice(wordBad+3)
} else {
    message = sentence
}

console.log(message)