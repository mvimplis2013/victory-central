import configparser
import logging
import os
import sys

logger = logging.getLogger('victory')

external_config = {}

# Check whether application external configuration is valid
def check_app_configuration_exists():
    my_conf_folder = os.getcwd() + '/conf/'
    my_conf_file = my_conf_folder + 'victory.conf'
    
    if os.path.exists( my_conf_folder ) is False:
        # CONF folder NOT found
        logger.error( 'Failed to find the CONF folder ... Aborting!' )
        sys.exit(1)
        
    elif os.path.isfile( my_conf_file ) is False:
        # app.CONF file NOT found
        logger.error( 'Failed to find the "app.conf" file ... Aborting!' )
        sys.exit(1)
         
    # Read the file with configuration parameters
    config = configparser.ConfigParser()
    config.read( my_conf_file )
    
    # Return both the config-parser & config-params inside the file
    return config
    

def external_cofiguration_DEFAULT():
    raise NotImplementedError

# Read External configuration from file ... get all application parameters from .conf 
def external_configuration_FILE(section, mkeys):
    config = check_app_configuration_exists()
    
    # Get a list of all sections / default not included
    values = []
    for key in mkeys:
        # Get the value for every key
        try: 
            value = config.get(section, key)
            values.append( value )
        except Exception as e:
            #sys.exit(-1)
            logger.error('Exception while reading keys from section ...' + str(e) )
            
            return None
    
        logger.debug('External Configuration ... ' + section + '.' + key + ' === ' + value)
    
    return values