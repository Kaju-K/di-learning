gifsList = document.querySelector(".gifs-list")
myForm = document.querySelector("#my-form")
deleteAll = document.querySelector(".delete-all")

async function gifSearcher(category) {
    let data = await fetch(`https://api.giphy.com/v1/gifs/search?api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&q=${category}`)
    let jsonData = await data.json()
    let gifs = jsonData.data
    let randomGif = gifs[Math.floor(Math.random()*gifs.length)]
    return randomGif
}

myForm.addEventListener("submit", async (e) => {
    e.preventDefault()
    category = e.target.category.value
    let randomGif = await gifSearcher(category)
    let urlGif = randomGif.images.downsized.url
    
    // create the div that will contain the img and button
    let gifDiv = document.createElement("div")
    
    // create the img
    let gifImg = document.createElement("img")
    gifImg.setAttribute("src", urlGif)
    gifImg.setAttribute("alt", randomGif.title)

    // create the button
    let gifDelete = document.createElement("button")
    gifDelete.textContent = "DELETE"
    
    // adding the event listener to the button
    gifDelete.addEventListener('click', e => {
        e.target.parentNode.remove()
    })

    // add img and button to gifDiv
    gifDiv.appendChild(gifImg)
    gifDiv.appendChild(gifDelete)

    // add gifDiv to gifsList
    gifsList.appendChild(gifDiv)
})

deleteAll.addEventListener("click", e => {
    gifsList.innerHTML = ""
})