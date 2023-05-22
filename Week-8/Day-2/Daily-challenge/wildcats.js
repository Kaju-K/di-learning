const gameInfo = [
    {
        username: "john",
        team: "red",
        score: 5,
        items: ["ball", "book", "pen"]
    },
    {
        username: "becky",
        team: "blue",
        score: 10,
        items: ["tape", "backpack", "pen"]
    },
    {
        username: "susy",
        team: "red",
        score: 55,
        items: ["ball", "eraser", "pen"]
    },
    {
        username: "tyson",
        team: "green",
        score: 1,
        items: ["book", "pen"]
    },
];

let usernames = []
let winners = []
let totalScore = 0

gameInfo.forEach(info => {
    usernames.push(`${info.username}!`)
})

console.log(usernames)

gameInfo.forEach(info => {
    info.score > 5 && winners.push(info.username)
})

console.log(winners)

gameInfo.forEach(info => totalScore += info.score)

console.log(totalScore)