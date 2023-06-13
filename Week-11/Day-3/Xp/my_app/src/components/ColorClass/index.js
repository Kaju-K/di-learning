import React from "react";
import Child from "../Child";

class ColorClass extends React.Component {
    constructor() {
        super()
        this.state = {
            favoriteColor: 'red',
            show: true
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

    getSnapshotBeforeUpdate(prevProps, prevState) {
        const div = document.querySelector('#previous')
        div.innerHTML = `<p>Before the update, the favorite color was ${prevState.favoriteColor}</p>`
        return true
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        // console.log(prevProps, prevState, snapshot)
    }    

    render() {
        return (
            <div>
                <h1>My favorite color is {this.state.favoriteColor}</h1>
                <button onClick={this.changeFavoriteColor}>Change color</button>
                <div id="previous"></div>

                {
                    (this.state.show) ? (
                        <>
                            <Child />
                            <button onClick={() => {this.setState({show: false})}}>Delete Header</button>
                        </>
                    ) : null
                }
            </div>
        )
    }
}

export default ColorClass
