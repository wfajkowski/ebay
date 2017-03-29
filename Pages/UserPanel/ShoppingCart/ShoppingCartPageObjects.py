from selenium.webdriver.common.by import By


class ShoppingCartPageObjects:

    countrySelect = (By.ID, 'countryId')
    street1Input = (By.ID, 'address1')
    street2Input = (By.ID, 'address2')
    cityInput = (By.ID, 'city')
    stateSelect = (By.ID, 'state')
    zipCodeInput = (By.ID, 'zip')
