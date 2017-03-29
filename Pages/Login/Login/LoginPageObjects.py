from selenium.webdriver.common.by import By


class EbayLoginPageObjects:

    LoginInput = (By.XPATH, '//input[@placeholder="Email or username"][@type="text"]')
    PasswordInput = (By.XPATH, '//input[@placeholder="Password"]')
    SignInButton = (By.ID, 'sgnBt')
    LoginErrorMessage = (By.ID, 'errf')
