import { robots } from "./data.js"

console.log(robots);

let cardContainer = document.querySelector(".cards-container");

function displayRobot(robot) {
    // creating the card
    let robotArticle = document.createElement("article")
    robotArticle.classList.add("card")

    // creating the image
    let robotImage = document.createElement("img")
    robotImage.setAttribute("src", robot.image)
    robotImage.setAttribute("alt", robot.name)
    robotImage.classList.add("card-image")

    // creating the div for information
    let robotInformation = document.createElement("div")
    robotInformation.classList.add("card-information")

    // creating the title
    let robotName = document.createElement("h2")
    robotName.classList.add("robot-name")
    robotName.textContent = robot.name

    // creating the description
    let robotDescription = document.createElement("p")
    robotDescription.classList.add("robot-description")
    robotDescription.textContent = robot.email

    // appending the title and description to the information div
    robotInformation.appendChild(robotName)
    robotInformation.appendChild(robotDescription)

    // appending the image and information to the card
    robotArticle.appendChild(robotImage)
    robotArticle.appendChild(robotInformation)

    // appending the card to the page
    cardContainer.appendChild(robotArticle)
}


robots.forEach(robot => displayRobot(robot));

let searchBar = document.querySelector(".search-bar")

searchBar.addEventListener("input", e => {
    // console.log(e.target.value)
    let typing = e.target.value
    let patt = new RegExp(typing, "i")

    cardContainer.innerHTML = ''

    robots.filter(robot => robot.name.match(patt)).forEach(robot => displayRobot(robot))
})