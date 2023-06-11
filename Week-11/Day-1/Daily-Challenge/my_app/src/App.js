import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from 'react-responsive-carousel';

import './App.css'

function App() {
  return (
    <div className="carousel-container">
      <Carousel>
          <div>
              <img src="/Hong_Kong.jpg" alt="Hong Kong" />
              <p className="legend">Hong Kong</p>
          </div>
          <div>
              <img src="/Macao.jpg" alt="Macao" />
              <p className="legend">Macao</p>
          </div>
          <div>
              <img src="/Japan.jpg" alt="Japan" />
              <p className="legend">Japan</p>
          </div>
          <div>
              <img src="/Las_Vegas.jpg" alt="Las Vegas" />
              <p className="legend">Las Vegas</p>
          </div>
      </Carousel>
    </div>
  );
}

export default App;
