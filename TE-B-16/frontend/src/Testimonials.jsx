import React from 'react';

function Testimonials() {
  return (
    <section className="testimonials">
      <h3>TESTINOMIALS</h3>
    <h2>What our Customers say</h2>
    
    <div className="testimonial-container">
      <div className="testimonial-card">
        <img src="gim1.png" alt="Naina" />
        <h3>Naina</h3>
        <p className="stars">★★★★★</p>
        <p>
          I was suffering from PCOS since 3 years, took treatment from Dr.
          Anjali and now I am much better than earlier. Very good services,
          satisfied with the app.
        </p>
      </div>
      <div className="testimonial-card">
        <img src="gim2.png" alt="Ritika" />
        <h3>Ritika</h3>
        <p className="stars">★★★★★</p>
        <p>
          Best app for everyone going through PCOS problems. Must try
          consulting the doctors. Happy with the service.
        </p>
      </div>
      <div className="testimonial-card">
        <img src="gim3.png" alt="Sania" />
        <h3>Sania</h3>
        <p className="stars">★★★★★</p>
        <p>
          Dr. Kumar is the best to consult. Amazing results in just 3 months!
        </p>
      </div>
    </div>
  </section>
  );
}

export default Testimonials;
