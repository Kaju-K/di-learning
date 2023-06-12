import React from "react";

class PhoneClass extends React.Component {
    constructor() {
        super()
        this.state = {
            brand: "Samsung",
            model: "Galaxy S20",
            color: "black",
            year: 2020
        };
    }

    changeColor = () => {
        this.setState({color: (this.state.color === "black") ? "blue" : "black"})
    }

    render() {
        return (
            <div>
                <h1>My phone is a {this.state.brand}</h1>
                <h2>It is a {this.state.color} {this.state.model} from {this.state.year}</h2>
                <div>
                    <button onClick={this.changeColor} >Change Color</button>
                </div>
            </div>
        )
    }

}

export default PhoneClass
