import time

from selenium import webdriver

from PagePattern.LoginPage import LoginPage
from Utility import XLutility

class Test_002:

    path = "C:\\Users\\wasim\\PycharmProjects\\Guru_Bank\\Test Data\\Test_Data.xlsx"

    def test_login(self,setup):
        self.driver=setup
        self.driver.get("https://demo.guru99.com/")
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.row=XLutility.getRowCount(self.path,'Sheet1')
        print(self.row)
        self.user=XLutility.readData(self.path,'Sheet1',2,1)
        print("user",self.user)
        self.lp.setemail(self.user)
        self.lp.click_submit()
        self.driver.save_screenshot("..\\Snapshots\\" + "test_homePageTitle.png")
        self.driver.find_element_by_xpath("//a[contains(text(),'Insurance Project')]").click()
        time.sleep(5)
        self.driver.save_screenshot("..\\Snapshots\\"+"add.png")
        self.driver.refresh()
        self.driver.find_element_by_xpath("//a[contains(text(),'Insurance Project')]").click()
        time.sleep(10)

