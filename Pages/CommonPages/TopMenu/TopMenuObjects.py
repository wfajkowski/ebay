from selenium.webdriver.common.by import By


class TopMenuObjects:

    SignInLink = (By.LINK_TEXT, 'Sign in')
    LoggedUserLink = (By.XPATH, '//a[@id="gh-ug"][contains(.,"{0}")]')
    CartIcon = (By.ID, 'gh-cart-i')
    MyEbayLink = (By.PARTIAL_LINK_TEXT, 'My eBay')
