__author__ = 'Narvi'
from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def initial(self):
    self.driver = webdriver.Firefox()
    self.url = "http://automationpractice.com/index.php"
    base_url = self.base_url
    return base_url