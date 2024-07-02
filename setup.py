from setuptools import setup, find_packages
from pathlib import Path

VERSION = "0.0.1"
DESCRIPTION = "Rule34 API"
LONG_DESCRIPTION = Path(__file__).cwd().joinpath("README.md").read_text()


setup(
    name="rule34",
    version=VERSION,
    author="Oyunsky",
    author_email="deadcardinal293@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["httpx"],
    keywords=["python", "api", "rule34", "rule34xxx", "rule34api", "rule34-api", "api-wrapper"],
)
