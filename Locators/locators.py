__author__ = 'Narvi'
from selenium import webdriver
from selenium.webdriver.common.by import By

class pageLocators():

    def clicksignIn(self):
        sign_in = (By.CLASS_NAME,'login')

    def registration_locators(self):
        email_address = (By.ID,'email_create')
        create_account_button = (By.ID,'SubmitCreate')
        title_radio_buttons = (By.ID,'id_gender1')
        first_name = (By.ID,'customer_firstname')
        last_name = (By.ID,'customer_lastname')
        password = (By.CLASS_NAME,'is_required validate form-control')
        first_name_address = (By.ID,'firstname')
        last_name_address = (By.ID,'lastname')
        address = (By.ID,'address1')

