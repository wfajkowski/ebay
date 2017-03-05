from selenium.webdriver.common.by import By

class EbayMainPageObjects:
    SignInLink = (By.XPATH,'//a[text()="Sign in"]')
    LoggedUserText  = (By.XPATH,'//a[@id="gh-ug"]/b')
    CategoryMotors = (By.XPATH,'//tr[@role="list"]//a[text()="Motors"]')