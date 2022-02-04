import logging
import os, sys
from datetime import datetime


LOG_LEVEL_FILE = logging.DEBUG
LOG_LEVEL_CONSOLE = logging.INFO


def init_log():
    log_i = logging.getLogger("m")
    log_i.setLevel(LOG_LEVEL_FILE)
    log_file_name = os.path.join(os.path.dirname(sys.argv[0]), "log", datetime.now().strftime("%Y%m%d_%H%M%S.log"))
    open(log_file_name, "w")
    fh = logging.FileHandler(log_file_name, encoding='utf-8')
    fh.setLevel(LOG_LEVEL_FILE)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(LOG_LEVEL_CONSOLE)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    log_i.addHandler(fh)
    log_i.addHandler(ch)
    return log_i


log = init_log()
