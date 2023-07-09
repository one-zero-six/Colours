import logging
from dataclasses import dataclass


@dataclass
class Color:
    BLUE: str = "\x1b[1;34m"
    PURPLE: str = "\x1b[1;35m"
    GREY: str = "\x1b[38;21m"
    GREEN: str = "\x1b[1;32m"
    YELLOW: str = "\x1b[33;21m"
    RED: str = "\x1b[31;21m"
    BOLD_RED: str = "\x1b[31;1m"
    DEFAULT: str = "\x1b[0m"
    DT: str = "\x1b[30;1m"


@dataclass
class BaseFormatter:
    DT_FORMAT: str = "%Y-%m-%d %H:%M:%S %p"

    FORMATTED = dict()
    FORMATTED[logging.DEBUG] = logging.Formatter(
        fmt=f"{Color.DT}%(asctime)s{Color.DEFAULT} {Color.GREY}%(levelname)-8s{Color.DEFAULT} {Color.PURPLE}%(name)s{Color.DEFAULT} %(message)s",
        datefmt=DT_FORMAT,
    )
    FORMATTED[logging.INFO] = logging.Formatter(
        fmt=f"{Color.DT}%(asctime)s{Color.DEFAULT} {Color.GREEN}%(levelname)-8s{Color.DEFAULT} {Color.PURPLE}%(name)s{Color.DEFAULT} %(message)s",
        datefmt=DT_FORMAT,
    )
    FORMATTED[logging.WARNING] = logging.Formatter(
        fmt=f"{Color.DT}%(asctime)s{Color.DEFAULT} {Color.YELLOW}%(levelname)-8s{Color.DEFAULT} {Color.PURPLE}%(name)s{Color.DEFAULT} %(message)s",
        datefmt=DT_FORMAT,
    )
    FORMATTED[logging.ERROR] = logging.Formatter(
        fmt=f"{Color.DT}%(asctime)s{Color.DEFAULT} {Color.RED}%(levelname)-8s{Color.DEFAULT} {Color.PURPLE}%(name)s{Color.DEFAULT} %(message)s",
        datefmt=DT_FORMAT,
    )
    FORMATTED[logging.CRITICAL] = logging.Formatter(
        fmt=f"{Color.DT}%(asctime)s{Color.DEFAULT} {Color.BOLD_RED}%(levelname)-8s{Color.DEFAULT} {Color.PURPLE}%(name)s{Color.DEFAULT} %(message)s",
        datefmt=DT_FORMAT,
    )

    @staticmethod
    def format_arguments(message: str, arguments: tuple) -> str:
        """Formats the arguments with 'agrs' color.

        Args:
            message (str): Debug message.
            arguments (tuple): Debug arguments.

        Returns:
            str: Formatted message.
        """
        parameter_count = message.count("{}")
        argument_count = len(arguments)

        if parameter_count < argument_count:
            difference = argument_count - parameter_count
            additional_param = ", ".join(["{}" for _ in range(difference)])

            spacer = f"{Color.BOLD_RED}|{Color.DEFAULT} argument:"
            message = f"{message} {spacer} {additional_param}"

        args = (f"{Color.BLUE}{arg}{Color.DEFAULT}" for arg in arguments)

        return message.format(*args)

    @staticmethod
    def get_formatter(level: int) -> logging.Formatter:
        """Return formatter object.

        Args:
            level (int): Log level.

        Returns:
            logging.Formatter: Formatter object.
        """
        return BaseFormatter.FORMATTED.get(level, logging.INFO)


class LogFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        formatter = BaseFormatter.get_formatter(level=record.levelno)

        if record.args:
            record.msg = BaseFormatter.format_arguments(
                message=record.msg, arguments=record.args  # type: ignore
            )
            record.args = None

        return formatter.format(record)
