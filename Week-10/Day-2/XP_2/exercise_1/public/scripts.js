const root = document.querySelector(".root")

console.log('oi')

fetch("http://localhost:3000/users")
    .then(res => res.json())
    .then(res => {
        console.log(res)
        root.textContent = JSON.stringify(res)
    })
    .catch(err => console.log(err))