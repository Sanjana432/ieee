import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load Fashion MNIST dataset
X_train, y_train = load_fashion_mnist()

# Preprocessing: Flatten images and normalize pixel values
X_train_flat = X_train.reshape(X_train.shape[0], -1).astype(np.float32) / 255
y_train_cat = to_categorical(y_train, 10)  # One-hot encode labels

# Split dataset into train and validation sets
X_train_split, X_val_split, y_train_split, y_val_split = train_test_split(X_train_flat, y_train_cat, test_size=0.2, random_state=42)

# Build a simple neural network model
model = Sequential([
    Flatten(input_shape=(28 * 28,)),  # Flatten input layer
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train_split, y_train_split, epochs=10, batch_size=64, validation_data=(X_val_split, y_val_split))

# Plot training and validation accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Evaluate the model on the validation set
val_loss, val_accuracy = model.evaluate(X_val_split, y_val_split)
print(f"Validation Accuracy: {val_accuracy * 100:.2f}%")
