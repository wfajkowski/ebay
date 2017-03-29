from Assets.Product.Auction import Auction
from Tests.BaseTestCase import BaseTestCase


class WatchListTests(BaseTestCase):
    """
    Klasa zawierajaca TC jedynie zwiazane z watch lista w user panelu
    """

    def test_addItemToWatchList(self):
        # pobranie usera z settingsow
        user = self.envSettings.user
        # zaczynamy od strony startowej
        # przechodzimy do strony logowania
        # logujemy sie - zwracana jest strona startowa
        # sprawdzamy zalogowane uzytkownika
        # otwieramy strone Fashion -> Women Clothing
        # przechodzimy do podstrony Dresses
        # filtrujemy jedynie aukcje
        # otwieramy pierwsza aukcje
        auctionPage = self.page.\
            clickSignInLink().\
            loginWithProperCredentials(user).\
            checkLoggedUser(user).\
            OpenFashionWomenClothingSubPage().\
            goToDressesCategory().\
            filterOnlyAuctions(). \
            enterFirstAuction()
        # tworzymy obiekt aukcji i zczytujemy ze strony odpowiednie dane
        dressAuction = Auction()
        dressAuction.title = auctionPage.getAuctionName()
        dressAuction.seller = auctionPage.getSellerName()
        dressAuction.timeLeft = auctionPage.getTimeLeft()
        dressAuction.startBid = auctionPage.getAuctionStartBid()
        # sprawdzamy czy aukcja jest juz dodana do watch listy
        isAuctionNotWatched = auctionPage.checkThatAuctionIsNotWatched()
        # jesli nie jest dodana to ja dodajemy
        if isAuctionNotWatched:
            auctionPage = auctionPage.addAuctionToWatchList()
        # przechodzimy do panelu uzytkownika
        # przechodzimy do watch listy w panelu
        watchListPage = auctionPage.goToMyEbay().\
            goToWatchList()
        # pobieramy dane z obserwowanej aukcji w watch liscie i sprawdzamy czy sa takie same
        # jak te pobrane na stronie z aukcja
        watchAuctionTitle = watchListPage.getFirstWatchedAuctionTitle()
        self.assertEqual(dressAuction.title, watchAuctionTitle)
        watchAuctionSeller = watchListPage.getFirstWatchedAuctionSellerName()
        self.assertEqual(dressAuction.seller, watchAuctionSeller)
