from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

product = str(input("enter the product you want to search"))
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.youtube.com")
try:
    srcbox = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "search_query")))
    srcbox.send_keys(product)
    try:
        submit_but = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-icon-legacy"]')))
        submit_but.click()
        try:
            first_video = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="video-title"]')))
            first_video.click()
        finally:
            print('not final -1')
    finally:
        print('not final -2')
finally:
    print('not final -3')

# srcbox = driver.find_element_by_name('search_query')
# srcbox.send_keys(product)
# submit_but = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# submit_but.click()
# first_video = driver.find_element_by_xpath('//*[@id="video-title"]')
# first_video.click()
# time.sleep(30)
# driver.quit()
