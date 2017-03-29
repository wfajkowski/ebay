from selenium.webdriver.common.by import By


class MainEbayPageObjects:

    SignInLink = (By.LINK_TEXT, 'Sign in')
    LoggedUserLink = (By.XPATH, '//a[@id="gh-ug"][contains(.,"{0}")]')
    CartIcon = (By.ID, 'gh-cart-i')

    # categories
    FollowingSection = ()
    TodaySection = ()
    MotorsCategory = ()
    FashionCategory = (By.XPATH, '//td[@class="cat"]/a[contains(.,"Fashion")]')
    ElectronicsCategory = ()
    CollectiblesAndArtCategory = ()
    HomeAndGardenCategory = ()
    SportingGoodsCategory = ()
    ToysCategoryCategory = ()
    BusinessAndIndustrialCategory = ()
    MusicCategory = ()
    DealsCategory = ()

    # Fashion sub-category
    UsaWomenClothingSubCategory = (By.XPATH, '//a[@title="Fashion - Women\'s Clothing"]')
    UkWomenClothingSubCategory = (By.XPATH, '//a[@title="Fashion - Women"]')

    # ebay sites
    EbaySites = (By.XPATH, '//a[@title="eBay country sites"]')
    SiteIcon = (By.XPATH, '//a[@title="eBay {0}"]')
