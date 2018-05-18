from django.test import TestCase
import os
import unittest

from . import HTMLTestRunner
from . import tests_calendar
from . import tests_interface


class MainTestSuite(unittest.TestCase):

    def test_Issue(self):
        regression_test = unittest.TestSuite()
        regression_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(tests_calendar.CalendarTests),
            # unittest.defaultTestLoader.loadTestsFromTestCase(tests_interface.InterfaceTests),
        ])

        outfile = open(os.path.join(os.getcwd(), "RegressionTestResult.html"), "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Regression Tests'
        )
        runner1.run(regression_test)

if __name__ == '__main__':
    unittest.main()
