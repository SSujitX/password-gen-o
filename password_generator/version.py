import os


def string():
    try:
        version_file = os.path.join(os.path.dirname(__file__), "VERSION")
        with open(version_file, "r", encoding="utf-8") as version_file:
            return version_file.read().strip()
    except Exception:
        return "0.0.0"  # Default version if no tag is found
