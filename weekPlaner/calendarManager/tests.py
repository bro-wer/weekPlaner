from django.conf import settings
from django.contrib.auth.models import User
from django.test import Client
from django.test import LiveServerTestCase
from django.test import TestCase
from selenium import webdriver

import time

class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(settings.SELENIUM_CHROMEDRIVER)
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()


    def test_navbar_has_roles_button(self):

        self.selenium.get(settings.MAIN_PAGE)

        time.sleep(5)
        rolesButton = self.selenium.find_element_by_id('aRoles')

        submit = self.selenium.find_element_by_name('register')

        #Fill the form with data
        first_name.send_keys('Yusuf')
        last_name.send_keys('Unary')
        username.send_keys('unary')
        email.send_keys('yusuf@qawba.com')
        password1.send_keys('123456')
        password2.send_keys('123456')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'Check your email' in self.selenium.page_source


#try:
#    # web_driver_module = settings.SELENIUM_WEBDRIVER
#    # print("DEBUG01")
#    # print(web_driver_module)
#    from selenium.webdriver.firefox import webdriver as web_driver_module
#    print("DEBUG02")
#    print(web_driver_module)
#except AttributeError:
#    from selenium.webdriver.firefox import webdriver as web_driver_module
#    print("DEBUG02")
#    print(web_driver_module)
#
#
#class CustomWebDriver(web_driver_module.WebDriver):
#    """Our own WebDriver with some helpers added"""
#
#    def find_css(self, css_selector):
#        """Shortcut to find elements by CSS. Returns either a list or singleton"""
#        elems = self.find_elements_by_css_selector(css_selector)
#        found = len(elems)
#        if found == 1:
#            return elems[0]
#        elif not elems:
#            raise NoSuchElementException(css_selector)
#        return elems
#
#    def wait_for_css(self, css_selector, timeout=7):
#        """ Shortcut for WebDriverWait"""
#        try:
#            return WebDriverWait(self, timeout).until(lambda driver : driver.find_css(css_selector))
#        except:
#            self.quit()
#
#
#class NavbarTests(TestCase):
#
#    def setUp(self):
#        self.client = Client()
#
#    def test_navbar_has_roles_button(self):
#        self.assertIs(False, False)
#        response = self.client.get('/')
#        print(response)
#
#class SeleniumTestCase(LiveServerTestCase):
#    """
#    A base test case for Selenium, providing hepler methods for generating
#    clients and logging in profiles.
#    """
#
#    def open(self, url):
#        self.wd.get("%s%s" % (self.live_server_url, url))
#
## Make sure your class inherits from your base class
#class Auth(SeleniumTestCase):
#    def setUp(self):
#        # setUp is where you setup call fixture creation scripts
#        # and instantiate the WebDriver, which in turns loads up the browser.
#        User.objects.create_superuser(username='admin',
#                                      password='pw',
#                                      email='info@lincolnloop.com')
#
#        # Instantiating the WebDriver will load your browser
#        self.wd = CustomWebDriver()
#
#    def tearDown(self):
#        # Don't forget to call quit on your webdriver, so that
#        # the browser is closed after the tests are ran
#        self.wd.quit()
#
#    def test_login(self):
#        self.open(reverse('admin:index'))
#
