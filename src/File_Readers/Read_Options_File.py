# Import modules here
from Python_Libraries.src.File_Readers.File_Readers import read_text_file_by_keywords as read_file
import sys
import pandas as pd
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:    December 21, 2017
# Purpose: This module reads in the ReadOptions.txt file

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
# Version: 1.0
# =============================================================================================
# =============================================================================================


class ReadOptions(object):
    def __init__(self, options):
        self.options = options

    def read_file(self, file_name):
        self.__read_file_options(file_name)

        if self.options.organize_expense_file.upper() == 'YES':
            self.__read_expense_file_name(file_name)
        if self.options.draft_daily_history.upper() == 'YES':
            self.__read_account_log_file_name(file_name)
        if self.options.plot_account_history.upper() == 'YES':
            self.__read_plot_file_name(file_name)
        if self.options.sum_account_values.upper() == 'YES':
            self.__read_sum_expenses(file_name)
        if self.options.create_histogram_tables.upper() == 'YES':
            self.__read_histogram_data(file_name)
        if self.options.tabulate_expense.upper() == 'YES':
            self.__tabulate_expense(file_name)
        if self.options.sum_vendors.upper() == 'YES':
            self.__sum_vendors(file_name)
        return
# ---------------------------------------------------------------------------------------------
    # Reads all options

    def __read_file_options(self, file_name):
        self.options.organize_expense_file = read_file(file_name, 'Organize Expense File:',
                                                       'STRING').upper()
        self.options.draft_daily_history = read_file(file_name, 'Draft Daily History:',
                                                     'STRING').upper()
        self.options.plot_account_history = read_file(file_name, 'Plot Account History:',
                                                      'STRING').upper()
        self.options.sum_account_values = read_file(file_name, 'Sum Account Values:',
                                                    'STRING').upper()
        self.options.create_histogram_tables = read_file(file_name, 'Create Histogram Tables:',
                                                         'STRING').upper()
        self.options.tabulate_expense = read_file(file_name, 'Tabulate Expense:',
                                                   'STRING')
        self.options.sum_vendors = read_file(file_name, 'Sum Vendors:',
                                             'STRING')
        self.options.plot_future = read_file(file_name, 'Plot Future:',
                                             'STRING')
        self.options.account_log_file_name = read_file(file_name, 'Account History:',
                                                       'STRING')
        return
# ---------------------------------------------------------------------------------------------
    # Reads file name for daily expense history

    def __read_expense_file_name(self, file_name):
        self.options.expense_file_name = read_file(file_name, 'Expense History File:',
                                                   'STRING')
        return
# ---------------------------------------------------------------------------------------------
    # Reads file name for daily account log

    def __read_account_log_file_name(self, file_name):
        self.options.expense_file_name = read_file(file_name, 'Expense History File:',
                                                   'STRING')
        self.options.account_log_file_name = read_file(file_name, 'Account History:',
                                                       'STRING')
        self.options.checking_start_value = read_file(file_name, 'Checking Start:',
                                                      'FLOAT')
        self.options.savings_start_value = read_file(file_name, 'Savings Start:',
                                                     'FLOAT')
        self.options.log_end_date = read_file(file_name, 'Log End Date:',
                                              'STRING')
        if self.options.log_end_date.upper() == 'TODAY' and \
           self.options.log_end_date.upper() == 'FILE':
            sys.exit("FATAL ERROR: Log end day must be 'TODAY' or 'FILE'")
        return
# ---------------------------------------------------------------------------------------------
    # Reads plot file name and start/end dates

    def __read_plot_file_name(self, file_name):
        self.options.account_log_file_name = read_file(file_name, 'Account History:',
                                                       'STRING')
        self.options.history_plot_name = read_file(file_name, 'History Plot Name:',
                                                   'STRING')
        self.options.history_start_date = read_file(file_name, 'Plot Start Date:',
                                                    'STRING')
        self.options.history_end_date = read_file(file_name, 'Plot End Date:',
                                                  'STRING')
        self.options.history_start_date = \
            self.__create_datetime(self.options.history_start_date)
        self.options.history_end_date = \
            self.__create_datetime(self.options.history_end_date)

        day = (self.options.history_end_date - self.options.history_start_date).days
        if day < 0:
            sys.exit("FATAL ERROR: Plot end date is before plot start date")
        return
