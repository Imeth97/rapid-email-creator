from setuptools import setup, find_packages
import os

# Read the contents of README.md file
with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as fh:
    long_description = fh.read()

# Read requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="rapid-email-creator",
    version="0.1.0",
    author="Rapid Email Creator Team",
    author_email="author@example.com",
    description="Automates creation of temporary email accounts using pluggable clients",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/rapid-email-creator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
) 