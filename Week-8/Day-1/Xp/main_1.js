let mainTitle = document.querySelector("h1")
console.log(mainTitle)

let article = document.querySelector("article")

article.lastElementChild.remove()

article.children[1].addEventListener("click", e => {
    e.target.setAttribute("style", "background-color:red;")
})

article.children[2].addEventListener("click", e => {
    e.target.setAttribute("style", "display: None;")
})

function makeBold() {
    paragraphs = document.querySelectorAll("p")
    paragraphs.forEach(paragraph => {
        paragraph.setAttribute("style", "font-weight: bold;")
    });
}