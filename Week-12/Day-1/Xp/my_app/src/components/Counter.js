import {useSelector, useDispatch} from 'react-redux'
import {increment, decrement} from '../redux/action'

function Counter(props) {
    const counter = useSelector(state => state.counter)
    const dispatch = useDispatch()

    return (
        <>
        <button onClick={() => dispatch(increment())}>+</button>
        <h1>{counter}</h1>
        <button onClick={() => dispatch(decrement())}>-</button>
        </>
    )
}

export default Counter