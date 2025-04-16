import React from 'react';

const About = () => {
  return (
    <div className="max-w-screen-xl mx-auto flex flex-col items-center justify-center text-center text-white">
        <br></br>
        <br></br>
      <section className="mb-24 flex-1 p-8 items-center justify-center align-middle">
        <h1 className="text-4xl font-semibold text-pink-500 mb-8">What is PCOS?</h1> <br></br>
        <p className="text-lg leading-relaxed max-w-3xl mx-auto text-gray-800">
          Polycystic Ovary Syndrome (PCOS) is one of the most common hormonal disorders among women of reproductive age. It affects millions of women worldwide and can lead to irregular periods, difficulty getting pregnant, and other health issues. However, many women remain undiagnosed or struggle to manage the condition effectively, making it important to spread awareness and offer better solutions.
        </p>
      </section>
      <br></br> <br></br> <br></br>
      <section className="mb-24 flex-1">
        <h2 className="text-3xl font-semibold text-yellow-500 mb-8 py-4">How PCOS Affects Women</h2> <br></br>
        <p className="text-lg leading-relaxed max-w-3xl mx-auto text-gray-800 mb-8">
          PCOS can affect a woman's body in many ways. Here are some of the most common symptoms:
        </p>
        <ul className="text-lg list-disc list-inside max-w-3xl mx-auto text-gray-800 space-y-6">
          <li>Irregular periods or no periods at all</li>
          <li>Excess androgen (male hormone) levels, which can lead to symptoms like acne, facial hair growth, and male pattern baldness</li>
          <li>Weight gain or difficulty losing weight</li>
          <li>Ovulation problems, which can make it difficult to get pregnant</li>
          <li>Skin problems, such as oily skin or acanthosis nigricans (dark, velvety patches of skin on the back of the neck, armpits, or groin)</li>
          <li>Sleep apnea</li>
          <li>Mood swings and depression</li>
        </ul>
        <div className="mt-8 flex justify-center">
          <img
            className="w-48 h-48 rounded-full shadow-xl"
            src="https://i.pinimg.com/736x/6e/20/f2/6e20f2f3cd78048b3f426917943fcaed.jpg"
            alt="PCOS effects illustration"
          />
        </div>
      </section>
      <br></br> <br></br> <br></br>

      <section className="mb-24 flex-1">
        <h2 className="text-3xl font-semibold text-yellow-500 mb-8">What We Offer</h2> <br></br>
        <p className="text-lg leading-relaxed max-w-3xl mx-auto text-gray-800 mb-8">
          Saheli is designed to empower women with knowledge and support. We provide:
        </p>
        <ul className="text-lg list-disc list-inside max-w-3xl mx-auto text-gray-800 space-y-6">
          <li>Personalized health insights based on your symptoms and history.</li>
          <li>Guidance on lifestyle changes to manage PCOS effectively.</li>
          <li>Emotional support through our friendly AI assistant.</li>
        </ul>
        <div className="mt-8 flex justify-center">
          <img
            className="w-48 h-48 rounded-full shadow-xl"
            src="https://i.pinimg.com/736x/64/8d/6c/648d6c72f509f1b2648dc7872fa296d8.jpg"
            alt="What we offer illustration"
          />
        </div>
      </section>
      <br></br>
      <br></br>
      <br></br>

      <section className="mb-24 flex-1">
        <h2 className="text-3xl font-semibold text-purple-600 mb-8">Prediction & Chatbot Feature</h2> <br></br>
        <p className="text-lg leading-relaxed max-w-3xl mx-auto text-gray-800 mb-8">
          Our advanced Machine Learning model analyzes historical data to predict PCOS and guide you on effective management techniques. Additionally, the IBM Watson-powered AI Assistant, Saheli, is here to provide emotional support and personalized care plans. Whether you need advice or a comforting chat, Saheli is always by your side!
        </p>
        <div className="flex justify-center">
          <img
            className="w-48 h-48 rounded-full shadow-xl"
            src="https://i.pinimg.com/736x/0f/01/6f/0f016f14d1129070288cf37f8fef31ff.jpg"
            alt="Prediction and chatbot illustration"
          />
        </div>
      </section>
      <br></br> <br></br> <br></br>

      <section className="flex-1 mb-24">
        <h2 className="text-3xl font-semibold text-blue-500 mb-8">Our Mission</h2> <br></br>
        <p className="text-lg leading-relaxed max-w-3xl mx-auto text-gray-800">
          Our mission is simple: "A healthy woman is a powerful woman." At Saheli, we strive to provide women with the care, knowledge, and support they need to manage PCOS. We believe that by empowering women, we can help them lead healthier, happier lives—because every woman deserves the best version of herself.
        </p>
      </section>
      <br></br> <br></br> <br></br>

      <footer className="mt-24 text-center text-gray-600">
        <p>&copy; 2025 Neural Nurture | All Rights Reserved</p>
      </footer>
    </div>
  );
};

export default About;
