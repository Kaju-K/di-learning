myForm = document.querySelector("#MyForm")
body = document.querySelector("body")

myForm.addEventListener("submit", e => {
    e.preventDefault()
    console.log(e)
    e.target.volume.value = Math.round((4/3) * Math.PI * parseFloat(e.target.radius.value)**3 * 100) / 100
})