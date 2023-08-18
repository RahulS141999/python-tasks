#demo.py
import logging

logging.basicConfig(filename='demo.log' , level=logging.DEBUG)
#logging.disable()

def nameCheck(name):
    if len(name) < 2:
        logging.debug('checking for name length...')
        return 'Invalid name'

    elif name.isspace():
        logging.debug('check if name is space')
        return 'invalid name'
    elif name.isalpha():
        logging.debug('check if name is an alphabet')
        return 'name is valid'
    elif name.replace(' ', '').isalpha():
        logging.debug('check full name')
        return 'name is valid'
    else:
        logging.debug('failed all check')
        return 'invalid name'
    
print(nameCheck('Rahul'))



#logging_file.py

import logging

logger = logging.getLogger()
logger.setLevel(logging.NOTSET)  

handler = logging.StreamHandler() 
handler.setLevel(logging.NOTSET)

formatter = logging.Formatter("%(levelname)s: %(message)s") 
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug('this is debug')
logger.info('this is info')
logger.warning('this is warning')
logger.error('this is error')
logger.critical('this is critical')
