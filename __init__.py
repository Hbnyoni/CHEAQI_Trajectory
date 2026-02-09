"""
Trajectory Exposure Analysis Plugin for QGIS
"""

def classFactory(iface):
    """Load TrajectoryExposurePlugin class from file trajectory_exposure"""
    from .trajectory_exposure_plugin import TrajectoryExposurePlugin
    return TrajectoryExposurePlugin(iface)
