function UserFavoriteAnimals({animals}){
    return (
        <>
            <p>Favorite Animals:</p>
            <ul>
                {
                    animals.map((animal, index) => {
                        return <li key={index}>{animal}</li>
                    })
                }
            </ul>
        </>
    )
}

export default UserFavoriteAnimals
