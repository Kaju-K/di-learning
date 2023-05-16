sectionPlanets = document.querySelector(".listPlanets")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

planets.forEach(planet => {
    let newDiv = document.createElement('div')
    newDiv.classList.add('planet', planet.toLowerCase())
    sectionPlanets.appendChild(newDiv)
});