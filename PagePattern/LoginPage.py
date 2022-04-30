
import pytest
from selenium import webdriver


class LoginPage:
    email_xpath="//input[@name='emailid']"
    submit_xpath='//input[@value="Submit"]'


    def __init__(self,driver):
        self.driver=driver

    def setemail(self,email):
        self.driver.find_element_by_xpath(self.email_xpath).clear()
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_xpath).click()
