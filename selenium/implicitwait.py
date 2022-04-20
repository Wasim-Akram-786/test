import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service

service=Service(executable_path="C:\\Users\\wasim\\.wdm\\drivers\\chromedriver\\win32\\100.0.4896.60\\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(10)
print(driver.title)
print(driver.current_url)