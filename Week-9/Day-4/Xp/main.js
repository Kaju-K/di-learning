findButton = document.querySelector(".find")
containerInformation = document.querySelector(".container-information")

findButton.addEventListener("click", async (e) => {
    loadingData()
    let randomCharacter = Math.floor(Math.random()*82 + 1)
    let data = await fetch(`https://www.swapi.tech/api/people/${randomCharacter}`)
    let jsonData = await data.json()
    if (jsonData.message == "ok") {
        
        let character = jsonData.result.properties
        // console.log(character)
        
        let characterInformations = {
            "name": character.name,
            "height": character.height,
            "gender": character.gender,
            "birth": character.birth_year,
            "home world": character.homeworld ? (await (await fetch(character.homeworld)).json()).result.properties.name : "unknown"
        }

        containerInformation.innerHTML = ""

        for (let [key, value] of Object.entries(characterInformations)) {
            let paragraph = document.createElement("p")
            if (key =="name") {
                paragraph.classList.add("character-name")
                paragraph.textContent = value
            } else {
                paragraph.textContent = `${capitalizeFirstLetters(key)}: ${value}`
            }
            containerInformation.appendChild(paragraph)
        }
        
    } else {
        containerInformation.innerHTML = ""
        let paragraph = document.createElement("p")
        paragraph.textContent = `Character doesn't exist`
        containerInformation.appendChild(paragraph)
        
    }
})

function capitalizeFirstLetters(text) {
    let wordsList = text.split(" ")
    let capitalizedWords = wordsList.map(word => word.charAt(0).toUpperCase() + word.slice(1))
    return capitalizedWords.join(" ")
}

function loadingData() {
    containerInformation.innerHTML = `<i class="fa-solid fa-sync fa-spin" style="--fa-animation-timing: ease-in-out; font-size: 3rem;"></i> <p style="font-size: 2rem;">LOADING</p>`
}
