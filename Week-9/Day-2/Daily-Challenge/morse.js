const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`

function toJs(data) {
    return new Promise((res, rej) => {
        if (data) {
            res(JSON.parse(data))
        } else {
            rej("The data is empty")
        }
    })
}

// console.log(toJs(morse))

function toMorse(morseJs) {
    let encryptedMessage = []
    let message = "Hello"
    message = message.toLowerCase().split("")
    return new Promise((res, rej) => {
        if (message.every(character => character in morseJs)) {
            message.forEach(letter => {
                encryptedMessage.push(morseJs[letter])
            });
            res(encryptedMessage)
        } else {
            rej("Your message contains characters that are not on our database of morse codification")
        }
    })
}

function joinWords(morseTranslation) {
    console.log(morseTranslation.join("\n"))
}

toJs(morse)
    .then(res => toMorse(res)
        .then(res => joinWords(res))
        .catch(err => console.log(err)))
    .catch(err => console.log(err))