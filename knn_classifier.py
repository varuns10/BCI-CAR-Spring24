import pandas as pd
from scipy import stats
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

# Correct the file path and delimiter according to the image provided
df = pd.read_csv('/Users/varunsharma/Desktop/BCI_Car/BCI-CAR-Spring24/final_compiled.csv', delimiter=',')

# Assuming the last column is the target 'y' and the rest are features 'X'
X = df.iloc[:, :-1].values  # All columns except the last one
y = df.iloc[:, -1].values   # The last column

# Convert the 'y' values to a numeric representation (classification)
# Since 'y' appears to be categorical with values like 'down', we need to encode these labels.
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Standardize features to have mean=0 and variance=1
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the KNN classifier with distance weights
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')

# Train the KNN on the scaled training data
knn.fit(X_train_scaled, y_train)

# Predict on the scaled test data
y_pred = knn.predict(X_test_scaled)

# Evaluate the KNN's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# K-fold Cross Validation
k = 10
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import make_pipeline

# Use stratified K-fold to maintain the distribution of classes in each fold
strat_k_fold = StratifiedKFold(n_splits=k, shuffle=True, random_state=42)

# Create a pipeline that scales the data and then applies KNN
pipeline = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5, weights='distance'))

# Perform cross-validation using the pipeline
scores = cross_val_score(pipeline, X, y_encoded, cv=strat_k_fold, scoring='accuracy')

# Print the accuracy scores for each fold
for i, score in enumerate(scores):
    print(f"Fold {i + 1} Accuracy: {score:.2f}")

# Calculate and print the mean accuracy across all folds
mean_accuracy = scores.mean()
print(f"Mean Accuracy: {mean_accuracy:.2f}")
