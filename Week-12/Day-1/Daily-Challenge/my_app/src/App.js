import './App.css';

import MovieList from './components/MovieList';
import Movie from './components/Movie';

function App() {
  
  return (
    <div className="App">
      <header className="App-header">
        <div>
          <h1>Redux Movies</h1>
          <div style={{display: 'flex', gap:'4rem', textAlign: 'start'}}>
            <MovieList />
            <Movie />
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
