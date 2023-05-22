// let paragraph = document.querySelector("li")
let navbar = document.querySelector(".navbar-nav");

(function (user) {
    let listItem = document.createElement("li")
    listItem.classList.add("nav-item")

    let linkItem = document.createElement("a")
    linkItem.classList.add("nav-link")
    linkItem.setAttribute("href", "#")
    linkItem.textContent = user

    listItem.appendChild(linkItem)

    navbar.appendChild(listItem)
})("You");