from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from Test_Data import credentials
from Test_Locators.login_page_locators import LoginPageLocators

class Orangehrm:

    def __init__(self):
        self.login_locators = LoginPageLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def login_username(self):
        """
        find the webelement of username,clear the text field and input the username

        :return:
        """
        username_webelement =self.driver.find_element(By.NAME, self.login_locators.username_locator_name_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)
        sleep(2)

    def login_password(self):
        """
        find the webelement of password, clear the text field and input the invalid password

        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.login_locators.password_locator_name_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)
        sleep(2)

    def click_login(self):

        login_button_webelement = self.driver.find_element(By.XPATH, self.login_locators.login_path_xpath)
        login_button_webelement.click()
        sleep(2)

    def error_text(self):

        invalid_text_webelement = self.driver.find_element(By.XPATH, self.login_locators.invalid_text_xpath)
        return invalid_text_webelement.text



    def orangehrm_login(self):
        self.login_username()
        self.login_password()
        sleep(2)
        self.click_login()
        sleep(5)
        self.error_text()
        sleep(2)


if __name__ == '__main__':
    Orangehrm().orangehrm_login()
