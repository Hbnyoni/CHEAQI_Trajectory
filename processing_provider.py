"""
Processing Provider for Trajectory Exposure Analysis
"""
from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon
import os

from .algorithms.trajectory_analysis_algorithm import TrajectoryAnalysisAlgorithm
from .algorithms.osm_building_fetcher import OSMBuildingFetcher


class TrajectoryExposureProvider(QgsProcessingProvider):
    """Processing Provider for Trajectory Exposure algorithms"""

    def __init__(self):
        super().__init__()

    def id(self):
        """Unique provider id"""
        return 'trajectory_exposure'

    def name(self):
        """Display name"""
        return 'Trajectory Exposure Analysis'

    def icon(self):
        """Provider icon"""
        icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
        if os.path.exists(icon_path):
            return QIcon(icon_path)
        return QgsProcessingProvider.icon(self)

    def loadAlgorithms(self):
        """Load all algorithms belonging to this provider"""
        self.addAlgorithm(TrajectoryAnalysisAlgorithm())
        self.addAlgorithm(OSMBuildingFetcher())
