# Title: Python challange
# Author: David Jaimes
# Email: david@djaimes.com
# Web: https://djaimes.com
# Due Date: 2019 December 02
# UCSD Extension: Data Science and Visualization Boot Camp
# Conda Version: 4.7.12
# Python Version: 3.7.4

import pandas as pd
import numpy as np
import sys

# Make class to make all Print function write to console and text file.
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('budget_data_djaimes.txt', 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
sys.stdout = Logger()

print('Financial Analysis')
print('-' * 28)

# Find Total Number of Unique Months.
# This code will omit any repeated months of the same year.
df = pd.read_csv('budget_data.csv', parse_dates=[0])
dates = pd.DatetimeIndex(df['Date'])
unique_months = np.unique(dates.year + dates.month / 12)
print(f'Total Months: {len(unique_months)}')

# Find the Net Total of "Profit/Losses" Column.
net_total = np.sum(df['Profit/Losses'])
print(f'Total: ${net_total}')

# Find the Average of the Changes in "Profit/Losses" Column.
# For chronological accuracy, I'll sort by "Date" before finding difference
# between adjacent elements.
sorted_df = df.sort_values(by='Date')
average_change = np.mean(np.diff(sorted_df['Profit/Losses']))
print(f'Average Change: ${round(average_change, 2)}')

# Find the Greatest Increase in Profits (Date and Amount) and Find the Greatest
# Decrease in Losses (Date and Amount).
txt_max = 'Greatest Increase in Profits: '
txt_min = 'Greatest Decrease in Losses: '
for x, y, z in [[np.argmax, np.max, txt_max], [np.argmin, np.min, txt_min]]:
    index = x(np.array(df['Profit/Losses']))
    great_date = df['Date'][index].strftime('%b-%Y')
    great_money = y(df['Profit/Losses'])
    print(z + f'{great_date} (${great_money})')
