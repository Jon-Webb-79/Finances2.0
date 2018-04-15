# Import modules here
from Containers.OptionsContainer import OptionsContainer
from File_Readers.Read_Options_File import ReadOptions
from Run_Modules.Run_Options import organize_expense_file_by_date, draft_daily_log_file
from Run_Modules.Run_Options import plot_time_history, sum_account_values
from Run_Modules.Run_Options import create_histogram_tables, tabulate_expense, vendor_expenses
from Run_Modules.Run_Options import plot_future_finances
# =============================================================================================
# =============================================================================================
# Date:    December 21, 2017
# Purpose: This class tests the ReadOptions class

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = 2.0
# =============================================================================================
# =============================================================================================
# Initialize files and file readers
container = OptionsContainer()
reader = ReadOptions(container)
reader.read_file('../Input_Files/RunOptions.txt')
if container.organize_expense_file.upper() == 'YES':
    organize_expense_file_by_date(container.expense_file_name)
if container.draft_daily_history.upper() == 'YES':
    draft_daily_log_file(container.checking_start_value, container.savings_start_value,
                         container.expense_file_name, container.account_log_file_name,
                         container.log_end_date)
if container.plot_account_history.upper() == 'YES':
    plot_time_history(container.account_log_file_name, container.history_start_date,
                      container.history_end_date)
if container.sum_account_values.upper() == 'YES':
    sum_account_values(container.sum_start_date, container.sum_end_date,
                       container.expense_file_name)
if container.create_histogram_tables.upper() == 'YES':
    create_histogram_tables(container.expense_file_name, container.histogram_directory,
                            container.histogram_end_date)
if container.tabulate_expense.upper() == 'YES':
    tabulate_expense(container.expense_file_name, container.expense_type,
                     container.expense_keyword, container.expense_start_date,
                     container.expense_end_date)
if container.sum_vendors.upper() == 'YES':
    vendor_expenses(container.expense_file_name, container.vendor_start_date,
                    container.vendor_end_date)
if container.plot_future.upper() == 'YES':
    plot_future_finances('../../Monte_Economix/Input_Files/Checking.csv',
                         container.account_log_file_name)
# =============================================================================================
# =============================================================================================
# eof
