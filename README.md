
🌊 GLOF Risk Prediction and Visualization System
A comprehensive pipeline that extracts geospatial features from remote sensing data, classifies potential Glacial Lake Outburst Flood (GLOF) risk zones, and visualizes multi-class risk maps with elevation contours for real-world application and research.

📁 Project Structure
GLOF-Risk-System/
│
├── data/
│   ├── glof_features_enhanced_2023-24.csv
│   ├── glof_features_enhanced_2024-25.csv
│   ├── glof_risk_predictions_2024.csv
│
├── fetch_landsat_data.py           # Extracts Landsat & DEM features
├── glof_feature_extraction.py      # NDWI, NDVI, NDSI, slope, aspect, etc.
├── glof_risk_model.py              # Clustering + Random Forest prediction
├── glof_risk_visualization.py      # Elevation contour + Risk map plot
├── requirements.txt                # Project dependencies
├── README.md                       # Project overview and instructions
⚙️ How It Works
Fetch Landsat & DEM data
Extract geospatial features: NDWI, NDVI, NDSI, etc.
Apply KMeans clustering → Label risk levels
Train Random Forest classifier
Predict risk zones for next year
Visualize risk zones with elevation contours
📂 Data Sources
This project focuses on satellite and topographic data specific to the South Lhonak Lake (SLL) region.

Study Area: South Lhonak Lake, Sikkim, India (~27.95°N, 88.14°E)
Satellite Imagery: Landsat-8 Collection 1
DEM Data: SRTM 30m resolution (USGS)
🔍 Key Features
Feature Extraction: Computes NDWI, NDVI, NDSI, elevation, slope, aspect, and distance to glaciers from satellite and DEM data.
Clustering & Classification: Uses KMeans clustering to identify patterns and Random Forest for risk classification.
Visualization: Generates contour-overlaid risk maps using matplotlib and custom colormaps.
Scalability: Easily extendable to any year or region using Landsat & DEM inputs.
Research Oriented: Designed to contribute to scientific GLOF risk analysis and mapping.
🧪 Technologies Used
Python 3.10+
Pandas, NumPy
Matplotlib
Scikit-learn
GDAL / Rasterio (optional for preprocessing)
Jupyter / VSCode (for local development)
🚀 Getting Started
1. Clone the repository
git clone https://github.com/yourusername/GLOF-Risk-System.git
cd GLOF-Risk-System
2. Setup environment
pip install -r requirements.txt
3. Run the pipeline
1. Extract Features
From Landsat and DEM files:

python fetch_landsat_data.py
2. Generate Feature CSVs
Compute NDWI, NDVI, Elevation, etc:

python glof_feature_extraction.py
3. Train Risk Model
Clustering + Random Forest classification:

python glof_risk_model.py
4. Visualize Risk Zones
Overlay risk levels with elevation contours:

python glof_risk_visualization.py
📊 Sample Output
glof_risk_predictions_2024-25.csv: Contains predicted risk labels
Risk visualization (PNG/interactive): Displays areas as Safe, Moderate, or High Risk
📂 Data Sources
Landsat-8: https://earthexplorer.usgs.gov
DEM (SRTM/ASTER): https://search.earthdata.nasa.gov
Glacier outlines (RGI): https://www.glims.org/RGI
👤 Author
Mirthesh M
🎓 B.E. Artificial Intelligence and Machine Learning
🏫 Kings Engineering College
📧 mirtheshmurugaiah1105@gmail.com
🔗 LinkedIn | GitHub

🙏 Acknowledgements
Andrew Ng's Deep Learning Specialization for foundational ML and DL knowledge.
USGS EarthExplorer and NASA Earthdata for providing open-access remote sensing data.
RGI (Randolph Glacier Inventory) for glacier outline datasets.
Open-source Python community for powerful geospatial and machine learning libraries.
📄 License
This project currently has no license. As a result, all rights are reserved by the author.

If you'd like to use or adapt this work for academic, research, or commercial purposes, please contact the author for permission.

📧 mirtheshmurugaiah1105@gmail.com

📚 Citation
If you use this work in your research, please cite it as:

@misc{mirthesh2025glof,
  author       = {Mirthesh M},
  title        = {GLOF Risk Prediction and Visualization System},
  year         = {2025},
  url          = {https://github.com/mirthesh1105/GLOF-Risk-System},
  note         = {A geospatial machine learning pipeline for detecting and visualizing glacial lake outburst flood (GLOF) risks using Landsat, DEM, and Random Forest classification.}
}
🧠 Future Improvements
Incorporate Sentinel-2 bands for finer resolution
Use U-Net or ResNet models for pixel-level segmentation
Develop a web-based GLOF risk alert dashboard
