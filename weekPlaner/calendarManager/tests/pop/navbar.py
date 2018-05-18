from django.conf import settings
from selenium import webdriver

class navbar(object):

    """docstring for navbar."""
    def __init__(self, selenium):
        self.selenium = selenium
        self.rolesLinkId = "aRoles"
        self.goalsLinkId = "aGoals"
        self.todosLinkId = "aTodos"

    def clickRolesLink(self):
        self.__clickItem(self.selenium.find_element_by_id(self.rolesLinkId))

    def clickGoalsLink(self):
        self.__clickItem(self.selenium.find_element_by_id(self.goalsLinkId))

    def clickTodosLink(self):
        self.__clickItem(self.selenium.find_element_by_id(self.todosLinkId))

    def __clickItem(self, item):
        try:
            item.click()
        except Exception as e:
            print("Failed to click element with id: " + str(item.get_attribute("id")))
            raise
