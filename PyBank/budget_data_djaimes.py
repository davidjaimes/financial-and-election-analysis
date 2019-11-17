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
# For chronological accuracy, I'll sort by "Date" before finding difference
# between adjacent elements.
sorted_df = df.sort_values(by='Date')
average_change = np.mean(np.diff(sorted_df['Profit/Losses']))
print(f'Average Change: ${round(average_change, 2)}')

# Find the Greatest Increase in Profits (Date and Amount).
gr8_increase_date = df['Date'][np.argmax(np.array(df['Profit/Losses']))]
gr8_increase_date = gr8_increase_date.strftime('%b-%Y')
gr8_increase = np.max(df['Profit/Losses'])
print(f'Greatest Increase in Profits: {gr8_increase_date} (${gr8_increase})')

# Find the Greatest Decrease in Losses (Date and Amount).
gr8_decrease_date = df['Date'][np.argmin(np.array(df['Profit/Losses']))]
gr8_decrease_date = gr8_decrease_date.strftime('%b-%Y')
gr8_decrease = np.min(df['Profit/Losses'])
print(f'Greatest Decrease in Losses: {gr8_decrease_date} (${gr8_decrease})')
