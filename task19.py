#employee.py
import logging
import saveToFile as STF


logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

f = logging.Formatter(' %(levelname)s - %(message)s')

fh= logging.FileHandler('task19/employee.log')
fh.setFormatter(f)

logger.addHandler(fh)



logger.debug("start of employee program")

name = 'rahul'
age = 24
email = 'rahul@gmail.com'

if STF.nameCheck(name) is True:
    STF.saveData(name, age, email)
else:
    logger.critical('Employee check failed')

logger.debug('End of employee program')


#SaveToFile.py

import os
import logging


logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh= logging.FileHandler('task19/saveToFile.log')
fh.setFormatter(f)

logger.addHandler(fh)

logger.info("start of saveToFile program")


def nameCheck(name):
    logger.debug(f'Checking name "{name}"...')
    if os.path.exists('task19/data.txt'):
        with open('task19/data.txt', 'r') as readFile:
            for line in readFile:
                if line.lower().startswith(f'name: {name.lower()}'):
                    logger.error(f'Name: "{name}" already exists')
                    return False
                if len(name) == 0:
                    logger.critical('Name canot be blank')
                    return False
                elif not name.isalpha():
                    logger.critical('Name must be an alphabet')
                    return False
                else:
                    logger.error(f"check successfull")
                    return True
    else:
        logger.debug('no data found')
        return True


def saveData(name, age, email):
    logger.debug(f'saving details of {name}...')
    with open('data.txt', 'a') as appendFile:
        appendFile.write(f'Name: {name} - Age: {age} - email: {email}\n')
        logger.info(f' Details saved ')
        print(f' Details saved')


logger.info("end of saveToFile program")
logger.debug("###")
