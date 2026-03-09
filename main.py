"""Simple greeting module for testproof."""


def greet(name: str = "World") -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def farewell(name: str = "World") -> str:
    """Return a farewell string."""
    return f"Goodbye, {name}!"


def greet_formal(name: str = "World") -> str:
    """Return a formal greeting."""
    return f"Good day, {name}."


if __name__ == "__main__":
    print(greet())
