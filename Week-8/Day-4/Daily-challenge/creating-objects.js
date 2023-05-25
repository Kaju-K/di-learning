class Video {
    constructor(title, uploader, time) {
        this.title = title
        this.uploader = uploader
        this.time = time
    }

    watch(){
        console.log(`${this.uploader} watched all the ${this.time} seconds of ${this.title}`)
    }
}

let video1 = new Video("Crazy Cat", "Kogut", 180)
let video2 = new Video("Awesome Destinations", "Marcelo", 600)

video1.watch()
video2.watch()
