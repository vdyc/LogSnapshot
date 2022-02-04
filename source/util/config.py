import configparser
import os
import sys
import codecs


class ConfigHelper:
    config = None

    def __init__(self):
        config_file = 'config.ini'
        ConfigHelper.config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(sys.argv[0]), config_file)
        ConfigHelper.config.read_file(codecs.open(config_path, "r", "utf8"))

    @classmethod
    def config_write_back(cls):
        pass

    @classmethod
    def get_config(cls):
        return cls.config


_c = ConfigHelper()
config = ConfigHelper.get_config()
