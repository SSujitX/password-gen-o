from .generator import generate_password
from .version import string as get_version

__version__ = get_version()

__all__ = ["generate_password"]
