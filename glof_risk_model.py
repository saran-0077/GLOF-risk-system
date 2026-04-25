"""
GLOF Risk Prediction Script
---------------------------
- Clusters 2023–24 feature data using KMeans
- Maps clusters to risk levels (safe, moderate, high)
- Trains a Random Forest classifier on 2023–24 labels
- Predicts GLOF risk levels for 2024–25 data

Author: Mirthesh M
"""

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import os

# ------------------------ Config ------------------------ #

features = ["NDWI", "NDVI", "NDSI", "Elevation", "Slope", "Aspect", "DistToGlacier"]
input_2023 = "data/glof_features_2023_24.csv"
input_2024 = "data/glof_features_2024_25.csv"
output_2024 = "output/glof_risk_predictions_2024_25.csv"

# ------------------ Load & Impute 2023 ------------------ #

df_2023 = pd.read_csv(input_2023)
imputer = SimpleImputer(strategy="mean")
X_2023 = imputer.fit_transform(df_2023[features])

# -------------------- Normalize ------------------------ #

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_2023)

# -------------------- Clustering ------------------------ #

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df_2023["Cluster"] = kmeans.fit_predict(X_scaled)

# ------------------ Cluster to Risk --------------------- #

# ⚠️ Update this if clustering result changes
cluster_to_risk = {
    0: 0,  # Safe
    1: 2,  # High Risk
    2: 1,  # Moderate
    3: 0,  # Safe Glacier
}

df_2023["Risk"] = df_2023["Cluster"].map(cluster_to_risk)

# ------------------ Train Classifier -------------------- #

X = df_2023[features].fillna(0)
y = df_2023["Risk"]
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# ------------------ Evaluation -------------------------- #

print("✅ Random Forest Evaluation:")
print(confusion_matrix(y_test, clf.predict(X_test)))
print(classification_report(y_test, clf.predict(X_test)))

# ------------------ Predict 2024–25 ---------------------- #

df_2024 = pd.read_csv(input_2024)
X_2024 = df_2024[features].fillna(0)
X_2024_scaled = scaler.transform(X_2024)

df_2024["Predicted_Risk"] = clf.predict(X_2024_scaled)

# ------------------ Save Results ------------------------ #

os.makedirs(os.path.dirname(output_2024), exist_ok=True)
df_2024.to_csv(output_2024, index=False)
print(f"🚀 Predicted risk zones saved to '{output_2024}'")
