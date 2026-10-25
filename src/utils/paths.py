from pathlib import Path


def find_project_root() -> Path:
    start = Path(__file__).resolve()

    # start is this file; its parents are the folders above it.
    for folder in start.parents:
        if (folder / ".git").exists():
            return folder

    raise FileNotFoundError(
        f"Could not find the project root: no .git found above {start}."
    )


RAW_DIR = find_project_root() / "data" / "raw"