export function selectMovie(value) {
    return {
        type: 'display_movie',
        movieDisplay: true,
        title: value.title,
        releaseDate: value.releaseDate,
        rating: value.rating
    }
}