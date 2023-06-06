""" Test Scenario: Adding Items to Cart

Test the process of adding items to the cart.
Click on the "Add to Cart" button for a product.
Verify that the product is successfully added to the cart.
Check that the cart total and item count are updated accordingly."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Test_Data import login_data
import pytest


class TestLogout:
    url = "https://www.saucedemo.com/"
    
    # Launching driver for running the Python Tests
    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        self.driver.close()
    
    def test_addtocart(self, launch_driver):
        self.driver.get(self.url)
        # login webpage
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username1)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()

        # assert if any product in cart
        try:
            absent_element = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_cart_badge)
        except NoSuchElementException:
        # The element is not present as expected
            assert True
        else:
        # The element is present, which is unexpected
            assert False            

        # add product to cart
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_backpack).click()
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_jacket).click()

        # assert two products added to cart
        item_count = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_cart_badge).text
        assert item_count == '2'
        print("SUCCESS # PRODUCT ADDED SUCCESSFULLY")



    def test_cart_total(self, launch_driver):
        self.driver.get(self.url)
        # login webpage
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username1)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()

        # add product to cart
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_backpack).click()
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_jacket).click()

        # click cart and assert product total
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_cart).click()
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_checkout).click()
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_firstname).send_keys(login_data.CartData.firstname)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_lastname).send_keys(login_data.CartData.lastname)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_zipcode).send_keys(login_data.CartData.zipcode)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_continue).click()
        cart_total = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_total).text
        product_total = login_data.CartData.product_rate1 + login_data.CartData.product_rate2 + login_data.CartData.tax
        assert cart_total == 'Total: $' + str(round(86.38225, 2))
        print("SUCCESS # CART TOTAL ADDED SUCCESSFULLY")

        # click menu button to select logout
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_menu).click()
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_logout).click()

        # assert if login button is present after logout
        login_button = self.driver.find_element(by=By.NAME, value="login-button")
        login_text = login_button.get_attribute("value")
        assert login_text == 'Login'
