"""
Fetch Landsat and DEM Data Script
---------------------------------
- Initializes Google Earth Engine
- Downloads Landsat 8 satellite images for specified region and date range
- Exports image to Google Drive for further processing

Author: Mirthesh M
"""

import ee

# Initialize Google Earth Engine
ee.Initialize(project="your_project_name") # Replace "your-project-id" with your own GEE project ID or use ee.Authenticate() for user-level access

# Define the region (South Lhonak Lake bounding box)
region = ee.Geometry.Rectangle([
    [88.180596, 27.904521],  # Bottom-left corner (Lon, Lat)
    [88.210465, 27.921510]   # Top-right corner (Lon, Lat)
])

# Load Landsat 8 Collection, Filter by Date & Bounds
landsat = (ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA")
           .filterBounds(region)
           .filterDate("2021-01-01", "2021-01-31")  # Adjust date range as needed
           .sort("CLOUD_COVER")  # Sort by least cloud cover
           .first()
           .toFloat())  # Get the least cloudy image

# Export Landsat Image to Google Drive
task = ee.batch.Export.image.toDrive(
    image=landsat,
    description="South_Lhonak_Lake_Landsat",
    folder="GEE_Exports",
    fileNamePrefix="south_lhonak_lake_Jan_2021",
    scale=30,
    region=region.getInfo()["coordinates"],  # Ensure proper format
    maxPixels=1e13
)

task.start()
print("Export started... Check your Google Drive for the image.")
print(task.status())



