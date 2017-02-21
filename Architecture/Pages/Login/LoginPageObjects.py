from selenium.webdriver.common.by import By

class LoginPageObjects:
    EmailInput = (By.XPATH, '//span/input[@placeholder="Email or username"]')
    PasswordInput = (By.XPATH,'//span/input[@placeholder="Password"]')
    LoginButton = (By.ID,'sgnBt')
    ErrorMessageText = (By.XPATH,'//span[@class="sd-err"]')