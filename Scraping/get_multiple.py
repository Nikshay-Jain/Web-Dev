from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
query = "laptops"
file = 0

for i in range(20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=4EWMQE3KTUMK&sprefix=laptops%2Caps%2C261&ref=nb_sb_noss_2")

    elems = driver.find_elements(By.CLASS_NAME, "puisg-row")
    print(len(elems)," elements found.")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        print(elem.text)
        with open(f"data/{query}_{file}.html", "w", encoding='utf-8') as f:
            f.write(d)
            file+=1

driver.close()