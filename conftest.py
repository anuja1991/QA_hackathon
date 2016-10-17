__author__ = 'Narvi'
import pytest

@pytest.fixture(scope="module")
def base_url():
    url = "http://automationpractice.com/index.php"
    return(url)
