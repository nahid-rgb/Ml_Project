from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of required libraries.
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="Ml_Project",
    version="0.0.1",
    author="Mahfujur Rahman",
    author_email="rmahfuzur818@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)




# ==========================================================
# setup.py — Project Packaging Configuration
# ==========================================================
#
# setup.py is the packaging configuration file of a Python project.
# It stores the project's metadata (name, version, author,
# dependencies, etc.) and tells Python/pip how to package,
# install, and distribute the project.
#
# PURPOSE:
#   • Converts your project from a normal folder into an
#     installable Python package.
#   • Allows the project to be shared or published on PyPI,
#     so others can install it using:
#
#         pip install <package_name>
#
#     (Just like installing NumPy, Pandas, or Scikit-learn.)
#
#   • Without setup.py → Your project is just a folder of scripts.
#   • With setup.py    → Python recognizes it as a package that
#                        can be installed, imported, and managed.
#
# WHEN DOES IT RUN?
#   setup.py does NOT execute automatically.
#
#   It is triggered by pip:
#
#       Directly:
#           pip install -e .
#
#       Indirectly:
#           pip install -r requirements.txt
#           (when requirements.txt contains "-e .")
#
#   During installation, pip reads setup.py to package the
#   project and install it correctly.
# ==========================================================


# ==========================================================
# Why do we use "-e ."?
# ==========================================================
#
# "-e ." means:
#     -e  -> Install in Editable Mode
#      .  -> Current Project
#
# During:
#
#     pip install -r requirements.txt
#
# pip installs all external libraries first. When it reaches "-e .",
# it triggers setup.py and installs the current project as a Python
# package in editable mode.
#
# Benefit:
# Any changes made to the source code are immediately reflected
# without reinstalling the project.


# ==========================================================
# Why was Ml_Project.egg-info created?
# ==========================================================
#
# When setup.py is executed (through "-e ."), pip automatically
# creates a *.egg-info folder.
#
# This folder stores metadata about the installed project and is
# generated automatically (do not edit it manually).
#
# Important files:
#
# PKG-INFO              -> Project metadata (name, version, author)
# requires.txt          -> Project dependencies
# top_level.txt         -> Top-level Python package(s) (e.g., src)
# SOURCES.txt           -> List of files included in the package
# dependency_links.txt  -> Dependency links (usually empty)
#
# Think of this folder as the "identity card" of your installed
# Python package. It is recreated automatically whenever the
# project is installed again.


# ==========================================================
# Why __init__.py inside src?
# ==========================================================
#
# __init__.py marks the folder as a Python package.
#
# This allows imports such as:
#
#     from src.components.data_ingestion import DataIngestion
#
# Without __init__.py, Python would not recognize the folder
# as a package in the traditional package structure.
#
#   ┌─────────────────────────────────────────┐
#   │  pip reads requirements.txt             │
#   │            │                            │
#   │            ▼                            │
#   │  installs pandas, numpy, Flask...       │
#   │            │                            │
#   │            ▼                            │
#   │  encounters "-e ."                      │
#   │            │                            │
#   │            ▼                            │
#   │  runs setup.py                          │
#   │            │                            │
#   │            ▼                            │
#   │  find_packages() finds src/             │
#   │            │                            │
#   │            ▼                            │
#   │  project registered as Python package   │
#   │            │                            │
#   │            ▼                            │
#   │  src/ is now importable everywhere      │
#   └─────────────────────────────────────────┘
#
# ==============================================================
