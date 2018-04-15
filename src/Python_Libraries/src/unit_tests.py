# Import modules here
from File_Readers import File_Readers as fr
from Calendar.Calendar import Calendar
from Plotting.TwoDPlots import twodplot, timedateplot, histogramplot

import numpy as np
import unittest
import datetime
# =============================================================================================
# =============================================================================================
# Date:    November 11, 2017
# Purpose: This code code tests all functionality in the python library

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


class MyTestCase(unittest.TestCase):
    # Test File_Readers/File_Readers.py.verify_file_existance()
    def test_file_reader_verify_file_existance(self):
        file_name = '../Data/VandV/File_Readers/Test.csv'
        # Validate the file does exist
        try:
            fr.verify_file_existance(file_name)
            self.assertEqual(1, 1)
        except:
            self.assertEqual(1, 0)
        # validate the file does not exist
        try:
            fr.verify_file_existance(file_name)
            self.assertEqual(1, 0)
        except:
            self.assertEqual(1, 1)
# ----------------------------------------------------------------------------------------------

    # Test File_Readers/File_Readers.py.read_csv_by_headers()
    def test_file_reader_read_csv_by_header(self):
        file_name = '../Data/VandV/File_Readers/Test.csv'
        test1 = np.array([1, 2, 3])
        test2 = np.array([3.6, 3.0, 2.87], np.dtype(np.float32))
        test3 = np.array(['Test1', 'Test2', 'Test3'])
        array1 = fr.read_csv_by_header(file_name, 'Column1', 'INTEGER')
        self.assertTrue((array1 == test1).all())
        array2 = fr.read_csv_by_header(file_name, 'Column2', 'FLOAT')
        self.assertTrue((array2 == test2).all())
        array3 = fr.read_csv_by_header(file_name, 'Column3', 'STRING')
        self.assertTrue((array3 == test3).all())
# ----------------------------------------------------------------------------------------------

    # Test File_Readers/File_Readers.py.read_textfile_by_keywords()
    def test_read_textfile_by_keyword(self):
        file_name = '../Data/VandV/File_Readers/Test.txt'
        value = fr.read_text_file_by_keywords(file_name,
                                              'First Keyword:', 'INteger')
        self.assertTrue(3, value)
        value = fr.read_text_file_by_keywords(file_name,
                                              'Second Keyword:', 'Float')
        self.assertTrue(27.6, value)
        value = fr.read_text_file_by_keywords(file_name,
                                              'Third Additional Keyword:', 'STRING')
        self.assertTrue('Test', value)
# =============================================================================================
    
    # Test Calendar/Calendar.py/Calendar/days_in_month()
    cal = Calendar()
    def test_calendar_days_in_month(self):
        months = np.array(['January', 'February', 'March', 'April',
                           'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December'])
        years = np.array([2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017,
                          2017, 2017, 2017, 2017])
        results = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
        days = []
        for i in range(len(months)):
            days.append(self.cal.days_in_month(months[i], years[i]))
        # Test for normal year with scalars
        self.assertListEqual(results.tolist(), days)
        # Test for leap year with scalars
        self.assertTrue(self.cal.days_in_month('February', 2016), 29)
        # catch difference between array and scalar inputs
        try:
            days = self.cal.days_in_month(months, years[i])
            self.assertEqual(1, 0)
        except:
            self.assertEqual(1, 1)
        # catch difference in size of arrays
        try:
            days = self.cal.days_in_month(months[:5], years[i])
            self.assertEqual(1, 0)
        except:
            self.assertEqual(1, 1)
        # Test for successfull array operations
        days = self.cal.days_in_month(months, years)
        self.assertTrue((days == results).all())
# ----------------------------------------------------------------------------------------------

    # Test Calendar/Calendar.py/Calendar/integer_month()
    def test_calendar_integer_month(self):
        results = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        months = np.array(['January', 'February', 'March', 'April',
                           'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December'])
        # test scalar values
        value = []
        for i in range(len(months)):
            value.append(self.cal.month_to_integer(months[i]))
        self.assertListEqual(value, results)
        # test array values
        new_value = self.cal.month_to_integer(months)
        self.assertTrue((new_value == results).all())

