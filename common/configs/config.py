import os
from configparser import ConfigParser

config_path = os.environ.get("CONFIG_PATH", "common/configs/local.cfg")
print("config_path", config_path)
config = ConfigParser()
config.read(config_path)