import logging
from Architecture.Pages.BasePage import BasePage
from Architecture.Pages.Login.LoginPageObjects import LoginPageObjects

class LoginPage(BasePage):
    def login(self,user):
        #login page
        #logging.info("Logging")
        self.driver.find_element(*LoginPageObjects.EmailInput).send_keys(user.login)
        self.driver.find_element(*LoginPageObjects.PasswordInput).send_keys(user.password)
        self.driver.find_element(*LoginPageObjects.LoginButton).click()

    def loginWithValidUser(self,user):
        #logging.info("ValidUser")
        from Architecture.Pages.Ebay.EbayMainPage import EbayMainPage
        self.login(user)
        return EbayMainPage(self.driver)

    def loginWithInvalidUser(self,user):
        #logging.info("NotValidUser")
        self.login(user)
        messageText = self.driver.find_element(*LoginPageObjects.ErrorMessageText).text
        return messageText



