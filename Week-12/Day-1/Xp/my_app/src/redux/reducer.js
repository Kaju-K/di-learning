const initState = {
    counter: 0
}

export function reducer(state=initState, action={}) {
    switch (action.type) {
        case 'increment':
            return {...state, counter: state.counter + 1}
        case 'decrement':
            return {...state, counter: state.counter - 1}
        default:
            return state
    }
}