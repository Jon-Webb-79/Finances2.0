# Import modules here
from File_Readers.Read_Expenses import read_expense_file, sort_dataframe_by_date
from File_Readers.Read_Expenses import read_log_file
from Data_Processing.Iterator import daily_account_value, histogram_values
from Data_Processing.Iterator import sum_expense
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sys
import matplotlib.dates as mdates
# =============================================================================================
# =============================================================================================
# Date:    December 22, 2017
# Purpose: This module runs the code

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = 1.0
# =============================================================================================
# =============================================================================================
# This function re-organizes the expense file by date and redrafts the .csv file


def organize_expense_file_by_date(file_name):
    """

    :param file_name: char str
                      the name of the expense file to include the \
                      relative or absolute path length
    :return: NA

    This function organizes all function calls required to sort and re-write \
    the expense file by date
    """
    data = read_expense_file(file_name)
    sort_dataframe_by_date(data, file_name)
    return
# =============================================================================================


def draft_daily_log_file(checking_start, savings_start, expense_file_name,
                         log_file, log_end_date):
    """

    :param checking_start: float
                           The starting amount in the checking account \
                           in dollars U.S.
    :param savings_start: float
                          The starting amount in the savings account \
                          in dollars U.S.
    :param expense_file_name: char str
                              The name of the expense file to include the \
                              relative or absolute path link
    :param log_file: char str
                     The name of the log file to include the relative \
                     or absolute path length
    :param log_end_date: char str
                         Today equates to current day, File equates to \
                         the last date in the expense file
    :return: NA

    This function organizes all of the function calls required to create a \
    log file containing the value of the checking and savings account at
    every date between start_date and end_date.
    """
    data = read_expense_file(expense_file_name)
    start_date = pd.to_datetime(min(data['Date'])).date()
    if log_end_date.upper() == 'TODAY':
        end_date = pd.to_datetime('today').date()
    else:
        end_date = max(data['Date']).date()
    daily_account_value(checking_start, savings_start, start_date, end_date,
                        data, log_file)
    return
# =============================================================================================
# This function produces a time history plot of the checking and total accounts


def plot_time_history(log_file, start_date, end_date):
    """

    :param log_file: char str
                     The name of the file containing daily log info
    :param start_date: object
                       Datetime object representing the start date \
                       (Year, Month, Day)
    :param end_date: object
                     Datetime object representing the end date \
                     (Year, Month, Day)
    :return NA:
    """
    data = read_log_file(log_file)
    newest_date = max(data['Date']).date()
    if end_date > newest_date:
        sys.exit('Plot end date is greater than the newest date in log file')
    data['Total'] = data['Checking'] + data['Savings']
    data = data.set_index("Date")
    plt.figure()
    ax = data.ix[end_date:start_date].plot(y=['Checking', 'Total'], style=['-', '-'],
                                           color=['red', 'blue'])
    ax.set_ylabel('Value ($)')
    plt.show()
# =============================================================================================
# This function sums all of the values in expense file over a specified date range


def sum_account_values(start_date, end_date, expense_file):
    """

    :param start_date: object
                       Datetime object representing the start date \
                       (Year, Month, Day)
    :param end_date: object
                     Datetime object represernting the end date \
                     (Year, Month, Day)
    :param expense_file: char str
                         The name of the file containing expense information
    :return NA:
    """
    data = read_expense_file(expense_file)
    data = data.set_index("Date")
    grouped = data.ix[end_date:start_date].groupby('Expense_Type').Checking_Debit.sum() + \
              data.ix[end_date:start_date].groupby('Expense_Type').Checking_Addition.sum()
    print('=================================================')
    print('=================================================')
    print('===========      CHECKING ACCOUNT      ==========')
    print('=================================================')
    print('=================================================')
    print(grouped)

#    grouped = data.ix[end_date:start_date].groupby('Expense_Type').Savings_Debit.sum() + \
#              data.ix[end_date:start_date].groupby('Expense_Type').Savings_Addition.sum()
#    print('=================================================')
#    print('=================================================')
#    print('===========      SAVINGS ACCOUNT      ===========')
#    print('=================================================')
#    print('=================================================')
#    print(grouped)
    return
# =============================================================================================
# This function sums all of the values in expense file over a specified date range


