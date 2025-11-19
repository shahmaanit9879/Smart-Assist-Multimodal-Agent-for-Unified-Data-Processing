import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    filename="smartassist.log",
    filemode="a"
)

def log_event(message):
    logging.info(message)
