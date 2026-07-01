from pathlib import Path


def ensure_directory(path: Path):
    """
    Creates a directory if it doesn't already exist.
    """
    path.mkdir(parents=True, exist_ok=True)