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

print('Financial Analysis')
print('-' * 30)

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
average_change = np.mean(np.diff(df['Profit/Losses']))
print(f'Average Change: ${round(average_change, 2)}')

'''
average_change = np.mean(df['Profit/Losses'])

greatest_increase = np.max(df['Profit/Losses'])
greatest_decrease = np.min(df['Profit/Losses'])

greatest_increase_date = df['Date'][np.argmax(df['Profit/Losses'])]
print(diff_date, total, average_change)
print(greatest_increase, greatest_decrease)
print(greatest_increase_date)
'''
