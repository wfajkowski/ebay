from Pages.BasePage import BasePage
from Pages.UserPanel.ShoppingCart.ShoppingCartPageObjects import ShoppingCartPageObjects


class ShoppingCartPage(BasePage):

    def checkAllFieldsAreInAddressForm(self):
        self.driver.find_element(*ShoppingCartPageObjects.countrySelect)
        self.driver.find_element(*ShoppingCartPageObjects.cityInput)
        self.driver.find_element(*ShoppingCartPageObjects.street1Input)
        self.driver.find_element(*ShoppingCartPageObjects.street2Input)
        self.driver.find_element(*ShoppingCartPageObjects.stateSelect)
        self.driver.find_element(*ShoppingCartPageObjects.zipCodeInput)

