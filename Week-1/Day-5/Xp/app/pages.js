navLinks = document.querySelectorAll(".nav-links")
pages = document.querySelectorAll(".page")

navLinks.forEach( (link, index) => {
    link.addEventListener("click", e => {
        let navClasses = e.target.classList
        let navClassesArray = Array.from(navClasses)
        if (navClassesArray.includes("nav-link--active")) {
            return
        } else {
            for (let i = 0; i < navLinks.length; i++) {
                let classes = Array.from(navLinks[i].classList)
                if(classes.includes("nav-link--active")) {
                    navLinks[i].classList.remove("nav-link--active")
                    pages[i].classList.remove("page--active")
                }
            }
            navClasses.add("nav-link--active")
            pages[index].classList.add("page--active")
        }
    })
});