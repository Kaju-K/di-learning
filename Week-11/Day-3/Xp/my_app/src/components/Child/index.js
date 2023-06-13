import React from 'react'

class Child extends React.Component {
    componentWillUnmount() {
        alert("The Header will be deleted")
    }

    render() {
        return (
            <div>
                <h2>Hello World</h2>
            </div>
        )
    }
}

export default Child
