from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.amazon.in/s?k=laptops&crid=4EWMQE3KTUMK&sprefix=laptops%2Caps%2C261&ref=nb_sb_noss_2")

elem = driver.find_element(By.CLASS_NAME, "puisg-row")
print(elem.text)
print(elem.get_attribute("outerHTML"))
# time.sleep(3)
driver.close()