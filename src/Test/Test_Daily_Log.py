from File_Readers.Read_Expenses import read_expense_file
from Data_Processing.Iterator import daily_account_value

import unittest
import pandas as pd
from datetime import date
# =============================================================================================
# =============================================================================================
# Date:    December 22, 2017
# Purpose: This class tests the ability to write a daily log file

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
# Version: 1.0
# =============================================================================================
# =============================================================================================


class TestDailyLog(unittest.TestCase):
    def test_daily_log(self):
        check_start = 8500.0
        savings_start = 4000.0
        start_date = pd.to_datetime('2015-1-1').date()
        end_date = pd.to_datetime('2015-1-7').date()
        data = read_expense_file('../Data/VandV/ReadExpenses/Read_File.csv')
        daily_account_value(check_start, savings_start, start_date, end_date,
                            data, '../Data/VandV/ReadExpenses/Log_File.csv')


if __name__ == '__main__':
    unittest.main()
