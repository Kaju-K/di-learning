import React from 'react'

class ClickMe extends React.Component {
    constructor() {
        super()
        this.state = {
            isToggledOn: true
        }
    }

    clickMe = () => {
        alert("I was clicked")
    }

    handleKeyDown = (e) => {
        console.log(e)
        if (e.code==="Enter") {
            alert(`The Enter key was pressed, your input is: ${e.target.value}`)
        }
    }

    handleClick = () => {
        this.setState({isToggledOn: !this.state.isToggledOn})
    }

    render() {
        return (
            <>
                <div>
                    <button onClick={this.clickMe}>Click Me</button>
                </div>
                <div>
                    <input type='text' onKeyDown={this.handleKeyDown} />
                </div>
                <div>
                    <button onClick={this.handleClick}>{this.state.isToggledOn ? "ON" : "OFF"}</button>
                </div>
            </>
        )
    }
}

export default ClickMe
