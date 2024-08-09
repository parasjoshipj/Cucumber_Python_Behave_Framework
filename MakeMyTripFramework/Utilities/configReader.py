from configparser import ConfigParser

config = ConfigParser()
config.read("Utilities/config.ini")


def readConfig(section, key):
    config = ConfigParser()
    config.read("Utilities/config.ini")
    return config.get(section, key)
print(readConfig("info basic","url"))
