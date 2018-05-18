months = ["",
          "JANUARY",
          "FEBRUARY",
          "MARCH",
          "APRIL",
          "MAY",
          "JUNE",
          "JULY",
          "AUGUST",
          "SEPTEMBER",
          "OCTOBER",
          "NOVEMBER",
          "DECEMBER",
          ]

class indexPage():

    def __init__(self, selenium):
        self.selenium = selenium
        self.prevMonthLinkId = "liPrevMonthId"
        self.nextMonthLinkId = "liNextMonthId"
        self.monthYearId = "liMonthYearId"


    def clickPrevMonth(self):
        self.__clickItem(self.selenium.find_element_by_id(self.prevMonthLinkId))

    def clickNextMonth(self):
        self.__clickItem(self.selenium.find_element_by_id(self.nextMonthLinkId))

    def getCurrentYearAsInt(self):
        monthYearElemVAlue = self.__getMonthYearElem()
        result = ''.join([i for i in self.__getMonthYearElem().text if i.isdigit()])
        print("getCurrentYearAsInt: " + str(result))
        return result

    def getCurrentMonthAsInt(self):
        result = ''.join([i for i in self.__getMonthYearElem().text if not i.isdigit()]).rstrip()
        print("getCurrentMonthAsInt: " + str(months.index(result)))
        return months.index(result)

    def __getMonthYearElem(self):
        try:
            return self.selenium.find_element_by_id(self.monthYearId)
        except Exception as e:
            print("Failed to get value from the month year field value!")
            raise


    def __clickItem(self, item):
        try:
            item.click()
        except Exception as e:
            print("Failed to click element with id: " + str(item.get_attribute("id")))
            raise
