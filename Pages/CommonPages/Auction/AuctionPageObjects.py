from selenium.webdriver.common.by import By


class AuctionPageObjects:

    AuctionTitle = (By.ID, 'itemTitle')
    SellerName = (By.ID, 'mbgLink')
    TimeLeft = (By.ID, 'vi-cdown_timeLeft')
    AuctionStartBid = (By.ID, 'prcIsum_bidPrice')
    BuyNowPrice = (By.ID, 'mm-saleDscPrc')
    AddToWatchListLink = (By.XPATH, '//a[@n="Watch list"]/span[contains(.,"Add to watch list")]')
    WatchingInfo = (By.XPATH, '//span[text()="Watching"]')
