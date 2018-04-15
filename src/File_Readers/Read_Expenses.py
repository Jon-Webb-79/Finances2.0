
from Python_Libraries.src.File_Readers.File_Readers import verify_file_existance
import pandas as pd
import os
import sys
# =============================================================================================
# =============================================================================================
# Date:    December 21, 2017
# Purpose: This class tests the Read_Expenses series of functions

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
# Version: 1.0
# =============================================================================================
# =============================================================================================
# This function reads data from an expense file to a pandas dataframe


def read_expense_file(file_name):
    """

    :param file_name: char str
                      The file name of the expense file to include the relative \
                      or absolute path length
    :return dataframe: object
                       The pandas dataframe

    This function opens and reads the expense file and ensures that the \
    expense_type entered is in accordance with a range of acceptable \
    inputs.
    """
    verify_file_existance(file_name)
    dataframe = pd.read_csv(file_name, parse_dates=[0],
                            dtype={'Date': str, 'Checking_Debit': float,
                                   'Checking_Addition': float,
                                   'Savings_Debit': float,
                                   'Savings_Addition': float,
                                   'Expense_Type': str,
                                   'Vendor': str,
                                   'Description': str})

    # Enforce Expense Type values
    for i in range(len(dataframe['Checking_Addition'])):
        if dataframe['Expense_Type'][i] != 'Bills' and \
           dataframe['Expense_Type'][i] != 'Paycheck' and \
           dataframe['Expense_Type'][i] != 'Groceries' and \
           dataframe['Expense_Type'][i] != 'Misc' and \
           dataframe['Expense_Type'][i] != 'Restaurant' and \
           dataframe['Expense_Type'][i] != 'Fed Taxes' and \
           dataframe['Expense_Type'][i] != 'State Taxes' and \
           dataframe['Expense_Type'][i] != 'Bar' and \
           dataframe['Expense_Type'][i] != 'Transfer' and \
           dataframe['Expense_Type'][i] != 'Planned Expense' and \
           dataframe['Expense_Type'][i] != 'Gas' and \
           dataframe['Expense_Type'][i] != 'Medical Bills':
            sys.exit('{}{}{}{}'.format('FATAL ERROR: ', dataframe['Expense_Type'][i],
                                       ' Expense type not properly entered on ',
                                       dataframe['Date'][i]))
    dataframe.fillna('None')
    return dataframe
# =============================================================================================
# This function opens the daily log file and reads it to a dataframe


def read_log_file(log_file):
    """

    :param log_file: char str
                     The name of the log file to include the relative \
                     or absolute path length
    :return data: object
                  The pandas dataframe

    This function reads the log file .csv file into a pandas dataframe \
    and passes the dataframe back to the calling program
    """
    verify_file_existance(log_file)
    data = pd.read_csv(log_file, parse_dates=[0], dtype={'Date': str, 'Checking': float,
                                                         'Savings': float})
    return data
# =============================================================================================
# This function reorganizes a python data frame based on date


def sort_dataframe_by_date(dataframe, file_name, test=False):
    """

    :param dataframe: object
                      The pandas dataframe that contains expense information
    :param file_name: char str
                      The file name for the expense file being sorted
    :param test: Boolean
                 False is no unit tests are performed or True if a unit \
                 test is performed
    :return: NA

    This function sorts an expense file based on dates and re-writes \
    the expense file if necessary
    """
    # Re-order the dataframe
    #print(dataframe['Date'])
    pd.to_datetime(dataframe['Date'])
    #sys.exit("Works Fine")
    dataframe['Date'] = pd.to_datetime(dataframe.Date)
    dataframe = dataframe.sort_values(by='Date')
    # Print the new file for test and real world configuration
    if test is True:
        file_name = file_name[:-4] + 'Temp.csv'
        dataframe[::-1].to_csv(file_name, index=False)
    if test is False:
        os.remove(file_name)
        dataframe[::-1].to_csv(file_name, index=False)
    return
# eof
