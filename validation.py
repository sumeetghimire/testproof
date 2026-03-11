"""Name validation for testproof."""


def validate_name(name: str, default: str = "World") -> str:
    """Return cleaned name or default if empty or invalid."""
    if not name or not name.strip():
        return default
    cleaned = name.strip()
    if any(c in cleaned for c in "@!#$%"):
        return default
    return cleaned
