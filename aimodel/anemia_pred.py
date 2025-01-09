import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
import pickle

# Suppress warnings
warnings.filterwarnings("ignore")

# Load the dataset
data = pd.read_csv(r"aimodel\Datasets\anemia.csv")

# Analyze data
# print("Dataset preview:")
# print(data.head())
# print("\nData grouped by 'Result':")
# print(data.groupby('Result').mean())

# Separate features and target
X = data.drop(columns='Result', axis=1)
Y = data['Result']

# Standardize the features
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)

X = standardized_data

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

# Train the SVM classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Model evaluation
# Predict on training data
train_predictions = classifier.predict(X_train)
train_accuracy = accuracy_score(Y_train, train_predictions)
print(f"Training Accuracy: {train_accuracy:.2f}")

# Predict on testing data
test_predictions = classifier.predict(X_test)
test_accuracy = accuracy_score(Y_test, test_predictions)
print(f"Testing Accuracy: {test_accuracy:.2f}")

# Classification report and confusion matrix
# print("\nClassification Report:")
# print(classification_report(Y_test, test_predictions))

# print("Confusion Matrix:")
# print(confusion_matrix(Y_test, test_predictions))

# Save the trained model
model_filename = "anemia_model.pkl"
with open(model_filename, 'wb') as file:
    pickle.dump(classifier, file)
# print(f"Model saved as '{model_filename}'")

# Save the scaler for future use
scaler_filename = "scaler.pkl"
with open(scaler_filename, 'wb') as file:
    pickle.dump(scaler, file)
# print(f"Scaler saved as '{scaler_filename}'")

# Load the model and scaler (example usage)
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

with open(scaler_filename, 'rb') as file:
    loaded_scaler = pickle.load(file)

# Example prediction with all features (5 features in the correct order)
sample_data = np.array([[1, 12.5, 4.3, 15.0, 85.0]])  # Replace with appropriate sample data

# Ensure the input shape matches (1, 5) for one sample with 5 features
sample_data_scaled = loaded_scaler.transform(sample_data)
sample_prediction = loaded_model.predict(sample_data_scaled)

if(sample_prediction[0] == 0):
  op="no anemia"
else:
  op="anemia"
print(op)