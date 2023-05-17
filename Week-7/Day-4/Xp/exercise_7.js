allBooks = [
    {
        title: "Harry Potter",
        author: "J.K. Rolling",
        image: "https://m.media-amazon.com/images/I/71HbYElfY0L._AC_UF1000,1000_QL80_.jpg",
        alreadyRead: true
    },
    {
        title: "Lord of the Rings",
        author: "J.R.R. Tolkien",
        image: "https://kbimages1-a.akamaihd.net/7a557cb3-f72a-47c3-992b-951c9566e4d4/1200/1200/False/the-fellowship-of-the-ring-the-lord-of-the-rings-book-1-1.jpg",
        alreadyRead: false
    },
    {
        title: "Sapiens",
        author: "Yuval Noah Harari",
        image: "https://m.media-amazon.com/images/I/713jIoMO3UL.jpg",
        alreadyRead: false
    },
    {
        title: "Hitchhiker's Guide to the Galaxy",
        author: "Douglas Adams",
        image: "https://m.media-amazon.com/images/I/81XSN3hA5gL._AC_UF1000,1000_QL80_.jpg",
        alreadyRead: true
    }
]

listBooks = document.querySelector(".listBooks")
for (let book of allBooks) {
    let newDiv = document.createElement("div")
    let details = document.createElement("p")
    let image = document.createElement("img")
    details.textContent = `${book.title} written by ${book.author}`
    if (book.alreadyRead) {
        details.setAttribute("style", "color: red;")
    }
    newDiv.appendChild(details)
    image.setAttribute("src", book.image)
    image.setAttribute("style", "width: 100px;")
    newDiv.appendChild(image)
    listBooks.appendChild(newDiv)
}