from Architecture.Pages.BasePage import BasePage
from Architecture.Pages.Ebay.EbayMainPageObjects import EbayMainPageObjects

class EbayMainPage(BasePage):
    def clickSignInLink(self):
        # login
        from Architecture.Pages.Login.LoginPage import LoginPage
        self.driver.find_element(*EbayMainPageObjects.SignInLink).click()
        return LoginPage(self.driver)

    def getLoggedUser(self):
        messageText = self.driver.find_element(*EbayMainPageObjects.LoggedUserText).text
        return messageText
