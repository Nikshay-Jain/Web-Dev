from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")

# Verify title contains "Python"
assert "Python" in driver.title
print("✅ Assertion Passed: 'Python' is in the page title.")

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# Verify search results do not show "No results found."
assert "No results found." not in driver.page_source
print("✅ Assertion Passed: Search returned results.")

time.sleep(3)
driver.close()