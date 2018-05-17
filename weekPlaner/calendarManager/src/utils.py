import calendar
import datetime

def parseMonthToInt(monthName):
    months = {v: k for k,v in enumerate(calendar.month_abbr)}
    return int(months[monthName[0:3]])

def decreaseMonth(dateTime):
    pass

def increaseMonth(dateTime):
    tmpYear = dateTime.year + dateTime.year // 12
    tmpMonth = (dateTime.month % 12) + 1
    dateTime.replace(year=tmpYear, month=tmpMonth)
    return dateTime
