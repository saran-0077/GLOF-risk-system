"""
GLOF Risk Visualization with Elevation Contours (2024–25)

Author: Mirthesh M
Affiliation: B.E. AIML, Kings Engineering College
Project: GLOF Risk Prediction using ML (Landsat-8 + SRTM DEM)

Description:
- Loads predicted GLOF risk zones and elevation data.
- Reshapes them into a 2D spatial grid (43x54).
- Visualizes risk zones with custom colormap.
- Overlays topographic elevation contours for context.

Output:
- Heatmap showing Safe, Moderate, High Risk zones with elevation overlays.

GitHub: https://github.com/mirthesh1105
LinkedIn: www.linkedin.com/in/mirthesh-m-083971294
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# -------------------- Load Data -------------------- #
df = pd.read_csv("data/glof_risk_predictions_2024.csv")

# -------------------- Reshape to Grid -------------------- #
height, width = 43, 54  # Spatial grid dimensions (rows, cols)
risk_grid = df["Predicted_Risk"].values.reshape((height, width))
elevation_grid = df["Elevation"].values.reshape((height, width))

# -------------------- Define Risk Color Map -------------------- #
# 0: Safe, 1: Moderate, 2: High
cmap = ListedColormap(["#1f77b4", "#ff7f0e", "#d62728"])

# -------------------- Plot Risk Map -------------------- #
plt.figure(figsize=(10, 6))
im = plt.imshow(risk_grid, cmap=cmap)
cbar = plt.colorbar(im, ticks=[0, 1, 2])
cbar.ax.set_yticklabels(["Safe (0)", "Moderate (1)", "High (2)"])
cbar.set_label("Predicted GLOF Risk Level")

# -------------------- Add Elevation Contours -------------------- #
contour_levels = np.linspace(elevation_grid.min(), elevation_grid.max(), 10)
contours = plt.contour(elevation_grid, levels=contour_levels, colors='black', linewidths=0.5)
plt.clabel(contours, inline=True, fontsize=8)

# -------------------- Add Labels and Title -------------------- #
plt.title("Predicted GLOF Risk Map with Elevation Contours (2024–25)")
plt.xlabel("Pixel Column")
plt.ylabel("Pixel Row")
plt.tight_layout()
plt.show()
