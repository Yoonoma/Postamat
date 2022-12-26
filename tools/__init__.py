from loguru import logger

logger.add("../TestTask/debug.log", format="{time} {level} {messange}",
           level="DEBUG", rotation="1 week")
