import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings

warnings.filterwarnings("ignore")

# Load dataset
# Replace 'kidney_stone.csv' with the actual file path if it's a CSV file.
data = pd.read_csv('/content/kidney-stone-dataset.csv')

# Remove the first column
data = data.iloc[:, 1:]

# Separate features (X) and target (Y)
X = data.drop(columns='target', axis=1)
Y = data['target']

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fit(X_train, Y_train)

# Evaluate the model
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
# print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
# print("\nClassification Report:\n", classification_report(Y_test, Y_pred))
# print("\nConfusion Matrix:\n", confusion_matrix(Y_test, Y_pred))

# Example prediction
# Replace with actual sample data, matching the number of features in the dataset
# Example: [gravity, ph, osmo, cond, urea, calc] - Ensure all features are included
example_input = np.array([1.017, 5.74, 577, 20.0, 296, 4.49]).reshape(1, -1)

# Standardize the sample input using the same scaler
standardized_input = scaler.transform(example_input)

# Predict using the trained model
prediction = model.predict(standardized_input)

# Output the result
print("\nExample Prediction:")
# print(f"Input: {example_input.flatten()}")
if(prediction[0]==1):
  print("Kidney Stone ")
else:
  print("No Kidney Stone ")
# print(f"Predicted Target: {prediction[0]} (1 = Kidney Stone, 0 = No Kidney Stone)")