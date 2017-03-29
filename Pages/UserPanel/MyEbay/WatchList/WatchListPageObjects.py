from selenium.webdriver.common.by import By


class WatchListPageObjects:

    AuctionTitleInfo = (By.XPATH, '//a[@class="vip item-title"]')
    AuctionSellerInfo = (By.XPATH, "//a[@class='seller-id']")
