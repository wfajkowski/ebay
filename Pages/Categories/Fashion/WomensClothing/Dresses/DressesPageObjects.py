from selenium.webdriver.common.by import By


class DressesPageObjects:

    filterAuctionRadio = (By.XPATH, '//a[input[@data-value="Auction"]]')
    firstAuctionImg = (By.XPATH, '//img[@class="img"]')
