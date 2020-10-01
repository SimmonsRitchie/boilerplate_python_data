import pytest
from dotenv import load_dotenv
from typing import Dict
from src.modules.init.pandas_opts import pandas_opts


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    # Makes it easier to see pandas DFs when printing to console
    pandas_opts()
    load_dotenv()


@pytest.fixture(scope="session")
def example_fixture() -> Dict[str, Dict]:
    """
    Example fixture.

    """
    return {
        "id": "1",
        "name": "example",
    }

