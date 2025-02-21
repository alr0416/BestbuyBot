import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import undetected_chromedriver as uc
from selenium import webdriver

# make sure this path is correct
RTX5070LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-5070-12gb-gddr7-graphics-card-graphite-grey/6614154.p?skuId=6614154"

# Load environment variables from .env file
load_dotenv()

# Initialize ChromeDriver
driver = uc.Chrome()
driver.delete_all_cookies()

time.sleep(3)

driver.get(RTX5070LINK)

# Retrieve the email and password from environment variables
username = os.getenv("EMAIL")  # Get the username from  environment variables
password = os.getenv("PASSWORD")  # Get the password from environment variables

is_complete = False

while not is_complete:
    # find add to cart button
    try:

        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-test-id='add-to-cart'][class*='px-300'][class*='py-100']"))
        )


    except:
        print("'add to cart' button not found")
        driver.refresh()
        continue

    try:
        # add to cart
        print("'add to cart' button found")
        add_to_cart_button.click()
        print("Successfully added to cart - beginning check out")

        # go to cart for checkout
        driver.get("https://www.bestbuy.com/cart")

        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Checkout']"))
        )
        checkout_button.click()

        # fill in email
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        email_field.send_keys(username)

        # Wait for and click the "Continue" button
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            # Wait for continue button to be clickable
        )
        continue_button.click()  # Click the continue button

        password_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#password-radio"))
            # Wait for continue button to be clickable
        )
        password_button.click()

        # fill in password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        password_field.send_keys(password)

        # Click to submit the login form
        signin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        signin_button.click()
        print("Signing in")

        # fill in card cvv
        cvv_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "cvv"))
        )
        cvv = os.getenv("CVV")
        cvv_input.send_keys(cvv)
        print("placing order")

        # place order
        place_order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-track='Place your Order - Docked']"))
        )
        place_order_button.click()
        time.sleep(5)

        isComplete = True
    except:
        # retry
        driver.get(RTX5070LINK)
        print("Error - restarting bot")
        continue

print("Order placed successfully!")
