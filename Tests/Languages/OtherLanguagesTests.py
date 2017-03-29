from Tests.BaseTestCase import BaseTestCase
from Assets.DataTypes.Sites import Sites


class LoginTests(BaseTestCase):

    def test_checkUnitedKingdom(self):
        # tutaj mamy wykorzystanie klasy Sites
        site = Sites.UK
        auctionPage = self.page.changeSiteTo(site).\
            checkUrl(site, self.envSettings).\
            OpenFashionWomenClothingSubPage(site).\
            goToDressesCategory().\
            enterFirstAuction()
        price = auctionPage.getAuctionStartBid()
        # jako ze znak funta jest znakiem specjalnym sprawszamy jest jego kod ascii
        self.assertEqual(price[0], "\xa3")
