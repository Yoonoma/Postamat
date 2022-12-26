from scripts.check_db import check_db
from loguru import logger

def get_start():
    # Checking for hardware errors
    start_program = check_db()

    if start_program:
        logger.info("The 'Cupboard' is ready to go...")
    else:
        # Log
        logger.error("ERROR")

    return start_program
