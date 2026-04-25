"""
GLOF Feature Extraction Script
------------------------------
Extracts geospatial features from Landsat 8 and DEM data for GLOF risk modeling:
- NDWI, NDVI, NDSI
- Elevation, Slope, Aspect
- Distance to Glacier

Author: Mirthesh M
"""

import rasterio
import numpy as np
import pandas as pd
from rasterio.warp import reproject, Resampling
from scipy.ndimage import sobel, distance_transform_edt
import os

# ----------------------------- CONFIG ----------------------------- #

# Input file paths (update as needed)
landsat_path = "data/landsat_image.tif"
dem_path = "data/SRTM_DEM.tif"

# Output file
output_csv = "output/glof_features_2024_25.csv"

# ----------------------- Load Landsat Bands ------------------------ #

with rasterio.open(landsat_path) as src:
    blue = src.read(2).astype(np.float32)
    green = src.read(3).astype(np.float32)
    red = src.read(4).astype(np.float32)
    nir = src.read(5).astype(np.float32)
    swir1 = src.read(6).astype(np.float32)
    swir2 = src.read(7).astype(np.float32)

    landsat_shape = (src.height, src.width)
    landsat_transform = src.transform
    landsat_crs = src.crs

# ------------------------- Spectral Indices ------------------------ #

with np.errstate(divide="ignore", invalid="ignore"):
    ndwi = np.where((green + nir) == 0, 0, (green - nir) / (green + nir))
    ndvi = np.where((nir + red) == 0, 0, (nir - red) / (nir + red))
    ndsi = np.where((green + swir1) == 0, 0, (green - swir1) / (green + swir1))

# ------------------------ Load & Align DEM ------------------------ #

print("🔄 Loading and resampling DEM to match Landsat resolution...")

with rasterio.open(dem_path) as dem_src:
    dem_data = dem_src.read(1).astype(np.float32)
    dem_resampled = np.empty(landsat_shape, dtype=np.float32)

    reproject(
        source=dem_data,
        destination=dem_resampled,
        src_transform=dem_src.transform,
        src_crs=dem_src.crs,
        dst_transform=landsat_transform,
        dst_crs=landsat_crs,
        resampling=Resampling.bilinear
    )

# ---------------------- Terrain Derivatives ------------------------ #

sx = sobel(dem_resampled, axis=1)
sy = sobel(dem_resampled, axis=0)
slope = np.hypot(sx, sy)
aspect = np.arctan2(sy, sx)

# ------------------------ Glacier Proximity ------------------------ #

glacier_mask = ndsi > 0.4
inv_mask = ~glacier_mask

if np.any(glacier_mask):
    distance_to_glacier = distance_transform_edt(inv_mask)
else:
    distance_to_glacier = np.full(landsat_shape, np.nan)

# ---------------------- Compile Features --------------------------- #

pixels = np.column_stack((
    ndwi.flatten(),
    ndvi.flatten(),
    ndsi.flatten(),
    dem_resampled.flatten(),
    slope.flatten(),
    aspect.flatten(),
    distance_to_glacier.flatten()
))

columns = ["NDWI", "NDVI", "NDSI", "Elevation", "Slope", "Aspect", "DistToGlacier"]
df = pd.DataFrame(pixels, columns=columns)

# ------------------------- Save to CSV ----------------------------- #

os.makedirs(os.path.dirname(output_csv), exist_ok=True)
df.to_csv(output_csv, index=False)
print(f"✅ Feature dataset saved to '{output_csv}' 🚀")
