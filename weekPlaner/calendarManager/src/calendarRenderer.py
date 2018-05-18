import calendar
import datetime
import time
from . import utils

class calendarRenderer(object):
    """docstring for calendarRenderer."""
    def __init__(self, request):
        self.request = dict(request.GET)
        self.innerHtml = ""
        self.useCurrentMonth = False
        self.__parseWsgiRequestToDict()

    def __parseWsgiRequestToDict(self):
        for key, value in self.request.items():
            self.request[key] = value.pop()


    def generateHtml(self):
        self.__obtainTargetDate()
        self.__generateCalendarHeader()
        self.__generateCalendarDaysOfWeek()
        self.__generateCalendarDays()
        return self.innerHtml


    def __obtainTargetDate(self):
        if self.request['targetDate'] == "CURRENT_DATE":
            targetDate = datetime.date.today()
            self.useCurrentMonth = True

        elif self.request['targetDate'] == "PREV_MONTH":
            # TODO: make it pretty and move to utils!
            print("self.request['currentlySetYear']")
            print(self.request['currentlySetYear'])
            tmpYear = int(self.request['currentlySetYear'])
            tmpMonth = utils.parseMonthToInt(self.request['currentlySetMonth'])

            if tmpMonth == 1:
                tmpMonth = 12
                tmpYear -= 1
            else:
                tmpMonth -= 1

            targetDate = datetime.date(year = tmpYear,
                                       month = tmpMonth,
                                       day = 1)

        elif self.request['targetDate'] == "NEXT_MONTH":
            # TODO: make it pretty and move to utils!
            print("self.request['currentlySetYear']")
            print(self.request['currentlySetYear'])
            tmpYear = int(self.request['currentlySetYear'])
            tmpMonth = utils.parseMonthToInt(self.request['currentlySetMonth'])

            tmpYear += tmpMonth // 12
            tmpMonth = (tmpMonth % 12) + 1

            targetDate = datetime.date(year = tmpYear,
                                       month = tmpMonth,
                                       day = 1)

        else:
            #TODO: add some meaningfull handling here
            print("INVALID DATE PROVIDED")
            targetDate = datetime.date.today()

        self.targetYear = targetDate.year
        self.targetMonth = targetDate.strftime("%B")
        self.targetMonthFirstDay = targetDate.replace(day=1).strftime("%w") # this assumes that week starts with sunday!
        self.targetMonthDayCount = calendar.monthrange(targetDate.year, targetDate.month)[1]

        if datetime.date.today().year == self.targetYear and datetime.date.today().strftime("%B") == self.targetMonth:
            self.useCurrentMonth = True

    def __generateCalendarHeader(self):
        self.innerHtml += '<div class="month">\n'
        self.innerHtml += '  <ul>\n'
        self.innerHtml += '    <li id="liPrevMonthId" class="prev" onclick="generatePrevMonth()">&#10094;</li>\n'
        self.innerHtml += '    <li id="liNextMonthId" class="next" onclick="generateNextMonth()">&#10095;</li>\n'
        self.innerHtml += '    <li id="liMonthYearId">' + str(self.targetMonth) + '<br><span style="font-size:18px">' + str(self.targetYear) + '</span></li>\n'
        self.innerHtml += '  </ul>\n'
        self.innerHtml += '</div>\n'

    def __generateCalendarDaysOfWeek(self):
        self.innerHtml += '<ul class="weekdays">\n'
        self.innerHtml += '  <li>Mo</li>\n'
        self.innerHtml += '  <li>Tu</li>\n'
        self.innerHtml += '  <li>We</li>\n'
        self.innerHtml += '  <li>Th</li>\n'
        self.innerHtml += '  <li>Fr</li>\n'
        self.innerHtml += '  <li>Sa</li>\n'
        self.innerHtml += '  <li>Su</li>\n'
        self.innerHtml += '</ul>\n'

    def __generateCalendarDays(self):
        self.innerHtml += '<ul class="days">\n'
        self.__generatePrefixDays()
        self.__generateDays()
        self.__generateSuffixDays()
        self.innerHtml += '</ul">\n'

    def __generatePrefixDays(self):
        for i in range(int(self.targetMonthFirstDay)-1):
            self.innerHtml += '<li> </li>\n'

    def __generateDays(self):
        if self.useCurrentMonth:
            self.__generateDaysWithHighlightDate(datetime.date.today().day)
        else:
            self.__generateDaysWithoutHighlightDate()

    def __generateDaysWithHighlightDate(self, highlightDate):
        self.__appendCalendarDays(1, int(highlightDate))
        self.innerHtml += '<li><span class="active">' + str(highlightDate) + '</span></li>\n'
        self.__appendCalendarDays(highlightDate + 1, int(self.targetMonthDayCount)+1)

    def __generateDaysWithoutHighlightDate(self):
        self.__appendCalendarDays(1, int(self.targetMonthDayCount)+1)

    def __appendCalendarDays(self, rangeMin, rangeMax):
        for i in range(rangeMin, rangeMax):
            self.innerHtml += '<li>' + str(i) + '</li>\n'

    def __generateSuffixDays(self):
        pass
