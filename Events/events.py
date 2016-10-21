__author__ = 'Narvi'
from selenium import webdriver
import pytest
from Locators.locators import pageLocators

class registrationEvents():

    def initial(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://automationpractice.com/index.php"
        return self.base_url

    def signIn(self):
        a = self.find_element(*self.sign_in).click()
        #return a

    def registration(self):
        self.find_element(*self.email_address).send_keys("user@gocodigo.com")
        b = self.find_element(*self.create_account_button).click()
        #return b




