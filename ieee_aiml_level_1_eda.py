import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Load Fashion MNIST dataset
X_train, y_train = load_fashion_mnist()

# Display sample images from each category
categories = np.unique(y_train)
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, category in enumerate(categories[:10]):
    idx = np.where(y_train == category)[0][0]  # Find one image per category
    axes[i // 5, i % 5].imshow(X_train[idx], cmap='gray')
    axes[i // 5, i % 5].set_title(f"Category {category}")
    axes[i // 5, i % 5].axis('off')
plt.show()

# Summary statistics for pixel values
pixel_values = X_train.flatten()
print("Summary statistics for pixel values:")
print(f"Min: {pixel_values.min()}, Max: {pixel_values.max()}, Mean: {pixel_values.mean()}, Std: {pixel_values.std()}")

# Class distribution
class_counts = Counter(y_train)
print("Class distribution:")
for category, count in class_counts.items():
    print(f"Category {category}: {count} samples")
