import logging 
import shutil
import os

logger = logging.getLogger('victory')
    
def hls_content_folder():
    return True
    
#
# Copy all files and sub-folders from one directory into another.
# Mainly used for HLS-chunks that must be transferred from headquarters to local-station.
#
def copy_files_with_structure(origin='video', remote='content', symlinks=False, ignore=None):
    logger.debug('Ready to copy files with structure between folders ....\n  Origin = %s --> Remote = %s', origin, remote)
    
    # From
    for item in os.listdir(origin):
        logger.debug("Source folder .... Found --> %s", item)
        
        s = os.path.join(origin, item)
        d = os.path.join(remote, item)
        
        if os.path.isdir(s):
            # Ready to copy a folder
            logger.debug("Ready to copy a subfolder recursively ....")
            
            if os.path.exists(d):
                # The destination folder already exists - remove it
                shutil.rmtree(d)
            
            # Copy a fresh image of subfolders      
            shutil.copytree(s, d, symlinks, ignore)
        elif os.path.isfile(s):
            logger.debug("Ready to copy a file ... %s" , s)
            
            shutil.copy2(s, d)
            
        #shutil.copy()
    # To
    
    return True