# Password Generator

**Password Generator** is a Python package that generates secure random passwords. It’s easy to use and can be integrated into any Python project. This project follows dynamic versioning based on Git tags and is published automatically using GitHub Actions.

## Installation

To install the package, use `pip`:

```sh
pip install password-gen-o
```

## Usage

Here is an example of how to use the generate_password function from the package:

```python
from password_generator import generate_password

# Generate a random password with default length (12 characters)
password = generate_password()

# Generate a password with a custom length (e.g., 16 characters)
custom_password = generate_password(16)

print("Generated Password:", password)
print("Custom Length Password:", custom_password)
```

## License

This project is licensed under the MIT license.
