import "./Exercise4.css"

function Exercise4() {
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
    };

    return (
        <>
            <h1 style={style_header}>This is a Title</h1>
            <p className="para">This is a paragraph</p>
            <form>
                <input type="text" />
                <button type="submit">Submit</button>
            </form>

            <a href="https://google.com">Go to Google</a>
            <ul>
                This is an unordered list
                <li>This a topic</li>
                <li>This is another topic</li>
                <li>And this is one more topic</li>
            </ul>
        </>
    )
}

export default Exercise4
