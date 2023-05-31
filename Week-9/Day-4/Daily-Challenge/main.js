let myForm = document.querySelector(".my-form")
let result = document.querySelector(".result")
let swapButton = document.querySelector(".swap")

myForm.addEventListener("submit", async (e) => {
    e.preventDefault()
    let firstValue = e.target["first-currency"].value
    let secondValue = e.target["second-currency"].value
    let amount = e.target["amount"].value

    let dataExchange = await fetch(`https://v6.exchangerate-api.com/v6/${config.API_KEY}/pair/${firstValue}/${secondValue}/${amount}`)
    let jsonDataExchange = await dataExchange.json()

    let conversion = jsonDataExchange.conversion_result

    result.innerHTML = `<p>${conversion.toFixed(2)}</p>`


})

swapButton.addEventListener("click", e => {
    [firstCurrency.value, secondCurrency.value] = [secondCurrency.value, firstCurrency.value]
})