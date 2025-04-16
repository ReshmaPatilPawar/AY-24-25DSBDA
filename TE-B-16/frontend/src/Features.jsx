import React from 'react';

function Features() {
  return (
    <section className="features">
      <h2>OUR FEATURES</h2>
      <div className="feature-box">
        <div className="features-grid">
          <div className="feature-item"><img src="pic1.png" alt="Doctor Consultation" onClick={() => window.open("https://www.mayoclinic.org/diseases-conditions/pcos/care-at-mayo-clinic/mac-20353446", "_blank")}/></div>
          <div className="feature-item"><img src="pic2.png" alt="Buy Medicines" onClick={() => window.open("https://www.nichd.nih.gov/health/topics/pcos", "_blank")} /></div>
          <div className="feature-item"><img src="pic3.png" alt="Keep Records" onClick={() => window.open("https://www.nhs.uk/conditions/polycystic-ovary-syndrome-pcos/", "_blank")}/></div>
          <div className="feature-item"><img src="pic4.png" alt="Lab Test Booking" onClick={() => window.open("https://www.acog.org/womens-health/faqs/polycystic-ovary-syndrome-pcos", "_blank")} /></div>
          <div className="feature-item"><img src="pic5.png" alt="Diet & Exercise"onClick={() => window.open("https://www.endocrine.org/patient-engagement/endocrine-library/pcos", "_blank")} /></div>
          <div className="feature-item"><img src="pic6.png" alt="Pcos Community" onClick={() => window.open("https://www.nichd.nih.gov/health/topics/pcos", "_blank")}/></div>
        </div>
      </div>
    </section>
  );
}

export default Features;
