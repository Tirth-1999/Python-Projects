from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path = "C:\Program Files (x86)\chromedriver.exe"

st = input('WHAT DO YOU WANT TO SEARCH??')

driver = webdriver.Chrome(path)
driver.get(r'https://www.sanfoundry.com/cryptography-questions-answers-hash-functions/')


time.sleep(8)

# searcher = driver.find_element_by_class_name("entry-content")

# st1 = searcher.text()
# print(st1)
# searcher.send_keys(st)
# searcher.send_keys(Keys.RETURN)

driver.quit() 