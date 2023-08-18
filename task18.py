#demo.py
import logging

logging.basicConfig(filename='task18/demo.log',
                    level=logging.DEBUG,
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )


logging.debug('this is debug')
logging.info('this is info')
logging.warning('this is warning')
logging.error('this is error')
logging.critical('this is critical')
