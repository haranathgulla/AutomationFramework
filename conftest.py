import pytest
from utils.base_driver import get_driver

@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()
