import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

function Banner() {
  const navigate = useNavigate(); // Initialize navigate hook

  const handleTakeTestClick = () => {
    navigate('/predict'); // Redirect to the Predict page
  };

  return (
    <section className="banner">
      <div className="banner-text">
        <br></br>
        <h4 className='font-mono text-xl text-gray-400'><b>#positivelyunashamed </b> that I have Pcos!</h4><br />
        <h1 className='font-mono font-extrabold text-5xl'>Let’s Fight Together with <br /><h2 className="highlight">PCOS</h2></h1><br />
        <button className="download-btn" onClick={handleTakeTestClick}>TAKE TEST</button>
      </div>
      <div className="banner-img">
        <img src="DOC.jpg" alt="Doctor consultation" style={{ height: '30%', width: '100%' }} />
      </div>
    </section>
  );
}

export default Banner;
