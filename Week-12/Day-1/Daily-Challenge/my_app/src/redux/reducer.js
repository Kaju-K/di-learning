const initState = {
    movieDisplay: false,
    title: null,
    releaseDate: null,
    rating: null
}

export function reducer(state=initState, action={}) {
    switch (action.type){
        case 'display_movie':
            return {
                ...state,
                movieDisplay: action.movieDisplay,
                title: action.title,
                releaseDate: action.releaseDate,
                rating: action.rating
            }
        default:
            return state
    }
}