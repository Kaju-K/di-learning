stringifiedContainer = document.querySelector(".stringified-container")

form = document.querySelector(".form-data")

form.addEventListener("submit", e => {
    e.preventDefault()
    dataDict = {}
    fields = [...e.target.children]
    fields.forEach(field => {
        if (field.tagName == "BUTTON") {
            return
        }
        dataDict[field.name] = field.value
        field.value = ""
    });

    stringifiedData = JSON.stringify(dataDict)

    newParagraph = document.createElement("p")
    newParagraph.textContent = stringifiedData

    stringifiedContainer.appendChild(newParagraph)
})