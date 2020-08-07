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
DIR_LOGS = ROOT_DIR / "logs"  # main dir for log-related files
DIR_LOGS_OUTPUT = DIR_LOGS / "output"
DIR_LOGS_CONFIG = DIR_LOGS / "config"
DIR_SRC = ROOT_DIR / "src"
DIR_TESTS = ROOT_DIR / "tests"
DIR_ASSETS = DIR_SRC / "assets"
DIR_OUTPUT = DIR_SRC / "output"

# PATHS
PATH_LOGS_CONFIG = DIR_LOGS_CONFIG / "logging.yaml"
PATH_LOGS_CONFIG_TEST = DIR_LOGS_CONFIG / "logging_test.yaml"