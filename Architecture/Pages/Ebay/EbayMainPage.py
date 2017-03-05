from Architecture.Pages.BasePage import BasePage
from Architecture.Pages.Ebay.EbayMainPageObjects import EbayMainPageObjects
import time

class EbayMainPage(BasePage):
    def clickSignInLink(self):
        # login
        from Architecture.Pages.Login.LoginPage import LoginPage
        self.driver.find_element(*EbayMainPageObjects.SignInLink).click()
        return LoginPage(self.driver)

    def getLoggedUser(self):
        messageText = self.driver.find_element(*EbayMainPageObjects.LoggedUserText).text
        return messageText

    def goToCategory(self):
        from Architecture.Pages.Motors.Motors import Motors
        self.driver.find_element(*EbayMainPageObjects.CategoryMotors).click()
        return Motors(self.driver)