# ---------------------------------------------------------------------------------------------
    # Reads sum expenses info

    def __read_sum_expenses(self, file_name):
        self.options.expense_file_name = read_file(file_name, 'Expense History File:',
                                                   'STRING')
        self.options.sum_start_date = read_file(file_name, 'Sum Start Date:',
                                                'STRING')
        self.options.sum_end_date = read_file(file_name, 'Sum End Date:',
                                              'STRING')
        self.options.sum_start_date = \
            self.__create_datetime(self.options.sum_start_date)
        self.options.sum_end_date = \
            self.__create_datetime(self.options.sum_end_date)

        day = (self.options.sum_end_date - self.options.sum_start_date).days
        if day < 0:
            sys.exit('FATAL ERROR: sum end date is before sum start date')
        return
# ---------------------------------------------------------------------------------------------
    # Reads create histogram info

    def __read_histogram_data(self, file_name):
        self.options.expense_file_name = read_file(file_name, 'Expense History File:',
                                                   'STRING')
        self.options.histogram_directory = read_file(file_name, 'Histogram Directory:',
                                                     'STRING')
        self.options.histogram_end_date = read_file(file_name, 'Histogram End Date:',
                                                    'STRING')
        return

# ---------------------------------------------------------------------------------------------


    def __tabulate_expense(self, file_name):
        self.options.expense_file_name = read_file(file_name, 'Expense History File:',
                                                   'STRING')
        self.options.expense_type = read_file(file_name, 'Expense Type:',
                                              'STRING')
        self.options.expense_start_date = read_file(file_name, 'Expense Start Date:',
                                                    'STRING')
        self.options.expense_end_date = read_file(file_name, 'Expense End Date:',
                                                  'STRING')
        self.options.expense_keyword = read_file(file_name, 'Expense Keyword:',
                                                 'STRING')
        self.options.expense_start_date = \
            self.__create_datetime(self.options.expense_start_date)
        self.options.expense_end_date = \
            self.__create_datetime(self.options.expense_end_date)

        if self.options.expense_type.upper() != 'VENDOR' and \
           self.options.expense_type.upper() != 'EXPENSE_TYPE' and \
           self.options.expense_type.upper() != 'DESCRIPTION':
            sys.exit('FATAL ERROR: Expense type not properly entered in run options file')

        day = (self.options.expense_end_date - self.options.expense_start_date).days
        if day < 0:
            sys.exit('FATAL ERROR: expense end date is before expense start date')
# ---------------------------------------------------------------------------------------------


    def __sum_vendors(self, file_name):
        self.options.expense_file_name = read_file(file_name, 'Expense History File:',
                                                   'STRING')
        self.options.vendor_start_date = read_file(file_name, 'Vendor Start Date:',
                                                   'STRING')
        self.options.vendor_end_date = read_file(file_name, 'Vendor End Date:',
                                                 'STRING')
        self.options.vendor_start_date = \
            self.__create_datetime(self.options.vendor_start_date)
        self.options.vendor_end_date = \
            self.__create_datetime(self.options.vendor_end_date)

        day = (self.options.vendor_end_date - self.options.vendor_start_date).days
        if day < 0:
            sys.exit('FATAL ERROR: expense end date is before expense start date')
# ---------------------------------------------------------------------------------------------
    # Transforms date from a string to a datetime object

    def __create_datetime(self, start_date):
        if start_date.upper() == 'TODAY':
            new_date = pd.to_datetime('today').date()
        else:
            calendar = start_date.split()
            day = int(calendar[0])
            month = self.__month_to_integer(calendar[1])
            year = int(calendar[2])
            new_date = pd.to_datetime(str(year)+'-'+str(month)+'-'+str(day)).date()
        return new_date
# ---------------------------------------------------------------------------------------------
    # Transforms date from a string to a datetime object

    def __month_to_integer(self, month):
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
# =============================================================================================
# =============================================================================================
# eof
