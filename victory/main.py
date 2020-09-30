"""
Your module description
"""
import logging
import os

from .logger import victory_loggers
from .external_configuration import external_cofiguration_DEFAULT, external_configuration_FILE
from .hls_content_folder import copy_files_with_structure
from .file_transfer_scheduler import schedule_new_chunks_for_transfer

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
    values = external_configuration_FILE( 'hls-segmenter', ['hls-origin-path', 'hls-remote-path'] )
    if values is None:
        external_cofiguration_DEFAULT()
    
    # Check whether the HLS-VIDEO folders exist
    if copy_files_with_structure(origin=values[0], remote=values[1]) is True:
        logger.debug("HLS Content Folder is Found")
        
    schedule_new_chunks_for_transfer()
    

    
    
    