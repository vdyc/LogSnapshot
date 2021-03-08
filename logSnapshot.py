import sys
from source.lssApplication import LssApplication
from source.util.logger import Logger
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    sys.stdout = Logger()
    app = QApplication(sys.argv)
    lss = LssApplication()
    lss.showMaximized()
    app.exec_()
