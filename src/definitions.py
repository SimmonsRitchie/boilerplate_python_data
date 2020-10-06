"""
This file contains important project variables.
"""
import os
from pathlib import Path

# This sets our root directory as the project directory
ROOT_DIR = (
    Path(os.path.dirname(os.path.abspath(__file__))) / ".."
)  # This is your Project Root

# DIRECTORIES
DIR_DATA = ROOT_DIR / "data"
DIR_SRC = ROOT_DIR / "src"
DIR_TESTS = ROOT_DIR / "tests"
DIR_ASSETS = DIR_SRC / "assets"
DIR_LOGS_OUTPUT = DIR_DATA / "logs"
DIR_LOGS_CONFIG = DIR_SRC / "logs_setup/config"
DIR_OUTPUT = DIR_DATA / "output"


# PATHS
PATH_LOGS_CONFIG = DIR_LOGS_CONFIG / "logging.yaml"
PATH_LOGS_CONFIG_TEST = DIR_LOGS_CONFIG / "logging_test.yaml"
