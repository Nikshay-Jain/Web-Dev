from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def scrape():
    # Connect to the Selenium WebDriver running inside the container
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")  # Run without UI

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",  # Connect to Docker WebDriver
        options=firefox_options
    )

    # driver = webdriver.Firefox()
    
    query = "laptops"
    file = 0

    for i in range(5):
        driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=4EWMQE3KTUMK&sprefix=laptops%2Caps%2C261&ref=nb_sb_noss_2")

        elems = driver.find_elements(By.CLASS_NAME, "puisg-row")
        print(len(elems)," elements found.")
        for elem in elems:
            d = elem.get_attribute("outerHTML")
            with open(f"data/{query}_{file}.html", "w", encoding='utf-8') as f:
                f.write(d)
                file+=1

    driver.close()