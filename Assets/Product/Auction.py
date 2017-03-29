class Auction:
    """
    Klasa do zarzadzania aukcja - aktualnie posiada jedynie atrybuty aukcji - ulatwia to przekazywania danych.
    Zamiast np. podawac funkcji 4 wartosci podajemy jeden - obiekt danej aukcji.
    """

    def __init__(self, title='', seller='', timeLeft='', startBid=''):
        self.title = title
        self.seller = seller
        self.timeLeft = timeLeft
        self.startBid = startBid
