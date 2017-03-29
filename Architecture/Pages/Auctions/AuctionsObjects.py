from selenium.webdriver.common.by import By

class AuctionsObjects:
    auctionName = (By.ID, 'itemTitle')
    auctionSeller = (By.XPATH,'//span[@class="mbg-nw"]')
    auctionTimeToEnd = (By.XPATH,'//span[@id="vi-cdown_timeLeft"]')
    auctionBids = (By.XPATH,'//a[@id="vi-VR-bid-lnk"]')