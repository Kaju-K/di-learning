firstCurrency = document.querySelector("#first-currency")
secondCurrency = document.querySelector("#second-currency")

async function supportedCodes() {
    let data = await fetch(`https://v6.exchangerate-api.com/v6/${config.API_KEY}/codes`)
    let jsonData = await data.json()
    return jsonData.supported_codes
}

async function addingOptions() {
    let codes = await supportedCodes()
    codes.forEach(code => {
        // create the option tag
        let optionValue = document.createElement("option")
        optionValue.setAttribute("value", `${code[0]}`)
        optionValue.textContent = `${code[0]} - ${code[1]}`

        // add option tag to both selectors
        firstCurrency.appendChild(optionValue)
        secondCurrency.appendChild(optionValue.cloneNode(true))
    });
}

addingOptions()