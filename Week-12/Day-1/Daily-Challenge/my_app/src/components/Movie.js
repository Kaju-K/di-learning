import { useSelector } from "react-redux"

function Movie() {
    const [movieDisplay, title, releaseDate, rating] = useSelector(state => {
        return [state.movieDisplay, state.title, state.releaseDate, state.rating]
    })

    return (
        <div>
            <h2>Movie</h2>
            {
            movieDisplay ? (
                <>
                <p>title: {title}</p>
                <p>Release Date: {releaseDate}</p>
                <p>Rating: {rating}</p>
                </>
            ) : "Select Movie"
            }
        </div>
    )
}

export default Movie