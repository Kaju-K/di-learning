import './App.css';
import BuggyCounter from './components/BuggyCounter'
import ColorClass from './components/ColorClass';
import ErrorBoundry from './ErrorBoundry'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h2>Together</h2>
        <ErrorBoundry>
          <BuggyCounter />
          <BuggyCounter />
        </ErrorBoundry>
        <hr style={{'width': '90%'}}/>
        <h2>Separeted</h2>
        <ErrorBoundry>
          <BuggyCounter/>
        </ErrorBoundry>
        <ErrorBoundry>
          <BuggyCounter/>
        </ErrorBoundry>
        <hr style={{'width': '90%'}}/>
        <h2>This one will crash everything</h2>
        <BuggyCounter />

        <ColorClass />
      </header>
    </div>
  );
}

export default App;
