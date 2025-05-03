document.getElementById("predictForm").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const formData = new FormData(this);
  
    fetch("/predict", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert("Error: " + data.error);
        } else {
          // Display the predictions on the page
          document.getElementById("result").innerHTML = `
            <p><strong>Discount Prediction:</strong> ${data.discount_prediction}</p>
            <p><strong>Purchase Amount Prediction (USD):</strong> ${data.purchase_prediction}</p>
          `;
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
});
