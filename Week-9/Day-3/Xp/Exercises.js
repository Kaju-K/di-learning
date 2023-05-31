// Exercise 1

let gif = fetch("https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")

// gif.then(
//     res => res.json()
//         .then(res => console.log(res))
// )

// Exercise 2

let sunGif = fetch("https://api.giphy.com/v1/gifs/search?api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&q=sun&limit=10&offset=2")

// sunGif.then(
//     res => res.json()
//         .then(res => console.log(res))
// )

// Exercise 3

async function dataFetch() {
    let data = await fetch("https://www.swapi.tech/api/starships/9/")
    let dataJson = await data.json()
    console.log(dataJson.result)
}

// dataFetch()

// Exercise 4

function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

asyncCall();
// It should return "calling" and after 2 seconds it should appear "resolved"