// it would be better to do it like this:
// let allBoldItems = document.querySelectorAll("p strong")
// but it's asking to make a function to add it to the variable created

let allBoldItems = [];
let paragraph = document.querySelector("p")

function getBoldItems() {
    for (let tag of paragraph.children) {
        if (tag.tagName == "STRONG") {
            allBoldItems.push(tag)
        }
    }
}

getBoldItems()

function highlight() {
    allBoldItems.forEach(tag => {
        tag.setAttribute("style", "background-color: yellow;")
    });
}

function return_normal() {
    allBoldItems.forEach(tag => {
        tag.removeAttribute("style")
    })
}

paragraph.addEventListener("mouseover", highlight)
paragraph.addEventListener("mouseout", return_normal)