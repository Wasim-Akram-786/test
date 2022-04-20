from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC



service=Service(executable_path="C:\\Users\\wasim\\.wdm\\drivers\\chromedriver\\win32\\100.0.4896.60\\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/")

wait=WebDriverWait(driver,10)
xpath='//span[text()="Username"]'


wait.until(EC.element_to_be_clickable('//span[text()="Username"]'))

