 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('churn_data.csv')

# Convert categorical variables to numerical
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})

# Select features and target
features = ['Age', 'Gender', 'Tenure', 'MonthlyCharges', 'TotalCharges']
X = df[features]
y = df['Churn']

# Handle missing values
X = X.fillna(X.mean())

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')

# Save model predictions
X_test['Predicted_Churn'] = y_pred
X_test.to_csv('churn_predictions.csv', index=False)
