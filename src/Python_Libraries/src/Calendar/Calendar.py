# import necessary packages
import sys
import numpy as np
from datetime import datetime
# =============================================================================================
# =============================================================================================
# Date:    November 11, 2017
# Purpose: This class contains calendar related functions

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


class Calendar:
    def __init__(self):
        self.leap_years = np.array([2016, 2020, 2024, 2028, 2032, 2036, 2040,
                                    2044, 2048, 2052, 2056, 2060, 2064, 2068,
                                    2072, 2076, 2080, 2084, 2088])
# =============================================================================================
# =============================       PUBLIC FUNCTIONS       ==================================
# =============================================================================================

    def month_to_integer(self, month):
        """

        :param month: char string
                      The month written as a string (i.e. 'February', 'January')
        :return int_month: int
                           The numerical value of a month

        This function determines the numerical value of a month in the Gregorian Calendar
        """
        if np.size(month) == 1:
            int_month = self.__month_to_integer_iterator(month)
        else:
            int_month = []
            for i in range(len(month)):
                int_month.append(self.__month_to_integer_iterator(month[i]))
            int_month = np.array(int_month, np.dtype(np.int))
        return int_month
# ---------------------------------------------------------------------------------------------

    def integer_to_month(self, integer):
        """

        :param integer: int
                        An integer (1-12) representing a month.  Can be a scalar \
                        or an array
        :return month: char string
                       A character string spelling out a month

        This member-function transforms integers ranging from 1-12 into character \
        string months
        """
        # verify data input
        if np.size(integer) == 1:
            month = self.__integer_to_month_iterator(integer)
        else:
            month = []
            for i in range(len(integer)):
                month.append(self.__integer_to_month_iterator(integer[i]))
            month = np.array(month, np.dtype)
        return month
# ---------------------------------------------------------------------------------------------

    def days_in_month(self, month, year):
        """

        :param month: char string
                      The month (i.e. 'January', 'February', etc...
        :param year: int
                     The year
        :return days: int
                      The number of days in a month
        This member function determines the number of days in a user defined month.
        """
        if np.size(month) == 1:
            if np.size(year) != 1:
                sys.exit("FATAL ERROR: Month and Year not the same length in 'days_in_month()'")
            days = self.__days_in_month(month, year)
        else:
            if len(month) != len(year):
                sys.exit("FATAL ERROR: Month and Year not the same length in 'days_in_month()'")
            days = []
            for i in range(len(month)):
                days.append(self.__days_in_month(month[i], year[i]))
            days = np.array(days, np.dtype(np.int))
        return days
# ---------------------------------------------------------------------------------------------

    def days_between_dates(self, start_date, end_date):
        """

        :param start_date: tuple
                           (day, month, year), month is a character string (i.e. 'January',
                           'February', etc...)
        :param end_date: tuple
                           (day, month, year), month is a character string (i.e. 'January',
                           'February', etc...)
        :return days: int
                      The number of days between to dates
        This member function determines the number of days between two dates
        """
        start = datetime(start_date[2], self.month_to_integer(start_date[1]), start_date[0])
        end = datetime(end_date[2], self.month_to_integer(end_date[1]), end_date[0])
        return (end-start).days
# =============================================================================================
# =============================       PRIVATE FUNCTIONS       ==================================
# =============================================================================================

    def __days_in_month(self, month, year):
        """
        :param month : char string
                       The month, fully spelled out, (i.e. 'January', 'February', etc...)
        :param year :  int
                       The year
        :return days : int
                       The number of days in a year

        This function determines how many days are in each month of \
        the year to include leap years.
        """
        # Check months for errors
        upper_month = month.upper()
        if upper_month != 'JANUARY' and upper_month != 'FEBRUARY' and \
           upper_month != 'MARCH' and upper_month != 'APRIL' and \
           upper_month != 'MAY' and upper_month != 'JUNE' and \
           upper_month != 'JULY' and upper_month != 'AUGUST' and \
           upper_month != 'SEPTEMBER' and upper_month != 'OCTOBER' and \
           upper_month != 'NOVEMBER' and upper_month != 'DECEMBER':
            sys.exit("Months not properly entered in 'days_in_month()' functions")
        if month.upper() == 'JANUARY' or month.upper() == 'MARCH' or \
           month.upper() == 'JULY' or month.upper() == 'AUGUST' or \
           month.upper() == 'OCTOBER' or month.upper() == 'DECEMBER' or \
           month.upper() == 'MAY':
            return np.int(31)
        elif month.upper() == 'APRIL' or month.upper() == 'JUNE' or \
             month.upper() == 'SEPTEMBER' or month.upper() == 'NOVEMBER':
            return np.int(30)
        for i in range(len(self.leap_years)):
            if year == self.leap_years[i] and month.upper() == 'FEBRUARY':
                return np.int(29)
        return np.int(28)
# ---------------------------------------------------------------------------------------------

    def __month_to_integer_iterator(self, month):
        """
        :param month : char
                      The month, fully spelled out, (i.e. 'January', 'February', etc...)
        :return number : int
                         The numerical equivilent for a month

        This function assigns an integer for each month of the year
        """
        month = month.rstrip()
        if month.upper() == 'JANUARY':
            return np.int(1)
        elif month.upper() == 'FEBRUARY':
            return np.int(2)
        elif month.upper() == 'MARCH':
            return np.int(3)
        elif month.upper() == 'APRIL':
            return np.int(4)
        elif month.upper() == 'MAY':
            return np.int(5)
        elif month.upper() == 'JUNE':
            return np.int(6)
        elif month.upper() == 'JULY':
            return np.int(7)
        elif month.upper() == 'AUGUST':
            return np.int(8)
        elif month.upper() == 'SEPTEMBER':
            return np.int(9)
        elif month.upper() == 'OCTOBER':
            return np.int(10)
        elif month.upper() == 'NOVEMBER':
            return np.int(11)
        elif month.upper() == 'DECEMBER':
            return np.int(12)
        else:
            sys.exit('{}{}'.format(month.upper(), " Month not properly entered into 'month_to_integer()' function"))
# ---------------------------------------------------------------------------------------------

    def __integer_to_month_iterator(self, integer):
        """

        :param integer: int
                        An integer (1-12) representing a month
        :return month: char string
                       A character string spelling out a month

        This member-function transforms integers ranging from 1-12 into character \
        string months
        """
        if integer == 1:
            return 'January'
        elif integer == 2:
            return 'February'
        elif integer == 3:
            return 'March'
        elif integer == 4:
            return 'April'
        elif integer == 5:
            return 'May'
        elif integer == 6:
            return 'June'
        elif integer == 7:
            return 'July'
        elif integer == 8:
            return 'August'
        elif integer == 9:
            return 'September'
        elif integer == 10:
            return 'October'
        elif integer == 11:
            return 'November'
        elif integer == 12:
            return 'December'
        else:
            sys.exit("Month not properly entered into 'month_to_integer()' function")

# =============================================================================================
# =============================================================================================
# eof
