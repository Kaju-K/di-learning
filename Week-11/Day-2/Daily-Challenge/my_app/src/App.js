import './App.css';
import { useState } from 'react'
import Language from './components/Language';

function App() {
  const [php, setPhp] = useState({name: 'Php', count: 0})
  const [python, setPython] = useState({name: 'Python', count: 0})
  const [javascript, setJavascript] = useState({name: 'Javascript', count: 0})
  const [java, setJava] = useState({name: 'Java', count: 0})

  return (
    <div className="App">
      <h1>Vote Your Language!</h1>
      <Language info={php} setVote={setPhp} />
      <Language info={python} setVote={setPython} />
      <Language info={javascript} setVote={setJavascript} />
      <Language info={java} setVote={setJava} />
    </div>
  );
}

export default App;
