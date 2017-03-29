import logging

from Pages.Login.Login.LoginPageObjects import EbayLoginPageObjects as Login
from Pages.Login.MainLoginPage import MainLoginPage


class LoginPage(MainLoginPage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def loginToEbay(self, user):
        logging.info("login with credentials: {0} // {1}".format(user.login, user.password))
        self.driver.find_element(*Login.LoginInput).clear()
        self.driver.find_element(*Login.LoginInput).send_keys(user.login)
        self.driver.find_element(*Login.PasswordInput).clear()
        self.driver.find_element(*Login.PasswordInput).send_keys(user.password)
        self.driver.find_element(*Login.SignInButton).click()

    def loginWithProperCredentials(self, user):
        from Pages.CommonPages.MainPage.MainEbayPage import MainEbayPage
        self.loginToEbay(user)
        self.waitTillJavaScriptsEnds()
        return MainEbayPage(self.driver)

    def getLoginErrorMessage(self):
        logging.info("Getting error message")
        return self.driver.find_element(*Login.LoginErrorMessage).text

    def loginWithWrongCredentials(self, user):
        self.loginToEbay(user)
        return self
