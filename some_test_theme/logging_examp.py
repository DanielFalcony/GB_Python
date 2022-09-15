import logging

result = 'O my goodes'

logging.basicConfig(filename='logs.log', filemode='w', format='%(asctime)s -- %(levelname)s:%(message)s',
                    datefmt='%d.%m.%Y %I:%M:%S %p',
                    encoding='utf-8', level=logging.DEBUG)
logging.debug(f'This is {result} DEBUG data')
logging.info('This is INFO data')
logging.warning('This is WARNING data')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
