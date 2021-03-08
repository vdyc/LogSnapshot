import sys
import os
from configparser import ConfigParser
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from gui.logSnapshot import Ui_MainWindow


class LssApplication(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        self.config = ConfigParser()
        self.config.read('config.ini')
        super(LssApplication, self).__init__(parent)
        self.setupUi(self)
        self.title = []
        self.show()
