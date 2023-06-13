import React from 'react'

class ErrorBoundry extends React.Component {
    constructor() {
        super()
        this.state = {
            hasError: false,
            info: '',
            error: ''
        }
    }

    static getDerivedStateFromError(error) {
        return { hasError: true }
    }

    // componentDidCatch(error, info) {
    //     this.setState({info: 2, error: error}, console.log(this.state.info, this.state.error))
    // }
    componentDidCatch(error, errorInfo) {
        this.setState({
            error: error,
            errorInfo: errorInfo
        })
    }
    render() {
        return (this.state.hasError) ? (
            <p>
                {this.state.error.toString()}
            </p>
        ) : (
            this.props.children
        )
    }
}

export default ErrorBoundry
