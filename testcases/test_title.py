from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://example.com")

# Verify page title
assert "Example Domain" in driver.title

driver.quit()
