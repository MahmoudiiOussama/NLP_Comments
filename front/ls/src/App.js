import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [inputText, setInputText] = useState('');
  const [predictions, setPredictions] = useState([]);

  const handlePrediction = async () => {
    try {
      const response = await axios.post('http://localhost:5000/prediction', { data: inputText });
      setPredictions(response.data);
    } catch (error) {
      console.error('Error fetching predictions:', error);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />
      <button onClick={handlePrediction}>Predict</button>
      <ul>
        {predictions.map((prediction, index) => (
          <li key={index}>
            Label: {prediction.label}, Prediction: {prediction.prediction}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