def create_histogram_tables(expense_file, histogram_directory, hist_end_date):
    """

    :param expense_file: char str
                         The name of the file containing expense information
    :param histogram_directory: char str
                                The name of the directory containing histogram \
                                information
    :param hist_end_date: char str
                          'Today' or 'File'
    :return NA:
    """
    data = read_expense_file(expense_file)
    start_date = min(data['Date']).date()
    if hist_end_date.upper() == 'TODAY':
        end_date = pd.to_datetime('today').date()
    else:
        end_date = max(data['Date']).date()
    info = []
    bar_expense = histogram_values(start_date, end_date, data, 'Bar')
    groceries_expense = histogram_values(start_date, end_date, data, 'Groceries')
    restaurant_expense = histogram_values(start_date, end_date, data, 'Restaurant')
    misc_expense = histogram_values(start_date, end_date, data, 'Misc')
    gas_expense, date = histogram_values(start_date, end_date, data, 'Gas')
    information = {'Date': date, 'Bar': bar_expense[0], 'Groceries': groceries_expense[0],
                   'Restaurant': restaurant_expense[0], 'Misc': misc_expense[0],
                   'Gas': gas_expense}
    df = pd.DataFrame(data=information)
    df = df.set_index("Date")
    df = df[::-1]
    df.to_csv(histogram_directory+'HistFile.csv')
    return
# =============================================================================================
# This function tabulates a specific expense


def tabulate_expense(file_name, expense_type, expense_keyword, start_date, end_date):
    data = read_expense_file(file_name)
    value = sum_expense(start_date, end_date, data, expense_keyword, expense_type)
    print('{}{}{}'.format(expense_keyword,': ', round(value, 2)))
    return

# =============================================================================================
# This function sums all vendor expenses over a user defined set of dates


def vendor_expenses(expense_file, start_date, end_date):
    data = read_expense_file(expense_file)
    data = data.set_index("Date")
    grouped = data.ix[end_date:start_date].groupby('Vendor').Checking_Debit.sum() + \
              data.ix[end_date:start_date].groupby('Vendor').Checking_Addition.sum()
    print('=================================================')
    print('=================================================')
    print('===========      CHECKING ACCOUNT      ==========')
    print('=================================================')
    print('=================================================')
    print(grouped)
    return
# =============================================================================================
# Plot future estimates from MC evaluation


def plot_future_finances(mc_file, daily_log):
    mc_data = pd.read_csv(mc_file, parse_dates=[0], dtype={'Date': str, 'Maximum': float,
                                                           'Mean': float, 'Minimum': float})
    mc_data = mc_data.set_index("Date")

    actual_data = pd.read_csv(daily_log, parse_dates=[0], dtype={'Date': str,
                                                                 'Checking': float,
                                                                 'Savings': float})
    actual_data = actual_data.set_index("Date")
    date_index = pd.date_range(mc_data.index.min(), actual_data.index.max())
    actual_info = actual_data['Checking'][date_index.max().date():date_index.min().date()]
    actual_info = actual_info[::-1]
    delta = (date_index[len(date_index) - 1] - date_index[0]).days + 1
    fig, td_plot = plt.subplots()
    if delta <= 15:
        myfmt = mdates.DateFormatter('%d')
        td_plot.xaxis.set_major_locator(mdates.DayLocator())
    elif delta <= 180:
        myfmt = mdates.DateFormatter('%b-%y')
        td_plot.xaxis.set_major_locator(mdates.MonthLocator())
    else:
        myfmt = mdates.DateFormatter('%b-%y')
        td_plot.xaxis.set_major_locator(plt.MaxNLocator(7))
        # td_plot.xaxis.set_major_locator(mdates.MonthLocator())
    td_plot.xaxis.set_major_formatter(myfmt)

    matplotlib.rc('xtick', labelsize=18)
    matplotlib.rc('ytick', labelsize=18)
    td_plot.set_xlabel('Date', fontsize=18)
    td_plot.set_ylabel('Account Value ($)', fontsize=18)
    td_plot.fill_between(mc_data.index, mc_data['Maximum'], mc_data['Minimum'],
                         color='red', interpolate=True)
    td_plot.plot(mc_data.index, mc_data['Mean'], label='Mean', color='black')
    td_plot.plot(date_index, actual_info, color='blue', label='Actual')
    plt.legend(loc=4)
    plt.savefig('../Input_Files/MC_Plot.png')
    plt.close()

    mid_delta = actual_data['Checking'][pd.to_datetime('today').date()] - \
                mc_data['Mean'][pd.to_datetime('today').date()]
    upper_delta = actual_data['Checking'][pd.to_datetime('today').date()] - \
                  mc_data['Maximum'][pd.to_datetime('today').date()]
    lower_delta = actual_data['Checking'][pd.to_datetime('today').date()] - \
                  mc_data['Minimum'][pd.to_datetime('today').date()]

    print('{}{}'.format('Upper Delta: ', round(float(upper_delta), 2)))
    print('{}{}'.format('Lower Delta: ', round(float(lower_delta), 2)))
    print('{}{}'.format('Average Delta: ', round(float(mid_delta), 2)))
    return
# =============================================================================================
# eof
