import React from 'react';

const ArticlesPage = () => {
  const articles = [
    {
      title: 'Understanding PCOS: What You Need to Know',
      link: 'https://www.womenshealth.gov/a-z-topics/polycystic-ovary-syndrome',
      description: 'Learn the basics of PCOS, its causes, and its symptoms.',
    },
    {
      title: 'PCOS and Fertility: What You Should Know',
      link: 'https://www.healthline.com/health/pcos-and-fertility',
      description: 'Explore the connection between PCOS and fertility issues.',
    },
    {
      title: 'Managing PCOS: Lifestyle Changes that Help',
      link: 'https://www.nhs.uk/conditions/polycystic-ovary-syndrome-pcos/living-with/',
      description: 'Discover lifestyle changes that can help manage PCOS symptoms.',
    },
    {
      title: 'The Role of Nutrition in Managing PCOS',
      link: 'https://www.medicalnewstoday.com/articles/pcos-and-diet',
      description: 'Understand how nutrition plays a key role in managing PCOS.',
    },
    {
      title: 'Emotional Support for Women with PCOS',
      link: 'https://www.pcosaa.org/mental-health-and-pcos',
      description: 'Find emotional support and coping strategies for dealing with PCOS.',
    },
  ];

  return (
    <div className="max-w-screen-xl mx-auto flex flex-col items-center justify-center text-center text-white">
      <section className="mb-24 flex-1 p-8 items-center justify-center align-middle">
        <h1 className="text-4xl font-semibold text-pink-500 mb-8">Articles on PCOS</h1>
        <p className="text-lg leading-relaxed max-w-3xl mx-auto text-gray-800 mb-8">
          Here are some helpful articles on PCOS that provide insights into the condition and how to manage it:
        </p>

        {articles.map((article, index) => (
          <div key={index} className="mb-16">
            <h2 className="text-3xl font-semibold text-yellow-500 mb-4">{article.title}</h2>
            <p className="text-lg leading-relaxed max-w-3xl mx-auto text-gray-800 mb-4">
              {article.description}
            </p>
            <a
              href={article.link}
              className="inline-block text-lg text-white bg-pink-500 hover:bg-pink-600 py-2 px-6 rounded-lg transition-all duration-300 ease-in-out transform hover:scale-105 mb-8"
              target="_blank"
              rel="noopener noreferrer"
            >
              Read More
            </a>

            <div className="mt-8 flex justify-center">
              <img
                className="w-48 h-48 rounded-full shadow-xl"
                src="https://i.pinimg.com/736x/6e/20/f2/6e20f2f3cd78048b3f426917943fcaed.jpg"
                alt={`Image for ${article.title}`}
              />
            </div>
          </div>
        ))}
      </section>

      <footer className="mt-24 text-center text-gray-600">
        <p>&copy; 2025 Neural Nurture | All Rights Reserved</p>
      </footer>
    </div>
  );
};

export default ArticlesPage;
