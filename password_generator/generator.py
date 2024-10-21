import random
import string


def generate_password(length=12):
    """Generates a random password with a specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))
