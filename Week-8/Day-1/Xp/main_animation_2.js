animate = document.querySelector("#animate")
container = document.querySelector("#container")

containerWidth = container.offsetWidth
animateWidth = animate.offsetWidth

function myMove() {
    counter = 0
    animate.style.left = 0
    console.log(animate.style.left)
    moving = setInterval(()=>{
        if (animate.style.left != `${containerWidth - animateWidth}px`) {
            animate.style.left = `${counter}px`
            counter++
        } else {
            clearInterval(moving)
        }
    }, 1)

}