# Date:    December 21, 2017
# Purpose: This class acts as a data structure

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
# Version: 1.0
# =============================================================================================
# =============================================================================================


class OptionsContainer:
    def __init__(self):
        self.organize_expense_file = 'NO'
        self.draft_daily_history = 'NO'
        self.plot_account_history = 'NO'
        self.sum_account_values = 'NO'
        self.create_histogram_tables = 'NO'
        self.tabulate_expense = 'NO'
        self.sum_vendors = 'NO'
        self.plot_future = 'NO'

        self.expense_file_name = 'NA'
        self.account_log_file_name = 'NA'
        self.history_plot_name = 'NA'
        self.histogram_directory = 'NA'
        self.expense_type = 'NA'
        self.expense_keyword = 'NA'

        self.log_end_date = 'NA'
        self.histogram_end_date = 'NA'
        self.history_start_date = 'NA'
        self.history_end_date = 'NA'
        self.sum_start_date = 'NA'
        self.sum_end_date = 'NA'
        self.hist_start_date = 'NA'
        self.hist_end_date = 'NA'
        self.expense_start_date = 'NA'
        self.expense_end_date = 'NA'
        self.vendor_start_date = 'NA'
        self.vendor_end_date = 'NA'

        self.checking_start_value = -20.0
        self.savings_start_value = -20.0
# eof
