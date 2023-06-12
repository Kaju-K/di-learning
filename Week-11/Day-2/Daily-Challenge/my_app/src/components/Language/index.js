import style from './Language.module.css'

function Language({info, setVote}) {
    function handleClick() {
        setVote((info) => {
            return {...info, count: info.count+1}
        })
    }

    return (
        <div className={style.card}>
            <p>{info.count}</p>
            <p>{info.name}</p>
            <button className={style.vote_button} onClick={handleClick}>Click Here</button>
        </div>
    )
}

export default Language
