import logging

class HandleLogs:
    @staticmethod
    def setup_logging():
        logger = logging.getLogger("TestLogger")
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        if not logger.handlers:
            logger.addHandler(ch)
        return logger

logs = HandleLogs.setup_logging()
