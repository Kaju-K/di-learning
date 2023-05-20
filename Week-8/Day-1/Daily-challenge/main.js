libForm = document.querySelector("#libform")
story = document.querySelector("#story")

libForm.addEventListener("submit", e => {
    e.preventDefault()
    console.log(e)
    noun = e.target.noun.value
    adjective = e.target.adjective.value
    person = e.target.person.value
    verb = e.target.verb.value
    place = e.target.place.value

    story.textContent = `I have a really ${adjective} family. The one that I like the most is ${person}. ${person} and I love to ${verb} a ${noun}. We do this every year on ${place}`
})