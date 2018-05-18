from django.conf import settings
from selenium import webdriver

class rolesPage():
    def __init__(self, selenium):
        self.selenium = selenium
        self.urlSuffix = 'roles'

    def getExpectedUrl(self):
        expectedUrl = "/".join([settings.MAIN_PAGE, self.urlSuffix])
        return expectedUrl
