import logging

import logging
import sys

def setup_logger(name="redteam", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    fmt = "[%(levelname)s] %(message)s"
    formatter = logging.Formatter(fmt)

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)

    logger.addHandler(console)
    return logger


def setup_logger(name="redteam", level=logging.INFO):
    logging.basicConfig(
        format="[%(levelname)s] %(message)s",
        level=level
    )
    return logging.getLogger(name)

if __name__ == "__main__":
    try:
        main()
    except PermissionError as e:
        log.error(e)
    except KeyboardInterrupt:
        log.warning("User terminated")
