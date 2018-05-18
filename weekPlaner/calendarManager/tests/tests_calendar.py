from django.conf import settings
from django.test import Client
from django.test import LiveServerTestCase
from selenium import webdriver
from . import utils
from .pop import indexPage
import time

class CalendarTests(LiveServerTestCase):

    def setUp(self):
        super(CalendarTests, self).setUp()
        self.__initSelenium()
        self.indexPage = indexPage.indexPage(selenium = self.selenium)
        self.testUtil = utils.TestUtil(selenium = self.selenium)

    def __initSelenium(self):
        self.selenium = webdriver.Chrome(settings.SELENIUM_CHROMEDRIVER)
        self.selenium.get(settings.MAIN_PAGE)

    def tearDown(self):
        self.selenium.quit()
        super(CalendarTests, self).tearDown()


    def test_current_date_is_displayed_at_start(self):
        currentYear = self.indexPage.getCurrentYearAsInt()
        currentMonth = self.indexPage.getCurrentMonthAsInt()

        for i in range(1,12):
            self.indexPage.clickNextMonth()
            #TODO: replace sleep with nice dymaic waiting for element in the loop
            time.sleep(0.4)
            assert (self.indexPage.getCurrentMonthAsInt()-1) == (currentMonth%12)

            currentYear = self.indexPage.getCurrentYearAsInt()
            currentMonth = self.indexPage.getCurrentMonthAsInt()


    def test_next_button_forwards_calendar_by_one_month(self):
        currentYear = self.indexPage.getCurrentYearAsInt()
        currentMonth = self.indexPage.getCurrentMonthAsInt()

        for i in range(1,12):
            self.indexPage.clickNextMonth()
            #TODO: replace sleep with nice dymaic waiting for element in the loop
            time.sleep(0.4)
            assert (self.indexPage.getCurrentMonthAsInt()-1) == (currentMonth%12)

            currentYear = self.indexPage.getCurrentYearAsInt()
            currentMonth = self.indexPage.getCurrentMonthAsInt()



    def test_prev_button_backwards_calendar_by_one_month(self):
        currentYear = self.indexPage.getCurrentYearAsInt()
        currentMonth = self.indexPage.getCurrentMonthAsInt()

        for i in range(1,12):
            self.indexPage.clickPrevMonth()
            #TODO: replace sleep with nice dymaic waiting for element in the loop
            time.sleep(0.4)
            assert ((self.indexPage.getCurrentMonthAsInt()+1)%12) == (currentMonth)

            currentYear = self.indexPage.getCurrentYearAsInt()
            currentMonth = self.indexPage.getCurrentMonthAsInt()
