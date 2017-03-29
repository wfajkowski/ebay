import logging

from Pages.BasePage import BasePage
from Pages.CommonPages.TopMenu.TopMenuObjects import TopMenuObjects


class TopMenu(BasePage):

    def clickSignInLink(self):
        logging.info('Clicking sign in link')
        from Pages.Login.Login.LoginPage import LoginPage
        self.driver.find_element(*TopMenuObjects.SignInLink).click()
        return LoginPage(self.driver)

    def checkLoggedUser(self, user):
        logging.info('Checking that proper user is logged')
        self.driver.find_element(TopMenuObjects.LoggedUserLink[0],
                                 TopMenuObjects.LoggedUserLink[1].format(user.name))
        return self

    def goToShoppingCart(self):
        from Pages.UserPanel.ShoppingCart.ShoppingCartPage import ShoppingCartPage
        self.driver.find_element(*TopMenuObjects.CartIcon).click()
        return ShoppingCartPage(self.driver)

    def goToMyEbay(self):
        from Pages.UserPanel.MyEbay.MyEbayPage import MyEbayPage
        self.driver.find_element(*TopMenuObjects.MyEbayLink).click()
        return MyEbayPage(self.driver)
