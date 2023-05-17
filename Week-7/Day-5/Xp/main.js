function playTheGame() {
    let confirmation = confirm("Do you want to play the game?")
    if (!confirmation) {
        return
    }
    let double_confirmation = confirm("Do you REALLY want to play the game?")
    if (!double_confirmation) {
        return
    }
    let chances = 3
    let computerNumber = Math.floor(Math.random()*11)
    let number
    for (let chance = 0; chance<chances; chance++) {
        do {
            number = parseFloat(prompt("Enter a number:"))
        } while ((isNaN(number)) || (number<0) || (number>10))
    
        let comparison = compareNumbers(number, computerNumber)
        if (comparison) {
            return
        }
    }
    alert(`Nevermind. You are out of chances. The computers number was: ${computerNumber}. Goodbye`)
}

function compareNumbers(userNumber, computerNumber) {
    if (userNumber == computerNumber) {
        alert("WINNER")
        return true
    } else if (userNumber>computerNumber) {
        alert("Your number is bigger then the computer's, guess again")
        return false
    } else if (userNumber<computerNumber) {
        alert("Your number is smaller then the computer's, guess again")
        return false
    }
}