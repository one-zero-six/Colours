from src.colours.colorize import BaseFormatter


def test_get_color_formatter() -> None:
    formatter = BaseFormatter().get_formatter(level=20)
    assert formatter == BaseFormatter.FORMATTED[20]


def test_format_arguments_default() -> None:
    message = "Hello {}!"
    args = ("World",)

    formatted = BaseFormatter.format_arguments(message=message, arguments=args)

    assert formatted == "Hello \x1b[1;34mWorld\x1b[0m!"


def test_format_arguments_mismatch() -> None:
    message = "Hello !"
    args = ("World",)

    formatted = BaseFormatter.format_arguments(message=message, arguments=args)

    assert formatted == "Hello ! \x1b[31;1m|\x1b[0m argument: \x1b[1;34mWorld\x1b[0m"
