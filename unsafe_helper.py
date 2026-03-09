"""DO NOT USE IN PRODUCTION - for PRoof security scan test only."""


def run_dynamic(code: str):
    """Dangerous: executes arbitrary code. Exists only to trigger PRoof security scan."""
    eval(code)  # noqa: S307 - intentional for testing PRoof


def run_shell(cmd: str):
    """Dangerous: shell execution. Exists only to trigger PRoof security scan."""
    import os
    os.system(cmd)  # noqa: S605 - intentional for testing PRoof
