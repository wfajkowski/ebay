from Assets.UsersRoles.User import User


class ProductionSettings(object):

    usaUrl = 'https://ebay.com'
    ukUrl = 'http://www.ebay.co.uk/'
    user = User(login='ebay.automatization@gmail.com', password='ebay123ebay', name='ebay')
