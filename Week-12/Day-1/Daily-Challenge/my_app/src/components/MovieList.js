import { data } from "../data"

import { selectMovie } from "../redux/action"

import { useDispatch } from "react-redux"

function MovieList() {
    const dispatch = useDispatch()
    return (
        <div>
            <h2>Movie List</h2>
            <ul style={{listStyle: "none", textAlign: "start", margin: '0', padding: '0'}}>
                {data.map((movie, index) => {
                return (
                    <li key={index} style={{display: 'flex', alignItems: 'center', gap: '3rem', justifyContent: 'space-between'}}>
                    <p>
                        {movie.title}
                    </p>
                    <button style={{height: '1.5rem'}} onClick={() => dispatch(selectMovie(movie))}>details</button>
                    </li>
                )
                })}
            </ul>
        </div>
    )
}

export default MovieList
