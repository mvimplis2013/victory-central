import configparser
import os

config = configparser.ConfigParser()
config.read(os.getcwd() + '/conf/victory.conf')

def external_cofiguration_DEFAULT():
    return

def external_configuration_FILE():
    print(config.sections());
    
    return