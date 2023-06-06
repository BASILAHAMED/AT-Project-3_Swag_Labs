# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class LoginData:
    username1 = "standard_user"
    username2 = "locked_out_user"
    username3 = "problem_user"
    username4 = "performance_glitch_user"

    password = "secret_sauce"
    invalid_password = "password"


# Python Class for Selenium Selectors
class ElementLocators:
    xpath_username = '//input[@id="user-name"]'
    xpath_password = '//input[@id="password"]'
    xpath_login = '//input[@id="login-button"]'
    xpath_product = '//span[@class="title"]'
    xpath_invalid_login = '//div[@id="login_button_container"]/div/form/div[3]/h3'
