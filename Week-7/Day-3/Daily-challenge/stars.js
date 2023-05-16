numberOfRows = 5

for (let i = 1; i <= numberOfRows; i++) {
    console.log("* ".repeat(i))
}

let text;

for (let i = 1; i<=numberOfRows;i++) {
    text = ""
    for (let j = 1; j <= i; j++) {
        text += "* "
    }
    console.log(text)
}