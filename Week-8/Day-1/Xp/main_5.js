hand = document.querySelector("#hand")

let clicked = false;

initialX = hand.offsetLeft
initialY = hand.offsetTop
handHeight = hand.offsetHeight
handWidth = hand.offsetWidth


hand.addEventListener("mouseover", e => {
    e.target.animate(
        {
            fontSize: "4rem",
        },
        {
        duration: 1000,
        fill: "forwards",
        easing: "ease",
    })
})

hand.addEventListener("mouseout", e => {
    e.target.animate(
        {
            fontSize: "2rem",
        },
        {
        duration: 1000,
        fill: "forwards",
        easing: "ease",
    })
})

window.addEventListener("mousemove", event => {
    if (clicked) {
        hand.animate(
            {
                transform: `translate(${event.clientX - (initialX+handWidth/2)}px, ${event.clientY - (initialY + handHeight/2)}px)`,
            }, 
            {
                duration: 1000,
                fill: "forwards",
                easing: "ease",
            }
        )
    }
})

hand.addEventListener("click", e => {
    clicked = true
})

hand.addEventListener("dblclick", e => {
    clicked = false
})