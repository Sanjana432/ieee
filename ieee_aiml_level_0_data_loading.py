import numpy as np
import matplotlib.pyplot as plt
import gzip
import os

# Function to load the Fashion MNIST dataset
def load_fashion_mnist():
    # Load the dataset using the correct path
    dataset_path = 'path/to/fashion-mnist'

    with gzip.open(os.path.join(dataset_path, 'train-images-idx3-ubyte.gz'), 'rb') as f:
        X_train = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1, 28, 28)
    
    with gzip.open(os.path.join(dataset_path, 'train-labels-idx1-ubyte.gz'), 'rb') as f:
        y_train = np.frombuffer(f.read(), np.uint8, offset=8)

    return X_train, y_train

# Load the dataset
X_train, y_train = load_fashion_mnist()

# Print dataset shape
print(f"X_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")

# Display a few images with labels
fig, axes = plt.subplots(1, 5, figsize=(10, 5))
for i in range(5):
    axes[i].imshow(X_train[i], cmap='gray')
    axes[i].set_title(f"Label: {y_train[i]}")
    axes[i].axis('off')
plt.show()

# Check if the images are grayscale (28x28 pixel)
print(f"Shape of the first image: {X_train[0].shape}")
