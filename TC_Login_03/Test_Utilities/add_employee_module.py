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

    def input_credentials(self):
        username_webelement = self.driver.find_element(By.NAME, self.login_locators.username_locator_name_tag)
        username_webelement.send_keys(credentials.username)
        sleep(4)

        password_webelement = self.driver.find_element(By.NAME, self.login_locators.password_locator_name_tag)
        password_webelement.send_keys(credentials.password)
        sleep(4)


        login_button_webelement = self.driver.find_element(By.XPATH, self.login_locators.login_path_xpath)
        login_button_webelement.click()
        sleep(5)


    def click_pim(self):

        pim_webelement = self.driver.find_element(By.XPATH, self.login_locators.pim_xpath)
        pim_webelement.click()
        sleep(2)

    def click_add(self):

        add_webelement = self.driver.find_element(By.XPATH, self.login_locators.add_button_xpath)
        add_webelement.click()
        sleep(2)

    def input_details(self):

        firstname_webelement = self.driver.find_element(By.XPATH, self.login_locators.fname_xpath)
        firstname_webelement.send_keys(credentials.firstname)
        sleep(2)

        middlename_webelement = self.driver.find_element(By.XPATH, self.login_locators.mname_xpath)
        middlename_webelement.send_keys(credentials.middlename)
        sleep(2)

        lastname_webelement = self.driver.find_element(By.XPATH, self.login_locators.lname_xpath)
        lastname_webelement.send_keys(credentials.lastname)
        sleep(2)


    def click_save(self):
        save_button_webelement = self.driver.find_element(By.XPATH, self.login_locators.save_button_xpath)
        save_button_webelement.click()
        sleep(2)

    def add_emp_details(self):
        self.input_credentials()
        sleep(2)
        self.click_pim()
        sleep(2)
        self.click_add()
        sleep(2)
        self.input_details()
        sleep(2)
        self.click_save()
        sleep(2)

if __name__ == '__main__':
    Orangehrm().add_emp_details()



