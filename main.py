from gui.MainWindow import application
from scripts.init_postamat import get_start
from loguru import logger

if __name__ == "__main__":
    if get_start():
        logger.info('Application is running.')
        application()
    else:
        logger.error('Application could not be started.')

