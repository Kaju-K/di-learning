container = document.querySelector("#container")
clearButton = document.querySelector("#clear")

setTimeout(()=>{alert("Hello World")}, 2000)
setTimeout(()=>{
    paragraph = document.createElement("p")
    paragraph.textContent = "Hello World"
    container.appendChild(paragraph)
}, 2000)

addingParagraph = setInterval(()=>{
    if (container.children.length < 5) {
        paragraph = document.createElement("p")
        paragraph.textContent = "Hello World"
        container.appendChild(paragraph)
    } else {
        clearInterval(addingParagraph)
    }
}, 2000)

clearButton.addEventListener("click", (e)=>{
    clearInterval(addingParagraph)
})