"""Input validation for greeting and message functions."""


def validate_name(name: str, default: str = "World") -> str:
    """
    Validate and sanitize a name for use in greetings.
    Returns the name if valid (non-empty, alphanumeric + spaces), else the default.
    """
    if not name or not isinstance(name, str):
        return default
    cleaned = name.strip()
    if not cleaned:
        return default
    # Allow letters, numbers, spaces, hyphens
    if all(c.isalnum() or c in " -" for c in cleaned):
        return cleaned
    return default
