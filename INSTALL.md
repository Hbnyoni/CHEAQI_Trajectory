# Installation Guide - Trajectory Exposure Analysis QGIS Plugin

## Quick Install

### Step 1: Install Python Dependencies

Open OSGeo4W Shell (Windows) or Terminal (Mac/Linux) and run:

```bash
# Required packages
python3 -m pip install pandas numpy geopandas pyproj

# Optional (for OSM building fetching)
python3 -m pip install osmnx
```

**Windows Users**: Use the "OSGeo4W Shell" that comes with QGIS, not regular Command Prompt.

**Mac Users**: May need to use the QGIS Python environment:
```bash
/Applications/QGIS.app/Contents/MacOS/bin/python3 -m pip install pandas numpy geopandas pyproj osmnx
```

### Step 2: Copy Plugin Files

1. Locate your QGIS plugins directory:
   - **Windows**: `C:\Users\<username>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`

2. Copy the entire `trajectory_exposure_qgis_plugin` folder to the plugins directory

3. The final structure should look like:
   ```
   plugins/
   └── trajectory_exposure_qgis_plugin/
       ├── __init__.py
       ├── metadata.txt
       ├── trajectory_exposure_plugin.py
       ├── processing_provider.py
       ├── algorithms/
       │   ├── __init__.py
       │   ├── trajectory_analysis_algorithm.py
       │   └── osm_building_fetcher.py
       ├── README.md
       └── INSTALL.md
   ```

### Step 3: Enable Plugin in QGIS

1. Open QGIS
2. Go to **Plugins → Manage and Install Plugins**
3. Click on **Installed** tab
4. Find **Trajectory Exposure Analysis**
5. Check the box next to it to enable
6. Click **Close**

### Step 4: Verify Installation

1. Open **Processing → Toolbox** (or press `Ctrl+Alt+T`)
2. Look for **Trajectory Exposure Analysis** group
3. You should see:
   - Trajectory Exposure Analysis (Multi-Format)
   - Fetch Buildings from OpenStreetMap

If you see these algorithms, installation is complete! ✓

## Troubleshooting

### Plugin doesn't appear in list

**Solution 1**: Check folder name
- Must be exactly: `trajectory_exposure_qgis_plugin`
- No spaces, no capital letters

**Solution 2**: Check file permissions
- Ensure files are readable
- On Linux/Mac: `chmod -R 755 trajectory_exposure_qgis_plugin`

**Solution 3**: Restart QGIS
- Close QGIS completely
- Reopen and check again

### "No module named pandas" error

**Solution**: Install packages in QGIS Python environment

**Windows**:
```bash
# Open OSGeo4W Shell (comes with QGIS)
python3 -m pip install pandas numpy geopandas pyproj
```

**macOS**:
```bash
# Use QGIS Python
/Applications/QGIS.app/Contents/MacOS/bin/python3 -m pip install pandas numpy geopandas pyproj
```

**Linux**:
```bash
# Use system Python 3 or QGIS Python
python3 -m pip install pandas numpy geopandas pyproj
```

### "No module named osmnx" warning

This is **optional**. OSMnx is only needed if you want to fetch buildings from OpenStreetMap automatically.

**To install**:
```bash
python3 -m pip install osmnx
```

**Alternative**: Upload your own building shapefile instead.

### Algorithm fails with "GDAL not found"

**Solution**: GDAL should come with QGIS. If missing:

**Windows**: Reinstall QGIS from OSGeo4W installer
**macOS**: Reinstall QGIS from official installer
**Linux**: Install via package manager:
```bash
sudo apt-get install python3-gdal  # Debian/Ubuntu
sudo yum install python3-gdal      # RedHat/Fedora
```

### "Could not load provider" error

**Solution**: Check metadata.txt format
- Ensure no extra spaces or special characters
- Verify all required fields present

### Performance issues with large datasets

**Solutions**:
1. Increase grid cell size (2000-5000m)
2. Process by subsets using boundary layers
3. Use more powerful computer or process smaller batches
4. Skip raster outputs if not needed

## Manual Installation (ZIP Method)

If you downloaded a ZIP file:

1. **Extract** the ZIP file
2. **Rename** folder to `trajectory_exposure_qgis_plugin` (no spaces)
3. **Copy** to plugins directory (see Step 2 above)
4. **Restart** QGIS
5. **Enable** plugin (see Step 3 above)

## Uninstalling

1. Go to **Plugins → Manage and Install Plugins**
2. Find **Trajectory Exposure Analysis**
3. Click **Uninstall Plugin**

Or manually:
1. Delete `trajectory_exposure_qgis_plugin` folder from plugins directory
2. Restart QGIS

## Testing Installation

Run this test to verify everything works:

1. Open QGIS Processing Toolbox
2. Find **Trajectory Exposure Analysis → Trajectory Exposure Analysis (Multi-Format)**
3. Click to open dialog
4. If dialog opens with all parameters visible, installation successful!

## Getting Help

If you encounter issues:

1. Check QGIS Python Console for detailed error messages:
   - **Plugins → Python Console**
   - Look for red error text

2. Check QGIS logs:
   - **View → Panels → Log Messages**
   - Look for errors related to the plugin

3. Report issues:
   - GitHub Issues: [your-repo-url]
   - Email: support@cheaqi.org
   - Include: QGIS version, OS, error message

## System Requirements

### Minimum
- QGIS 3.16 or higher
- Python 3.6+
- 4 GB RAM
- 500 MB free disk space

### Recommended
- QGIS 3.28 LTR or higher
- Python 3.9+
- 8 GB RAM
- 2 GB free disk space
- SSD for better performance

### Tested On
- ✓ QGIS 3.28 LTR (Windows 10/11)
- ✓ QGIS 3.30 (macOS 12+)
- ✓ QGIS 3.28 (Ubuntu 22.04)

## Development Installation

For developers who want to modify the plugin:

```bash
# Clone repository (or use your existing folder)
cd /path/to/qgis/plugins/

# Create symbolic link (Unix/Mac)
ln -s /path/to/development/trajectory_exposure_qgis_plugin trajectory_exposure_qgis_plugin

# Or (Windows - as Administrator)
mklink /D trajectory_exposure_qgis_plugin C:\path\to\development\trajectory_exposure_qgis_plugin

# Enable plugin reload in QGIS
# Plugins → Plugin Reloader → Choose plugin
```

## Next Steps

After successful installation:

1. Read the **README.md** for usage instructions
2. Try the example workflow with sample data
3. Explore algorithm parameters
4. Check out the tutorial videos (if available)

---

**Installation complete!** 🎉 You're ready to analyze trajectories with dwell time calculations!
