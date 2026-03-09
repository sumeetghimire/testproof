"""Simple greeting module for testproof."""


def greet(name: str = "World") -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def farewell(name: str = "World") -> str:
    """Return a farewell string."""
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    print(greet())
