from django.conf import settings
from selenium import webdriver

class todosPage():
    def __init__(self, selenium):
        self.selenium = selenium
        self.urlSuffix = 'todos'

    def getExpectedUrl(self):
        expectedUrl = "/".join([settings.MAIN_PAGE, self.urlSuffix])
        return expectedUrl
