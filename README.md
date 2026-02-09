# Trajectory Exposure Analysis - QGIS Plugin

A comprehensive QGIS plugin for analyzing GPS trajectories with air quality data, featuring time-weighted exposure metrics, dwell time analysis, and indoor/outdoor validation.

## Features

### 🎯 Core Capabilities
- **Multi-format Input Support**: Shapefile, GeoPackage, GeoJSON, KML, CSV
- **Dwell Time Analysis**: Automatic calculation of time spent at each location
- **Time-Weighted Exposure**: Accurate exposure metrics accounting for stationary vs. moving periods
- **Indoor/Outdoor Validation**: Using building footprints or OpenStreetMap data
- **Grid-Based Aggregation**: Spatial analysis with customizable cell sizes
- **Quality Assurance**: Teleport detection, speed filtering, coverage metrics

### 📊 Analysis Outputs
- **Person-Day-Cell Footprints**: Detailed exposure by individual, date, and grid cell
- **Person-Day Summaries**: Daily aggregated metrics per individual
- **Raster Grids**: GeoTIFF outputs for PM2.5, NO2, and dwell time
- **Multiple Export Formats**: GeoPackage, Shapefile, GeoJSON, CSV

### 🏢 Indoor/Outdoor Validation
- Upload custom building polygons
- Automatic OSM building fetch
- GPS drift compensation with buffer zones
- Confidence scoring for indoor classification

## Installation

### Requirements
- QGIS 3.16 or higher
- Python packages:
  - pandas
  - numpy
  - geopandas
  - pyproj
  - osmnx (optional, for OSM building fetching)

### Install Plugin

1. **Download** the plugin folder to your QGIS plugins directory:
   - Windows: `C:\Users\<username>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`

2. **Enable** the plugin in QGIS:
   - Go to `Plugins → Manage and Install Plugins`
   - Find "Trajectory Exposure Analysis"
   - Check the box to enable

3. **Install dependencies**:
   ```bash
   pip install pandas numpy geopandas pyproj
   pip install osmnx  # Optional, for OSM building fetching
   ```

## Usage

### 1. Access the Algorithm

Find the algorithms in QGIS Processing Toolbox under:
**Trajectory Exposure Analysis**

### 2. Prepare Input Data

#### Required Fields
Your trajectory data must include:
- **PID**: Person/Individual ID
- **date**: Timestamp (any datetime format)
- **lat**: Latitude (for CSV) or point geometry
- **lon**: Longitude (for CSV) or point geometry
- **pm25**: PM2.5 concentration (µg/m³)
- **no2**: NO2 concentration (µg/m³)

#### Supported Input Formats

**Vector Layers:**
- Shapefile (.shp)
- GeoPackage (.gpkg)
- GeoJSON (.geojson)
- KML (.kml)

**CSV Files:**
- Must include latitude and longitude columns
- Specify field names in the algorithm dialog
- Coordinate system: EPSG:4326 (default) or specify custom

### 3. Configure Parameters

#### Data Inputs
- **Input Data Type**: Vector layer or CSV file
- **Trajectory Layer/File**: Your trajectory data
- **Field Names**: Specify column names for PID, date, PM2.5, NO2
- **Boundary Layer** (optional): Polygon to filter analysis area
- **Building Footprints** (optional): For indoor/outdoor validation

#### Building Data Options
1. **Upload Shapefile**: Use custom building polygons
2. **Fetch from OSM**: Automatically download buildings
   - Set buffer distance (0.1 - 10 km)
   - Works globally

#### Analysis Parameters
- **Grid Cell Size**: 100 - 10,000 meters (default: 1,000m)
- **Max Dwell Time**: 1 - 120 minutes (default: 10 min)
- **Speed Threshold**: 50 - 500 km/h (default: 120 km/h)
- **Remove Teleports**: Flag to filter unrealistic speeds
- **Building Buffer**: 0 - 50 meters for GPS drift (default: 5m)
- **Exclude Indoor Points**: Option to remove indoor locations

#### Output Options
- **Vector Format**: GeoPackage, Shapefile, GeoJSON, or CSV
- **Person-Day-Cell Footprints**: Detailed grid-level data
- **Person-Day Summaries**: Daily aggregated metrics
- **PM2.5 Raster**: GeoTIFF grid
- **NO2 Raster**: GeoTIFF grid
- **Dwell Time Raster**: GeoTIFF grid

### 4. Run Analysis

1. Click **Run** in the algorithm dialog
2. Monitor progress in the log panel
3. Output layers automatically added to QGIS

### 5. Interpret Results

#### Person-Day-Cell Footprints
- Each record represents exposure in one grid cell on one day for one person
- **dwell_min**: Total time spent in cell (minutes)
- **pm25_tw**: Time-weighted average PM2.5 (µg/m³)
- **no2_tw**: Time-weighted average NO2 (µg/m³)
- **pct_indoor**: Percentage of time spent indoors

#### Person-Day Summaries
- Daily aggregated metrics per individual
- **dwell_day**: Total recorded time that day (minutes)
- **pm25_day**: Daily time-weighted PM2.5 exposure
- **no2_day**: Daily time-weighted NO2 exposure
- **n_cells**: Number of grid cells visited
- **coverage**: Proportion of 24 hours with data (0-1)

