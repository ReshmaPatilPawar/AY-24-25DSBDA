```python
import joblib
from sklearn.linear_model import LinearRegression

# your trained a Linear Regression model
linear_regressor = LinearRegression()  # Initialize model
linear_regressor.fit(X_train, y_train)  # Train the model (make sure X_train & y_train are defined)

# Saving the trained model
model_filename = "model.sav"
joblib.dump(linear_regressor, model_filename)

print(f"Linear Regression model saved as {model_filename}")
```
https://pcos-prediction-backend.onrender.com/
