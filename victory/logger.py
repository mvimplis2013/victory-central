import logging
import logging.config
import os, sys

##############################################
### Configure the application logger
##############################################
def victory_loggers():
    user_file = os.getcwd() + '/conf/logger.conf'
    
    if not os.path.exists(user_file):
        # Missing logger configuration file -- cannot proceed
        print('Logger External Configuration File is Not Found !')
        
        #raise IOError()
        sys.exit(1)
        
    # External configuration is found ... Ready to load it 
    logging.config.fileConfig( user_file )
    #logger = logging.getLogger()
    logger = logging.getLogger('victory')
    
    logger.debug('STEP 1 --> Victory Logger is Ready to Report Application Mesages ...')
    
    #return logger