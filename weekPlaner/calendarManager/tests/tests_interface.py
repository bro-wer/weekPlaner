from django.test import Client
from django.test import LiveServerTestCase
from . import utils

class InterfaceTests(LiveServerTestCase):

    def setUp(self):
        self.test = utils.TestManager()
        super(InterfaceTests, self).setUp()

    def tearDown(self):
        self.test.destroy()
        super(InterfaceTests, self).tearDown()


    def test_navbar_has_roles_button(self):
        self.test.checkItemTextUsingItemId(itemId = 'aRoles', expectedText = 'Roles')
        self.test.checkClickRedirectUsingItemId(itemId = 'aRoles', expectedUrl = 'roles')

    def test_navbar_has_goals_button(self):
        self.test.checkItemTextUsingItemId(itemId = 'aGoals', expectedText = 'Goals')
        self.test.checkClickRedirectUsingItemId(itemId = 'aGoals', expectedUrl = 'goals')

    def test_navbar_has_todos_button(self):
        self.test.checkItemTextUsingItemId(itemId = 'aTodos', expectedText = 'TODOs')
        self.test.checkClickRedirectUsingItemId(itemId = 'aTodos', expectedUrl = 'todos')
