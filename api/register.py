from selenium import webdriver

class Registration():

    def __init__(self, base_url):
        self.driver = webdriver.Firefox()
        self.driver.get(base_url)








