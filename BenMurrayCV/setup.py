from setuptools import setup

with open("VERSION", "r") as version_file:
    VERSION=version_file.readline().strip()

setup(
    name="BenMurrayCV",
    version=VERSION,
    install_requires=[
        "Django"
    ]
)