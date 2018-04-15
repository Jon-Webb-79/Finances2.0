# Import modules here
import pandas as pd
import numpy as np
from datetime import date
# =============================================================================================
# =============================================================================================
# Date:    December 22, 2017
# Purpose: This module iterates through dates to complete certain actions

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
# =============================================================================================
# =============================================================================================
# Generator function for iterating through dates


def daily_account_value(checking_start, savings_start, start_date,
                        end_date, dataframe, directory):
    """

    :param checking_start: float
                           The initial value of the checking account \
                           in units of dollars U.S.
    :param savings_start:  float
                           The initial value of the savings account \
                           in units of dollars U.S.
    :param start_date: object
                       The start date as a datetime object (Year, Month, Day)
    :param end_date: object
                     The end date as a datetime object (Year, Month, Day)
    :param dataframe: object
                      The pandas dataframe containing expense information
    :param directory: char str
                      The file name being read to include the relative or
                      absolute path length
    :return: NA:

    This function reads in expense information and uses it to create a \
    .csv file with the value of checking and savings account at each \
    day between the start_date and end_date.
    """
    grp_df = dataframe.groupby('Date').sum()
    dataframe = dataframe.set_index("Date")
    delta = pd.Timedelta('1 days')
    expense_report = []
    while start_date <= end_date:
        if start_date in dataframe.index:
            savings_start += (grp_df.loc[start_date, "Savings_Addition"] -
                              grp_df.loc[start_date, "Savings_Debit"])
            checking_start += (grp_df.loc[start_date, "Checking_Addition"] -
                               grp_df.loc[start_date, "Checking_Debit"])
            expense_report.append([start_date, round(float(checking_start), 2),
                                   round(float(savings_start), 2)])
        elif start_date not in dataframe.index:
            expense_report.append([start_date, round(float(checking_start), 2),
                                   round(float(savings_start), 2)])
        start_date += delta
    # Create new dataframe
    df_exp_rpt = pd.DataFrame(expense_report, columns=["Date", "Checking", "Savings"])
    df_exp_rpt = df_exp_rpt[::-1]
    df_exp_rpt.to_csv(directory, index=False)
    return
# =============================================================================================
 # This function iterates over dates to produce totao expenses in each day

def histogram_values(start_date, end_date, dataframe, expense):
    """

    :param start_date: object
                       The start date as a datetime object (Year, Month, Day)
    :param end_date: object
                     The end date as a datetime object (Year, Month, Day)
    :param dataframe: object
                      The pandas dataframe containing expense information
    :param expense: char str
                      The type of expense being that a histogram is \
                      being generated for
    :return: hist_data: float
                        An array containing the total expense on each \
                        day

    This function reads in expense information and uses it to create an \
    array with the spending information on each day.
    """
    pd.to_datetime(dataframe['Date'])
    dataframe = dataframe.set_index("Date")
    delta = pd.Timedelta('1 days')
    array = []
    date = []
    while start_date <= end_date:
        if start_date in dataframe.index:
            timestamp = dataframe[str(start_date)]
            i = 0
            summation = 0.0
            for eachItem in timestamp['Expense_Type']:
                if eachItem == expense:
                    summation += timestamp['Checking_Debit'][i]
                i += 1
            date.append(start_date)
            array.append(summation)
        else:
            date.append(start_date)
            array.append(0.0)
        start_date += delta
    return array, date
# =============================================================================================
# This function will iterate over an expense file to sum an expense type


def sum_expense(start_date, end_date, dataframe, keyword, expense_type):
    pd.to_datetime(dataframe['Date'])
    dataframe = dataframe.set_index("Date")
    delta = pd.Timedelta('1 days')
    summation = 0.0
    while start_date <= end_date:
        if start_date in dataframe.index:
            timestamp = dataframe[str(start_date)]
            i = 0
            for eachItem in timestamp[expense_type]:
                if eachItem == keyword:
                    summation += timestamp['Checking_Debit'][i] + \
                                 timestamp['Checking_Addition'][i]
                i += 1
        start_date += delta
    return summation
# =============================================================================================
# =============================================================================================
# eof
