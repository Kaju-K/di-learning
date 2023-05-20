form = document.querySelector("form")
usersAnswer = document.querySelector(".usersAnswer")

// console.log(form)

firstNameById = document.querySelector("#fname")
lastNameById = document.querySelector("#lname")
submitById = document.querySelector("#submit")

// console.log(firstNameById, lastNameById, submitById)

firstNameByName = document.querySelector("[name=fname]")
lastNameByName = document.querySelector("[name=lname]")

// console.log(firstNameByName, lastNameByName)

form.addEventListener("submit", e => {
    e.preventDefault()
    console.log(firstNameById.value)
    if (firstNameById.value && lastNameById.value) {
        answer = document.createElement("li")
        pFirstName = document.createElement("p")
        pLastName = document.createElement("p")

        pFirstName.textContent = firstNameById.value
        pLastName.textContent = lastNameById.value

        answer.setAttribute("style", "border: 1px solid black; border-radius: 5px; padding: 0.5rem; list-style: none; margin:0.5rem;")
        answer.appendChild(pFirstName).appendChild(pLastName)
        usersAnswer.appendChild(answer)
    }
})