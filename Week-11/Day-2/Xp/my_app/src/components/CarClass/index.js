import React from 'react'
import GarageClass from '../GarageClass'

class CarClass extends React.Component {
    constructor(){
        super()
        this.state = {
            color: 'red'
        }
    };
    render() {
        return (
            <div>
                <h1>This car is a {this.state.color} {this.props.info.model}</h1>
                <GarageClass size="small" />
            </div>
        );
    }
}

export default CarClass