# ----------------------------------------------------------------------------------------------

    # Test Calendar/Calendar.py/Calendar/days_to_month()
    def test_integer_to_month(self):
        inputs1 = 1
        inputs2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        months = np.array(['January', 'February', 'March', 'April',
                           'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December'])
        self.assertTrue(self.cal.integer_to_month(inputs1), 'January')
        self.assertTrue((self.cal.integer_to_month(inputs2) == months).all())

# ----------------------------------------------------------------------------------------------

    # Test Calendar/Calendar.py/Calendar/days_between_dates()
    def test_days_between_dates(self):
        start_date = (1, 'January', 2017)
        end_date = (1, 'January', 2018)
        days = self.cal.days_between_dates(start_date, end_date)
        self.assertEqual(days, 365)
        end_date = (1, 'January', 2016)
        days = self.cal.days_between_dates(start_date, end_date)
        self.assertEqual(days, -366)
# =============================================================================================

    # Test Plotting/TwoDPlots.py/twodplot() for one set of data
    def test_single_two_d_plot(self):
        xdata1 = np.linspace(0, 1, num=100)
        ydata1 = xdata1**2.0
        plot_name = '../Data/VandV/plotting/OneFunc.png'
        twodplot(xdata1, ydata1, 'lin', 'lin', 'red', 'NONE', plot_name,
                 'X-axis', 'Y-axis', plots='single')
        return
# ----------------------------------------------------------------------------------------------
    # Test with two sets of data
    def test_multiple_two_d_plot(self):
        xdata1 = np.linspace(0, 1, num=100)
        xdata2 = xdata1

        ydata1 = xdata1
        ydata2 = xdata1**2.0

        xdata = (xdata1, xdata2)
        ydata = (ydata1, ydata2)

        colors = np.array(['red', 'blue'])
        labels = np.array(['linear', 'parabolic'])

        plot_name = '../Data/VandV/plotting/TwoFunc.png'
        twodplot(xdata, ydata, 'lin', 'lin', colors, labels, plot_name,
                 'X-axis', 'Y-axis', plots='multiple')
        return

# ----------------------------------------------------------------------------------------------
    # Test for logrithmic plotting
    def test_log_two_d_plot(self):
        xdata1 = np.linspace(0, 1, num=100)
        xdata2 = xdata1

        ydata1 = xdata1
        ydata2 = xdata1 ** 2.0

        xdata = (xdata1, xdata2)
        ydata = (ydata1, ydata2)

        colors = np.array(['red', 'blue'])
        labels = np.array(['linear', 'parabolic'])

        plot_name = '../Data/VandV/plotting/LogFunc.png'
        twodplot(xdata, ydata, 'log', 'log', colors, labels, plot_name,
                 'X-axis', 'Y-axis', plots='multiple')
        return
# ----------------------------------------------------------------------------------------------

    # Test for plotting a datetime string
    def test_timedateplot(self):
        base = datetime.datetime.today()
        number = 1000
        date_list = [base + datetime.timedelta(days=x) for x in range(0, number)]
        date_list2 = date_list
        xdata = np.linspace(0, 1, num=number)
        ydata = xdata**2.0
        ydata2 = xdata

        dates = (date_list, date_list2)
        yval = (ydata, ydata2)
        colors = np.array(['red', 'blue'])
        labels = np.array(['Test1', 'Test2'])

        plot_name = '../Data/VandV/plotting/TimeFunc.png'
        timedateplot(dates, yval, 'Dates', 'Y Data', colors, labels,
                     plot_name)
        return
# ----------------------------------------------------------------------------------------------

    # Test for histogram plotting
    def test_histogramplot(self):
        file = '../Data/VandV/plotting/Test.png'
        gaussian_numbers = np.random.normal(size=1000)
        histogramplot(gaussian_numbers, 'X Label', 'Y Label', file, nbins=100)
# =============================================================================================

if __name__ == '__main__':
    unittest.main()
