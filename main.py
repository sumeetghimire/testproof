"""Simple greeting module for testproof."""

from validation import validate_name


def greet(name: str = "World") -> str:
    """Return a greeting string. Validates name before use."""
    safe_name = validate_name(name, "World")
    return f"Hello, {safe_name}!"


def farewell(name: str = "World") -> str:
    """Return a farewell string."""
    return f"Goodbye, {name}!"


def greet_formal(name: str = "World") -> str:
    """Return a formal greeting."""
    return f"Good day, {name}."


def thanks(name: str = "you") -> str:
    """Return a thank-you message."""
    return f"Thank you, {name}!"


def welcome(name: str = "guest") -> str:
    """Return a welcome message."""
    return f"Welcome, {name}!"


if __name__ == "__main__":
    print(greet())
