import setuptools
import subprocess


def get_version():
    try:
        version = (
            subprocess.run(
                ["git", "describe", "--tags", "--abbrev=0"], stdout=subprocess.PIPE
            )
            .stdout.decode("utf-8")
            .strip()
        )
        return version
    except Exception:
        return "0.0.0"


# Write version to a VERSION file
version = get_version()
with open("password_generator/VERSION", "w", encoding="utf-8") as version_file:
    version_file.write(f"{version}\n")

setuptools.setup(
    name="password_gen_o",
    version=version,
    description="A simple password generator package",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SSujitX/password-generator",
    author="Sujit Biswase",
    author_email="ssujitxx@gmail.com",
    license="MIT",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    package_data={"password_generator": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
