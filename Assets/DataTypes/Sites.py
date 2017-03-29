from enum import Enum, unique


@unique
class Sites(Enum):
    """
    Klasa wspierająca różne lokacje ebay'a - aktualnie znajdują się w niej dwie używane w testach - USA i UK.
    Bazujemy tutaj na Enumach (zwróćcie uwagę na przecinki -> jest to bardzo podobne do słownika z tym, że
    zaimplementowanego jako klasa), dzięki czemu mamy łatwiejsze zarządzanie, a do funkcji zamiast podawać stringów
    (w których łatwo o literówkę) podajemy dany typ danych (np. Sites.UK), który wyciągnie sobie stringa z nazwą
    situ z tej klasy.
    """
    USA = "United States",
    UK = "United Kingdom"
