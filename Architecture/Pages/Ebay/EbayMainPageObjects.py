from selenium.webdriver.common.by import By

class EbayMainPageObjects:
    SignInLink = (By.XPATH,'//a[text()="Sign in"]')
    LoggedUserText  = (By.XPATH,'//a[@id="gh-ug"]/b')