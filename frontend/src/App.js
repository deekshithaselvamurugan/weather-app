import React, { useState } from 'react';
import './App.css';

function App() {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);

  const fetchWeather = async () => {
    const res = await fetch(`http://localhost/api/weather?city=${city}`);
    const data = await res.json();
    setWeather(data);
  };

  return (
    <div className="App">
      <h1>Weather App</h1>
      <input value={city} onChange={e => setCity(e.target.value)} placeholder="Enter city" />
      <button onClick={fetchWeather}>Get Weather</button>
      {weather && (
        <div>
          <h3>{weather.city}</h3>
          <p>{weather.temperature} °C</p>
          <p>{weather.description}</p>
        </div>
      )}
    </div>
  );
}

export default App;

