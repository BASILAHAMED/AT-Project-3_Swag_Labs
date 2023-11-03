### AT Project 3
### System Description
Sauce Labs provides a demo website called "Swag Labs" specifically designed for testing automation. It offers different features and scenarios to test, such as adding items to a cart, placing orders, and more. You can access it at https://www.saucedemo.com/.

### Test Cases
```
1.Test Cases dealing with login and logout
2.Test Cases dealing with testing cart, adding product to cart
```

### Folder Structure
```
1.Test_Codes # It consists of Test Files (i.e. test_login, test_pim)
2.Test_Data # It consists of Test Data's (i.e. username, password, XPATH, ID, etc.,)
```

### Command Execution
```
pytest -v -s --capture=sys --html=C:\Users\test_result.html
pytest -v -s --capture=sys --html=C:\Users\AT-Project-3_Swag_Labs\reports\test_report.html
pytest -v -s --capture=sys --html=C:\Users\AT-Project-3_Swag_Labs\reports\test_report.html
```
