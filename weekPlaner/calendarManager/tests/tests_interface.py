from django.conf import settings
from django.test import Client
from django.test import LiveServerTestCase
from selenium import webdriver
from . import utils
from .pop import goalsPage
from .pop import indexPage
from .pop import rolesPage
from .pop import todosPage
from .pop import navbar

class InterfaceTests(LiveServerTestCase):

    def setUp(self):
        super(InterfaceTests, self).setUp()
        self.__initSelenium()
        self.goalsPage = goalsPage.goalsPage(selenium = self.selenium)
        self.indexPage = indexPage.indexPage(selenium = self.selenium)
        self.rolesPage = rolesPage.rolesPage(selenium = self.selenium)
        self.todosPage = todosPage.todosPage(selenium = self.selenium)
        self.navbar = navbar.navbar(selenium = self.selenium)
        self.testUtil = utils.TestUtil(selenium = self.selenium)

    def __initSelenium(self):
        self.selenium = webdriver.Chrome(settings.SELENIUM_CHROMEDRIVER)
        self.selenium.get(settings.MAIN_PAGE)


    def tearDown(self):
        self.selenium.quit()
        super(InterfaceTests, self).tearDown()


    def test_navbar_has_roles_button(self):
        self.navbar.clickRolesLink()
        self.testUtil.assertCurrentUrl(expectedUrl = self.rolesPage.getExpectedUrl())

    def test_navbar_has_goals_button(self):
        self.navbar.clickGoalsLink()
        self.testUtil.assertCurrentUrl(expectedUrl = self.goalsPage.getExpectedUrl())

    def test_navbar_has_todos_button(self):
        self.navbar.clickTodosLink()
        self.testUtil.assertCurrentUrl(expectedUrl = self.todosPage.getExpectedUrl())
