import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
import warnings

warnings.filterwarnings('ignore')

# Load dataset
dataset = pd.read_csv("aimodel\Datasets\heart.csv")

# Check dataset info
# print(dataset.info())

# Split predictors and target
predictors = dataset.drop("target", axis=1)
target = dataset["target"]

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(predictors, target, test_size=0.20, random_state=42)

# Random Forest Classifier
rf = RandomForestClassifier(random_state=42, n_estimators=100)
rf.fit(X_train, Y_train)
Y_pred_rf = rf.predict(X_test)

# Accuracy
score_rf = round(accuracy_score(Y_pred_rf, Y_test) * 100, 2)
# print(f"The accuracy score achieved using Random Forest is: {score_rf} %")

# Classification Report
# print(classification_report(Y_test, Y_pred_rf))

# Feature Importance
feature_importances = rf.feature_importances_
features = predictors.columns
importance_df = pd.DataFrame({"Feature": features, "Importance": feature_importances}).sort_values(by="Importance", ascending=False)

# Example Prediction
# Create a hypothetical input (all features must be included in the correct order)
example_input = np.array([63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]).reshape(1, -1)

# Predict using the model
example_prediction = rf.predict(example_input)
example_proba = rf.predict_proba(example_input)

if(example_prediction==1):
    print("Heart disease")

else:
    print("no Heart disease")

