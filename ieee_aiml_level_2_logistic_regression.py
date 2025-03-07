import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Load dataset
X_train, y_train = load_fashion_mnist()

# Preprocessing: Flatten images and normalize pixel values
X_train_flat = X_train.reshape(X_train.shape[0], -1).astype(np.float64)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_flat)

# Split dataset into train and test sets
X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(X_train_scaled, y_train, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_split, y_train_split)

# Predictions and evaluation
y_pred = model.predict(X_test_split)
accuracy = accuracy_score(y_test_split, y_pred)
print(f"Logistic Regression Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix visualization
cm = confusion_matrix(y_test_split, y_pred)
plt.figure(figsize=(10, 7))
plt.imshow(cm, cmap='Blues', interpolation='nearest')
plt.title('Confusion Matrix')
plt.colorbar()
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

# Feature Importance (coefficients)
importances = model.coef_[0]
plt.figure(figsize=(10, 7))
plt.bar(range(len(importances)), importances)
plt.title('Logistic Regression Feature Importance')
plt.show()
