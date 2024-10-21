import os


def string():
    try:
        version_file = os.path.join(os.path.dirname(__file__), "VERSION")
        with open(version_file, "r", encoding="utf-8") as fh:
            version = fh.read().strip()
            return version
    except Exception:
        return "unknown"
