from selenium import webdriver
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Nike homepage
driver.get("https://www.nike.com")

time.sleep(5)

# Selecting a specific product

shoes_link = driver.find_element("xpath", "/html/body/div[4]/div/div/div[2]/div[6]/div/div/div/div/section/ul/li[3]")
shoes_link.click()

# Wait for the product page to load
time.sleep(8)

# Select a specific size (for example, size 10)

size_option = driver.find_element("xpath", "/html/body/div[4]/div/div/div[2]/div/div[4]/div[2]/div[2]/div/div/div[3]/form/div[1]/fieldset/div/div[6]")
size_option.click()

# Add the product to favourite

add_to_favourite_button = driver.find_element("xpath", "/html/body/div[4]/div/div/div[2]/div/div[4]/div[2]/div[2]/div/div/div[3]/form/div[2]/div/div/button[2]")
add_to_favourite_button.click()

time.sleep(8)

# Close the webdriver

time.sleep(8)  # Wait to see the result before closing the browser
driver.close()
