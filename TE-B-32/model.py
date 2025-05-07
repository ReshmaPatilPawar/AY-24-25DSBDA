# 📦 Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# 📁 Load Dataset
df = pd.read_csv('/content/drive/MyDrive/Mini_Project/mobile_phone_addiction_dataset.csv')
df.head()
df.tail()
df.shape
df.info()



# 🧼 Data Cleaning
print("Missing values:\n", df.isnull().sum())
df.dropna(inplace=True)  # Drop if any nulls

# 📊 EDA (Exploratory Data Analysis)
sns.histplot(df['screen_time_hrs_per_day'], kde=True)
plt.title('Screen Time Distribution')
plt.show()

sns.pairplot(df, hue='addicted')
plt.suptitle('Pairplot of Features vs Target', y=1.02)
plt.show()

# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# plt.title('Feature Correlation Heatmap')
# plt.show()

# 🎯 Features & Target
X = df[['screen_time_hrs_per_day', 'gaming_time', 'social_media_time', 'data_usage_gb_per_day']]
y = df['addicted']

# 🔀 Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🧠 Train Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# 🔎 Model Evaluation
y_pred = model.predict(X_test)

print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("✅ Classification Report:\n", classification_report(y_test, y_pred))

sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# 🔍 Feature Importance
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.sort_values().plot(kind='barh', color='skyblue')
plt.title('Feature Importances (Random Forest)')
plt.show()

# 💾 Save the model
joblib.dump(model, "random_forest_addiction_model.pkl")
print("🎉 Model saved as random_forest_addiction_model.pkl")
