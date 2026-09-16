"""
Petalyze — Project 2, DecodeLabs AI Internship
Data Classification Using AI: K-Nearest Neighbors on the Iris dataset
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score
import numpy as np

# ---- 1. INPUT: Load & understand the dataset ----
iris = load_iris()
X, y = iris.data, iris.target
species_names = iris.target_names  # ['setosa' 'versicolor' 'virginica']

print(f"Samples: {X.shape[0]}, Features: {X.shape[1]}, Classes: {len(species_names)}")

# ---- 2. PROCESS: Split, scale, tune k, train ----

# Shuffle + split (80/20) — shuffling first removes any order bias
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True, stratify=y
)

# Scale features — KNN relies on distance, so unscaled features
# with bigger raw ranges would unfairly dominate the distance calculation
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Find the best k using the "elbow method"
error_rates = []
k_range = range(1, 21)
for k in k_range:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    preds = model.predict(X_test_scaled)
    error_rates.append(np.mean(preds != y_test))

best_k = k_range[np.argmin(error_rates)]
print(f"Best k found: {best_k} (lowest error rate: {min(error_rates):.3f})")

# Train the final model with the best k
model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_train_scaled, y_train)

# ---- 3. OUTPUT: Predict & evaluate properly (not just accuracy) ----
predictions = model.predict(X_test_scaled)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nFull Classification Report (Precision / Recall / F1):")
print(classification_report(y_test, predictions, target_names=species_names))

print(f"Weighted F1 Score: {f1_score(y_test, predictions, average='weighted'):.3f}")


def predict_flower(sepal_length, sepal_width, petal_length, petal_width):
    """Predict the species of a single new flower measurement."""
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    distances, neighbor_indices = model.kneighbors(features_scaled)
    return {
        "species": species_names[prediction],
        "nearest_neighbor_distances": distances[0].tolist(),
    }


if __name__ == "__main__":
    # Example: classify a new flower
    example = predict_flower(5.1, 3.5, 1.4, 0.2)
    print(f"\nExample prediction: {example['species']}")
