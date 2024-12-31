# Source Udemy: https://cglearning.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/learn/lecture/27782756#overview

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = './chromedriver-mac-arm64/'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (optional)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=path, options=chrome_options)

# Set explicit timeouts
driver.set_page_load_timeout(30)
driver.set_script_timeout(30)

# Open the website
driver.get(website)

# Perform any actions on the website here
try:
    # Example: Wait for a specific element to be present
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "some_element_id"))
    )
    print(element.text)
finally:
    driver.quit()