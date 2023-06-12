import React from "react";

class ColorClass extends React.Component {
    constructor() {
        super()
        this.state = {
            favoriteColor: 'red'
        }
    }

    componentDidMount() {
        setTimeout(() => {
            this.setState({favoriteColor: 'yellow'})
        }, 5000)
    }
    
    changeFavoriteColor = () => {
        this.setState({favoriteColor: 'blue'})
    }

    render() {
        return (
            <div>
                <h1>My favorite color is {this.state.favoriteColor}</h1>
                <button onClick={this.changeFavoriteColor}>Change color</button>
            </div>
        )
    }
}

export default ColorClass
