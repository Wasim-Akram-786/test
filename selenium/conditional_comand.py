import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service

service=Service(executable_path="C:\\Users\\wasim\\.wdm\\drivers\\chromedriver\\win32\\100.0.4896.60\\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/")

xpath='//span[text()="Username"]'

user=driver.find_element(by=By.XPATH, value=xpath)
print(user.is_displayed())
print(user.is_enabled())
print(user.is_selected())