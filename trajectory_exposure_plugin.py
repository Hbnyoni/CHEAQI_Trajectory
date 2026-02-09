"""
Main Plugin Class for Trajectory Exposure Analysis
"""
from qgis.PyQt.QtCore import QCoreApplication, QTranslator
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import QgsApplication
import os.path

from .processing_provider import TrajectoryExposureProvider


class TrajectoryExposurePlugin:
    """QGIS Plugin Implementation for Trajectory Exposure Analysis"""

    def __init__(self, iface):
        """Constructor"""
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.provider = None
        
        # Initialize plugin actions
        self.actions = []
        self.menu = '&Trajectory Exposure Analysis'
        self.toolbar = None

    def initProcessing(self):
        """Initialize Processing framework integration"""
        self.provider = TrajectoryExposureProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI"""
        self.initProcessing()
        
        icon_path = os.path.join(self.plugin_dir, 'icon.png')
        
        # Add action to open the processing toolbox
        action = QAction(
            QIcon(icon_path) if os.path.exists(icon_path) else QIcon(),
            'Trajectory Exposure Analysis',
            self.iface.mainWindow()
        )
        action.triggered.connect(self.run)
        action.setStatusTip('Open Trajectory Exposure Analysis')
        
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(action)
        self.iface.addPluginToMenu(self.menu, action)
        self.actions.append(action)

    def unload(self):
        """Remove the plugin menu item and icon from QGIS GUI"""
        for action in self.actions:
            self.iface.removePluginMenu(self.menu, action)
            self.iface.removeToolBarIcon(action)
        
        if self.provider:
            QgsApplication.processingRegistry().removeProvider(self.provider)

    def run(self):
        """Run method that opens the processing toolbox"""
        self.iface.messageBar().pushInfo(
            "Trajectory Exposure Analysis",
            "Find the algorithms in Processing Toolbox under 'Trajectory Exposure'"
        )
        # Open processing toolbox
        self.iface.showProcessingToolbox()
