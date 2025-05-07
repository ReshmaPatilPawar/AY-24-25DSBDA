document.getElementById("predictForm").addEventListener("submit", async (e) => {
    e.preventDefault();
  
    const form = e.target;
    const data = {
      genre: form.genre.value,
      director: form.director.value,
      budget: Number(form.budget.value),
      year: Number(form.year.value),
      runtime: Number(form.runtime.value)
    };
  
    const resultBox = document.getElementById("result");
    resultBox.innerText = "Predicting...";
    resultBox.style.opacity = "0.5";
  
    try {
      const res = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
      });
  
      const result = await res.json();
      resultBox.innerText = `⭐ Predicted IMDb Rating: ${result.predicted_rating}`;
      resultBox.style.opacity = "1";
    } catch (error) {
      resultBox.innerText = "❌ Error occurred while predicting.";
      resultBox.style.opacity = "1";
    }
  });
  