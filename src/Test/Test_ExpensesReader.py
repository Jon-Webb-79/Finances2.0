from File_Readers.Read_Expenses import read_expense_file, sort_dataframe_by_date

import unittest
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


class TestReadExpenses(unittest.TestCase):
    # Test the ability to properly read in an expense file

    def test_file_reader(self):
        data = read_expense_file('../Data/VandV/ReadExpenses/Read_File.csv')
        dates = ['2015-01-05', '2015-01-01', '2015-01-02', '2015-01-02', '2015-01-02',
                 '2015-01-05', '2015-01-03', '2015-01-07', '2015-01-07', '2015-01-07',
                 '2015-01-02']
        check_debit = [75.00, 45.00, 245.00, 1280.00, 75.00, 55.00, 287.00, 3185.0, 981.00, 342.10,
                       64.80]
        check_add = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        savings_debit = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        savings_add = [0.0, 0.0, 0.0, 0.0, 75.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        exp_type = ['Bar', 'Misc', 'Misc', 'Bills', 'Transfer', 'Restaurant',
                    'Misc', 'Paycheck', 'Fed Taxes', 'State Taxes', 'Groceries']
        vendor = ['The Pub', 'JC Penny', 'Amazon', 'Apartment Complex',
                  'Checking to Savings', 'Olive Garden', 'Car Dealer', 'My Company',
                  'Federal Income Tax', 'Utah State Income Tax', 'Fresh Market']
        descript = ['None', 'Jeans', 'Camera', 'Rent', 'Savings Account', 'Dinner',
                    'Oil Change', 'Paycheck', 'Income Tax', 'Income Tax', 'Party']

        self.assertTrue((dates == data['Date']).all())
        self.assertTrue((check_debit == data['Checking_Debit']).all())
        self.assertTrue((check_add == data['Checking_Addition']).all())
        self.assertTrue((savings_debit == data['Savings_Debit']).all())
        self.assertTrue((savings_add == data['Savings_Addition']).all())
        self.assertTrue((exp_type == data['Expense_Type']).all())
        self.assertTrue((vendor == data['Vendor']).all())
        self.assertTrue((descript == data['Description']).all())
#        grouped = data.groupby('Expense_Type').Checking_Debit.sum()
#        print(grouped)
# =============================================================================================
    # Test the ability to throw an exception for the wrong expense type

    def test_exception_handling(self):
        try:
            read_expense_file('../Data/VandV/ReadExpenses/Exception.csv')
            self.assertEqual(1, 0)
        except SystemExit:
            self.assertEqual(1, 1)
        return
# =============================================================================================
    # Test the ability to reorganize a datafile by date

    def test_sort_file_by_date(self):
        data = read_expense_file('../Data/VandV/ReadExpenses/Read_File.csv')
        sort_dataframe_by_date(data, '../Data/VandV/ReadExpenses/Read_File.csv',
                               test=True)
        new_data = read_expense_file('../Data/VandV/ReadExpenses/Read_FileTemp.csv')
        date = ['2015-01-07', '2015-01-07', '2015-01-07', '2015-01-05', '2015-01-05',
                '2015-01-03', '2015-01-02', '2015-01-02', '2015-01-02', '2015-01-02',
                '2015-01-01']
        check_debit = [342.1, 981.0, 3185.0, 55.0, 75.0, 287.0, 64.8, 75.0,
                       1280.0, 245.0, 45.0]
        check_add = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        savings_debit = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        savings_add = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 75.0, 0.0, 0.0, 0.0]
        expense = ['State Taxes', 'Fed Taxes', 'Paycheck', 'Restaurant',
                   'Bar', 'Misc', 'Groceries', 'Transfer', 'Bills', 'Misc',
                   'Misc']
        descript = ['Income Tax', 'Income Tax', 'Paycheck', 'Dinner', 'None',
                    'Oil Change', 'Party', 'Savings Account', 'Rent', 'Camera',
                    'Jeans']
        self.assertTrue((date == new_data['Date']).all())
        self.assertTrue((check_debit == new_data['Checking_Debit']).all())
        self.assertTrue((check_add == new_data['Checking_Addition']).all())
        self.assertTrue((savings_debit == new_data['Savings_Debit']).all())
        self.assertTrue((savings_add == new_data['Savings_Addition']).all())
        self.assertTrue((expense == new_data['Expense_Type']).all())
        self.assertTrue((descript == new_data['Description']).all())
        return
# =============================================================================================
# =============================================================================================


if __name__ == '__main__':
    unittest.main()
# eof