#### Raster Outputs
- Continuous surface maps in EPSG:6933 (World Equidistant Cylindrical)
- Cell size matches grid configuration
- NoData for cells without observations
- Can be visualized with graduated colors

## Dwell Time Methodology

The plugin calculates **dwell time** as the temporal duration between consecutive GPS points for the same individual:

1. **Time Difference**: Calculate seconds between point i and point i+1
2. **Speed Check**: Flag unrealistic speeds as teleports (optional removal)
3. **Day Boundary**: Reset dwell time at midnight (no cross-day spillover)
4. **Maximum Cap**: Limit dwell time to prevent gaps inflating exposure
5. **Weighting**: Multiply pollutant concentration by dwell time
6. **Aggregation**: Sum weighted exposures, divide by total dwell time

### Example Calculation

```
Point 1: 10:00 AM, PM2.5 = 25 µg/m³
Point 2: 10:05 AM, PM2.5 = 30 µg/m³ (5 min dwell at Point 1)
Point 3: 10:15 AM, PM2.5 = 20 µg/m³ (10 min dwell at Point 2)

Time-weighted average = (25×5 + 30×10) / (5+10) = 28.3 µg/m³
```

## Example Workflow

### Scenario: Urban Air Quality Study

**Goal**: Analyze pedestrian exposure to air pollution in city center

```python
# 1. Prepare trajectory data (CSV)
trajectories.csv:
PID,timestamp,lat,lon,pm25,no2
001,2026-01-15 09:00:00,40.7580,-73.9855,22.5,35.1
001,2026-01-15 09:05:00,40.7590,-73.9845,24.1,37.2
...

# 2. Run in QGIS Processing Toolbox
# Input: trajectories.csv
# Grid: 500m cells
# Buildings: Fetch from OSM (1km buffer)
# Building buffer: 5m
# Max dwell: 10 minutes

# 3. Outputs
# - footprints.gpkg: 15,000 person-day-cell records
# - summaries.gpkg: 500 person-day records  
# - pm25_grid.tif: Raster surface map
```

### Scenario: Multi-Country Analysis

**Goal**: Compare exposure across different cities

```python
# Trajectories from multiple countries
# Different CRS handled automatically
# Boundary layers to isolate each city
# Consistent grid size (1000m) for comparison

# Compare:
# - Average dwell time per cell
# - Exposure distributions
# - Indoor vs outdoor patterns
```

## Troubleshooting

### Common Issues

**"No valid trajectory data loaded"**
- Check field names match configuration
- Ensure date field is parseable datetime format
- Verify coordinates are valid (lat: -90 to 90, lon: -180 to 180)

**"OSMnx not installed"**
- Install: `pip install osmnx`
- Restart QGIS after installation
- Or provide custom building shapefile instead

**"Could not create output sink"**
- Check output path is writable
- Ensure sufficient disk space
- Try different output format

**Low coverage values**
- Normal if GPS tracking is intermittent
- Check max dwell time setting (may need adjustment)
- Review speed threshold (may be removing valid points)

### Performance Tips

- **Large datasets**: Increase grid cell size (2000-5000m)
- **Memory issues**: Process by subsets using boundary layers
- **OSM fetch slow**: Use smaller buffer or pre-download buildings
- **Raster export**: Skip if only need vector outputs

## Advanced Configuration

### Custom CRS
All analysis performed in EPSG:6933 (metric) for accurate distance calculations. Input data automatically reprojected.

### Field Mapping
Customize field names if your data uses different columns:
```
PID_FIELD: participant_id
DATE_FIELD: datetime_utc
PM25_FIELD: pm2p5_ugm3
NO2_FIELD: no2_ppb
```

### Batch Processing
Use QGIS Batch Processing to analyze multiple files:
1. Right-click algorithm → "Execute as Batch Process"
2. Add multiple trajectory files
3. Configure parameters once
4. Run all analyses

## Output Examples

### Visualization in QGIS

**Point Layer Styling** (Person-Day-Cell Footprints):
- Graduated symbols by `dwell_min`
- Color ramp by `pm25_tw`
- Size by `n_points`

**Raster Styling**:
- Singleband pseudocolor
- Red-Yellow-Green color ramp (inverted for pollution)
- Stretch: Min-Max or Custom breaks

**Temporal Animation**:
- Filter by date using temporal controller
- Animate exposure changes over time

## Citation

If you use this plugin in research, please cite:

```
[Your Citation Here]
CHEAQI Research Team (2026). 
Trajectory Exposure Analysis: A QGIS Plugin for Spatiotemporal Air Quality Exposure Assessment.
Version 1.0.0.
```

## Support

- **Issues**: [GitHub Issues](https://github.com/your-org/trajectory-exposure/issues)
- **Documentation**: [Full Documentation](https://github.com/your-org/trajectory-exposure)
- **Email**: support@cheaqi.org

## License

[Your License Here - e.g., MIT, GPL-3.0]

## Changelog

### Version 1.0.0 (2026-02-09)
- Initial release
- Multi-format input support
- Dwell time calculations
- Indoor/outdoor validation
- OSM building integration
- Multiple export formats
- Raster grid generation

## Contributors

CHEAQI Research Team
- [Your Names/Affiliations]

## Acknowledgments

Built using:
- QGIS Processing Framework
- GeoPandas for spatial operations
- OSMnx for OpenStreetMap integration
- Pandas/NumPy for data processing
