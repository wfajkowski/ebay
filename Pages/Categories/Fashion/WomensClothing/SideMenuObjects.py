from selenium.webdriver.common.by import By


class SideMenuObjects:
    dressesLink = (By.XPATH, '//span[@class="title" and contains(.,"Dresses")]')
    onlyAuctionsOption = (By.XPATH, '//input[@type="radio" and @data-value="Auction"]')
