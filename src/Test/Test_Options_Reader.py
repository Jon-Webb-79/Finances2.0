# Import modules here
from Containers.OptionsContainer import OptionsContainer
from File_Readers.Read_Options_File import ReadOptions

import unittest
import numpy as np
from datetime import date
# =============================================================================================
# =============================================================================================
# Date:    December 21, 2017
# Purpose: This class tests the ReadOptions class

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
# Version: 1.0
# =============================================================================================
# =============================================================================================


class TestReadOptions(unittest.TestCase):
    def setUp(self):
        self.container = OptionsContainer()
        self.reader = ReadOptions(self.container)
# =============================================================================================
    # Test input file for uppercase letters

    def test_read_file_uppercase(self):
        self.reader.read_file('../Data/VandV/ReadOptions/Uppercase_File.txt')
        self.assertEqual(self.container.organize_expense_file, 'YES')
        self.assertEqual(self.container.draft_daily_history, 'YES')
        self.assertEqual(self.container.plot_account_history, 'YES')
        self.assertEqual(self.container.sum_account_values, 'YES')
        self.assertEqual(self.container.create_histogram_tables, 'YES')
        self.assertEqual(self.container.plot_histograms, 'YES')
        self.assertEqual(self.container.expense_file_name,
                         '../Input_Files/Expense_File.csv')
        self.assertEqual(self.container.account_log_file_name,
                         '../Input_Files/Daily_Log.csv')
        self.assertEqual(self.container.checking_start_value, np.float32(3712.67))
        self.assertEqual(self.container.savings_start_value, np.float32(1441.35))
        self.assertEqual(self.container.history_plot_name,
                         '../Input_Files/Daily_Log.png')
        self.assertEqual(self.container.history_plot_name, '../Input_Files/Daily_Log.png')
        self.assertEqual(self.container.history_start_date, date(2012, 11, 1))
        self.assertEqual(self.container.history_end_date, date(2017, 12, 21))
        self.assertEqual(self.container.sum_start_date, date(2000, 1, 1))
        self.assertEqual(self.container.sum_end_date, date.today())
        self.assertEqual(self.container.histogram_directory, '../Input_Files/Histograms')
        self.assertEqual(self.container.hist_start_date, date(2000, 1, 1))
        self.assertEqual(self.container.hist_end_date, date(2000, 1, 11))
        return
# =============================================================================================
    # Test input file for lowercase letters

    def test_read_file_lowercase(self):
        self.reader.read_file('../Data/VandV/ReadOptions/Lowercase_File.txt')
        self.assertEqual(self.container.organize_expense_file, 'YES')
        self.assertEqual(self.container.draft_daily_history, 'YES')
        self.assertEqual(self.container.plot_account_history, 'YES')
        self.assertEqual(self.container.sum_account_values, 'YES')
        self.assertEqual(self.container.create_histogram_tables, 'YES')
        self.assertEqual(self.container.plot_histograms, 'YES')
        self.assertEqual(self.container.expense_file_name,
                         '../Input_Files/Expense_File.csv')
        self.assertEqual(self.container.account_log_file_name,
                         '../Input_Files/Daily_Log.csv')
        self.assertEqual(self.container.checking_start_value, np.float32(3712.67))
        self.assertEqual(self.container.savings_start_value, np.float32(1441.35))
        self.assertEqual(self.container.history_plot_name,
                         '../Input_Files/Daily_Log.png')
        self.assertEqual(self.container.history_plot_name, '../Input_Files/Daily_Log.png')
        self.assertEqual(self.container.history_start_date, date(2012, 11, 1))
        self.assertEqual(self.container.history_end_date, date(2017, 12, 21))
        self.assertEqual(self.container.sum_start_date, date(2000, 1, 1))
        self.assertEqual(self.container.sum_end_date, date.today())
        self.assertEqual(self.container.histogram_directory, '../Input_Files/Histograms')
        self.assertEqual(self.container.hist_start_date, date(2000, 1, 1))
        self.assertEqual(self.container.hist_end_date, date(2000, 1, 11))
        return
# =============================================================================================
    # Test input file for start date after end date

    def test_read_file_mixed_dates(self):
        try:
            self.reader.read_file('../Data/VandV/ReadOptions/Mixed_Dates.txt')
            self.assertEqual(1, 0)
        except SystemExit:
            self.assertEqual(1, 1)
        return
# =============================================================================================
    # Test input file for partially populated file

    def test_partial_file(self):
        self.reader.read_file('../Data/VandV/ReadOptions/Partial_File.txt')
        self.assertEqual(self.container.organize_expense_file, 'YES')
        self.assertEqual(self.container.draft_daily_history, 'YES')
        self.assertEqual(self.container.plot_account_history, 'NO')
        self.assertEqual(self.container.sum_account_values, 'NO')
        self.assertEqual(self.container.create_histogram_tables, 'YES')
        self.assertEqual(self.container.plot_histograms, 'YES')
        self.assertEqual(self.container.expense_file_name,
                         '../Input_Files/Expense_File.csv')
        self.assertEqual(self.container.account_log_file_name,
                         '../Input_Files/Daily_Log.csv')
        self.assertEqual(self.container.checking_start_value, np.float32(3712.67))
        self.assertEqual(self.container.savings_start_value, np.float32(1441.35))
        self.assertEqual(self.container.history_plot_name, 'NA')
        self.assertEqual(self.container.history_plot_name, 'NA')
        self.assertEqual(self.container.history_start_date, 'NA')
        self.assertEqual(self.container.history_end_date, 'NA')
        self.assertEqual(self.container.sum_start_date, 'NA')
        self.assertEqual(self.container.sum_end_date, 'NA')
        self.assertEqual(self.container.histogram_directory, '../Input_Files/Histograms')
        self.assertEqual(self.container.hist_start_date, date(2000, 1, 1))
        self.assertEqual(self.container.hist_end_date, date(2000, 1, 11))
        return
# =============================================================================================
# =============================================================================================


if __name__ == '__main__':
    unittest.main()
