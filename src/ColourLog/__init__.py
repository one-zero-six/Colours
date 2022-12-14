"""
Simples use:

import logging

from ColourLogger import logger

log = logger.build(LogLevel.DEBUG)

log.debug("This is a {} message with argument", "debug")
"""

import sys
import logging
from .colorize import ColourLog

VERSION = "0.0.1"


def build_logger(name: str = __name__, log_level: int = logging.INFO) -> logging.Logger:
    """Return a colorized loggin object.

    Args:
        log_level (int, optional): Loggin level. Defaults to LogLevel.INFO.

    Returns:
        logging.Logger: Logging object
    """
    log = logging.getLogger(name)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(ColourLog())

    log.addHandler(handler)
    log.setLevel(log_level)

    return log
