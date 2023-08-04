from configparser import ConfigParser


# based on category and key it will read configurations

def read_configuration(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)
