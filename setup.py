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




# ==============================================================
# setup.py — Project Packaging Configuration
# ==============================================================
#
# PURPOSE:
#   Turns your project folder into an installable Python package.
#
#   Without setup.py → just a folder of scripts
#   With    setup.py → a proper package Python can install,
#                      recognize, and let you import from anywhere
#
# WHEN DOES IT RUN?
#   setup.py does NOT run on its own. It is triggered by pip:
#
#     Directly  →  pip install -e .
#     Indirectly →  pip install -r requirements.txt
#                   (only when requirements.txt contains "-e .")
# ==============================================================


# from setuptools import find_packages, setup
# from typing import List


# ==============================================================
# CONSTANT: HYPEN_E_DOT
# ==============================================================
#
# "-e ." is a pip installation instruction, NOT a real package.
# If passed to setup(), it causes an error.
# So we store it as a constant to detect and remove it cleanly.
#
# HYPEN_E_DOT = '-e .'


# ==============================================================
# FUNCTION: get_requirements(file_path)
# ==============================================================
#
# Reads requirements.txt and returns a clean Python list
# of package names that setup() can actually use.
#
# WHAT IT DOES STEP BY STEP:
#
#   1. Opens requirements.txt
#   2. Reads every line into a list
#   3. Strips "\n" (newline) from each line
#   4. Removes "-e ." because it is a pip command, not a package
#   5. Returns the clean list
#
# EXAMPLE:
#
#   requirements.txt          Returned list
#   ─────────────────    →    ──────────────────────────────────
#   pandas                    ['pandas', 'numpy', 'Flask',
#   numpy                      'scikit-learn', 'xgboost']
#   Flask
#   scikit-learn
#   xgboost
#   -e .                      ← removed, not a real package
#


# def get_requirements(file_path: str) -> List[str]:
#     requirements = []

#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()

#         # Remove newline characters from every line
#         requirements = [req.replace("\n", "") for req in requirements]

#         # Remove "-e ." — it's a pip instruction, not an installable package
#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)

#     return requirements


# ==============================================================
# FUNCTION: find_packages()
# ==============================================================
#
# Automatically scans the project and finds every folder
# that contains an __init__.py file — those folders are
# treated as Python packages.
#
# WHY USE IT?
#   You never have to manually list your packages.
#   As your project grows and you add more folders/modules,
#   find_packages() discovers them automatically.
#
# EXAMPLE:
#
#   Project structure:
#
#   ML_Project/
#   ├── src/
#   │   ├── __init__.py         ← found by find_packages()
#   │   ├── components/
#   │   │   └── __init__.py     ← found by find_packages()
#   │   └── pipeline/
#   │       └── __init__.py     ← found by find_packages()
#   └── setup.py
#
#   Result: ['src', 'src.components', 'src.pipeline']
#
# NOTE:
#   A folder WITHOUT __init__.py is invisible to find_packages().
#   Always create __init__.py inside every folder you want
#   Python to recognize as a package.
#


# ==============================================================
# FUNCTION: setup()
# ==============================================================
#
# The main registration function. Officially introduces your
# project to Python so it can be installed and imported.
#
# FIELDS EXPLAINED:
#
#   name            → The package name used during installation
#                     e.g. pip install mlproject
#
#   version         → Current version of your project
#                     Follow semantic versioning: MAJOR.MINOR.PATCH
#                     0.0.1 = early development / first build
#
#   author          → Name of the project creator
#
#   author_email    → Contact email for the project
#
#   packages        → List of all packages found by find_packages()
#                     These are the folders Python will recognize
#
#   install_requires → External libraries your project depends on
#                      Returned by get_requirements('requirements.txt')
#                      pip installs these automatically
#
# WHAT HAPPENS AFTER setup() RUNS?
#
#   Python registers your project. You can now import your own
#   modules from anywhere inside the project, just like you
#   import third-party packages:
#
#     from src.components.data_ingestion import DataIngestion
#

# setup(
#     name="mlproject",
#     version="0.0.1",
#     author="Mahfuzur Rahman",
#     author_email="rmahfuzur818@gmail.com",
#     packages=find_packages(),
#     install_requires=get_requirements("requirements.txt")
# )


# ==============================================================
# WHAT DOES "-e ." MEAN IN requirements.txt?
# ==============================================================
#
#   -e  →  Editable Mode
#    .  →  Current folder (where setup.py lives)
#
# NORMAL install (pip install .)
#   Copies your code into the Python environment.
#   If you change your code, you must reinstall.
#
# EDITABLE install (pip install -e .)
#   Creates a live link to your project folder.
#   Any code change is immediately reflected —
#   no reinstall needed. Perfect for development.
#
# FULL EXECUTION FLOW when you run:
#   pip install -r requirements.txt
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
