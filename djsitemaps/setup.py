#!/usr/bin/env python
from setuptools import setup

VERSION = "1.0"

setup(
    name="djsitemaps",
    version=VERSION,
    url="http://github.com/bradreardon/djsitemaps",
    download_url="git@github.com:bradreardon/djsitemaps.git",
    description="Extended version of Django sitemaps framework",
    author="Brad Reardon",
    author_email="me@bradreardon.com",
    platforms=["any"],
    packages=[
        "djsitemaps",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
    ],
    install_requires=[
        "django",
    ],
    zip_safe=False,
    include_package_data=True,
)