import sys
from source.lssApplication import LssApplication
from source.util.logger import log
from PyQt5.QtWidgets import QApplication
from source.util.config import config

if __name__ == "__main__":
    version = config.get('VERSION', 'version')
    release = config.get("VERSION", "release_date")
    log.info(f"Welcome LogSnapshot ver: {version}   release: {release}")
    app = QApplication(sys.argv)
    lss = LssApplication()
    lss.showMaximized()
    app.exec_()
