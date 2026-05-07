from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:5000")  # Replace with your app URL

# Find button and click
button = driver.find_element(By.TAG_NAME, "button")
button.click()

# Verify updated text
message = driver.find_element(By.ID, "message")
assert message.text == "Received!"

driver.quit()
