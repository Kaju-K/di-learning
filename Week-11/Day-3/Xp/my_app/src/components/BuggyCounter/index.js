
import React from 'react'

class BuggyCounter extends React.Component {
    constructor() {
        super()
        this.state = {
            counter: 0
        }
    }

    handleClickCounter = () => {
        this.setState({counter: this.state.counter + 1}, () => {
            if (this.state.counter >= 5) {
                throw new Error("I crashed")
            }
        })
        
    }

    render() {
        return (
            <div>
                <p>{this.state.counter}</p>
                <button onClick={this.handleClickCounter}>Increment</button>
            </div>
        )
    }
}

export default BuggyCounter
