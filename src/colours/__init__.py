"""
Makes logging to the terminal easy and pretty.

>>> from colours import build_logger, Levels
>>> logger = build_logger(name="MyApp", log_level=Levels.DEBUG)
>>> logger.info("Hello {}!", "World")
2023-07-08 22:35:45 PM INFO     MyApp Hello World!
>>> logger.error("Something bad happened{}", "!!")
2023-07-08 22:36:38 PM ERROR    MyApp Something bad happened!!
"""

import sys
import logging
from .colorize import LogFormatter
from dataclasses import dataclass

VERSION = "1.0.0"


@dataclass
class Levels:
    DEBUG: int = logging.DEBUG
    INFO: int = logging.INFO
    WARNING: int = logging.WARNING
    ERROR: int = logging.ERROR
    CRITICAL: int = logging.CRITICAL


def build_logger(name: str = __name__, level: int = Levels.INFO) -> logging.Logger:
    """Create a logging object with color.

    Args:
        name (str, optional): Logger name. Defaults to __name__.
        level (int, optional): Log level. Defaults to Levels.INFO.

    Returns:
        logging.Logger: Logging object.
    """
    log = logging.getLogger(name)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(LogFormatter())

    log.addHandler(handler)
    log.setLevel(level)

    return log
