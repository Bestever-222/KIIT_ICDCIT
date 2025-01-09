import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report
import warnings
import pickle

warnings.filterwarnings("ignore")

# Load the dataset
data = pd.read_csv("aimodel\Datasets\diabetes.csv")

# Display group statistics
# print("Mean values grouped by Outcome:\n", data.groupby('Outcome').mean())

# Separate features and target
X = data.drop(columns='Outcome', axis=1)
Y = data['Outcome']

# Standardize the data
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)

# Update features with standardized data
X = standardized_data

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

# Train the SVM classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Evaluate the model
Y_pred = classifier.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
# print(f"Model accuracy: {accuracy * 100:.2f}%")

# Classification report
# print("\nClassification Report:\n", classification_report(Y_test, Y_pred))

# Save the trained model
with open("svm_diabetes_model.pkl", "wb") as model_file:
    pickle.dump(classifier, model_file)

# Load the model (for demonstration purposes)
with open("svm_diabetes_model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)

# Example prediction
# Sample input (ensure the values are in the same order as the dataset features)
sample_input = np.array([5, 166, 72, 19, 175, 25.8, 0.587, 51]).reshape(1, -1)

# Standardize the sample input using the same scaler
standardized_sample = scaler.transform(sample_input)

# Predict using the loaded model
sample_prediction = loaded_model.predict(standardized_sample)

# Output the result
print("\nSample Input Prediction:")
# print(f"Input: {sample_input.flatten()}")
if(sample_prediction[0]==1):
    print("Diabetic")
else:
    print("no Diabetic")
# print(f"Predicted Outcome: {sample_prediction[0]} (1 = Diabetic, 0 = Non-Diabetic)")
