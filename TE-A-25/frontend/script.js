document.getElementById("ratingForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const data = {
        online_order: document.getElementById("online_order").value,
        book_table: document.getElementById("book_table").value,
        location: document.getElementById("location").value,
        rest_type: document.getElementById("rest_type").value,
        cuisines: document.getElementById("cuisines").value,
        cost: document.getElementById("cost").value,
        listed_in: document.getElementById("listed_in").value,
        votes: document.getElementById("votes").value
    };

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        document.getElementById("result").innerText = "⭐ Predicted Rating: " + result.predicted_rating;
    })
    .catch(err => {
        document.getElementById("result").innerText = "❌ Error: Unable to fetch prediction";
        console.error("Error:", err);
    });
});
