"""
Your module description
"""
import logging

from .logger import victory_loggers
from .external_configuration import external_cofiguration_DEFAULT, external_configuration_FILE
from .hls_content_folder import hls_content_folder

from . import *

def my_t():
    print( "######################################\n" + 
      app_messages['APPLICATION_STARTS'] + 
      "\n######################################")
    
    # Setup application loggers
    victory_loggers()
    # Get the VICTORY logger for application messages
    logger = logging.getLogger('victory')
    
    # Read the application external configuration with important information
    if external_configuration_FILE() is False:
        external_cofiguration_DEFAULT()
        
    # Check for hls-content folder if it exists
    if hls_content_folder() is True:
        logger.debug("HLS Content Folder is Found")
    

    
    
    