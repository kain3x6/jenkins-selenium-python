from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class GreenCardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.product_carts = (By.CSS_SELECTOR, "div[class='product']")
        self.add_to_cart_button = (By.CSS_SELECTOR, "button[type='button']")
        self.product_name = (By.CSS_SELECTOR, "h4[class='product-name']")
        self.card_icon = (By.CLASS_NAME, "cart-icon")
        self.proceed_to_checkout_button = (By.XPATH, "//button[.='PROCEED TO CHECKOUT']")
        self.wait = WebDriverWait(self.driver, 5)

    def navigate(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


    def add_to_cart(self, product_name):

        products = self.driver.find_elements(*self.product_carts)

        for product in products:
            name = product.find_element(*self.product_name)
            print(name.text)

            if name.text == product_name:
                product.find_element(*self.add_to_cart_button).click()
                break

    def open_cart_list(self):
        self.wait.until(EC.element_to_be_clickable(self.card_icon)).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()
