import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG) 

file_handler = RotatingFileHandler("app.log", maxBytes=5*1024*1024, backupCount=3)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

