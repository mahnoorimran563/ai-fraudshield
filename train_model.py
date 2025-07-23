import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
credit_card_data = pd.read_csv('credit_data.csv')

# Split into legit and fraud
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]
legit_sample = legit.sample(n=492)

# Combine
new_dataset = pd.concat([legit_sample, fraud], axis=0)

X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']

# Train/test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Save model
joblib.dump(model, 'fraud_model.pkl')

# Accuracy
print("Training Accuracy:", accuracy_score(Y_train, model.predict(X_train)))
print("Testing Accuracy:", accuracy_score(Y_test, model.predict(X_test)))
