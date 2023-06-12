import './App.css';

import CarClass from './components/CarClass'
import ClickMe from './components/ClickMe'
import ColorClass from './components/ColorClass';
import PhoneClass from './components/PhoneClass';

function App() {
  const carinfo = {name: "Ford", model: "Mustang"};

  return (
    <div className="App">
      <header>
        <CarClass info={carinfo} />
        <ClickMe />
        <PhoneClass />
        <ColorClass />
      </header>
    </div>
  );
}

export default App;
