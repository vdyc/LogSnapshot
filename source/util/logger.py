import sys
import os
from datetime import datetime


class Logger(object):
    """
    Redirect print to file
    """
    def __init__(self):
        self.terminal = sys.stdout
        self.last_update = datetime.now()
        log_folder = os.path.join(os.path.dirname(sys.argv[0]), "log")
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        self.log = open(os.path.join(log_folder, datetime.now().strftime("%Y_%m_%d_%H_%M_%S.log")), "w+")

    def write(self, message):
        cur_time = datetime.now()
        self.log.write(cur_time.strftime("%M:%S.%f: ") + message + "\n")
        if (cur_time - self.last_update) > 3:
            self.log.flush()
            self.last_update = cur_time

    def flush(self):
        pass
