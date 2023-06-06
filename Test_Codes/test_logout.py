from selenium import webdriver
from selenium.webdriver.common.by import By
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
    
    def test_logout(self, launch_driver):
        self.driver.get(self.url)
        # initial login 
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username1)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        # click menu button to select logout
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_menu).click()
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_logout).click()
        # assert if login button is present after logout
        login_button = self.driver.find_element(by=By.NAME, value="login-button")
        login_text = login_button.get_attribute("value")
        assert login_text == 'Login'
        print("SUCCESS # LOGGED OUT")
        print(login_text)