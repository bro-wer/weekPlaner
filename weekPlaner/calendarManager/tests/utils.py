from django.conf import settings
from selenium import webdriver

class TestManager():
    """docstring for testManager."""

    def __init__(self):
        self.selenium = webdriver.Chrome(settings.SELENIUM_CHROMEDRIVER)
        self.__getMainPage()

    def destroy(self):
        self.selenium.quit()

    def __getMainPage(self):
        self.selenium.get(settings.MAIN_PAGE)

    def checkItemTextUsingItemId(self, itemId, expectedText):
        try:
            item = self.__getItemUsingId(itemId)
            assert expectedText in item.text
        except Exception as e:
            print("\nFailed to find element with requested parameters!",
                  "\nElement id: {} \nElement text: {}".format(itemId, expectedText),)
            raise

    def checkClickRedirectUsingItemId(self, itemId, expectedUrl):
        try:
            item = self.__getItemUsingId(itemId)
            item.click()
            expectedUrl = "/".join([settings.MAIN_PAGE, expectedUrl])
            assert expectedUrl in self.selenium.current_url
        except Exception as e:
            print("\nCurrent url is not equal to expected url!" +
                  "\nExpected url: {} \nCurrent url: {}".format(expectedUrl, self.selenium.current_url),)
            raise

    def __getItemUsingId(self, itemId):
        return self.selenium.find_element_by_id(itemId)
