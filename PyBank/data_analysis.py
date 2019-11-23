# Title: Python challange
# Author: David Jaimes
# Email: david@djaimes.com
# Web: https://djaimes.com
# Due Date: 2019 December 02
# UCSD Extension: Data Science and Visualization Boot Camp
# Conda Version: 4.7.12
# Python Version: 3.7.4

from csv import reader as csvreader
import numpy as np

with open('budget_data.csv', newline='') as csvfile:
    reader = csvreader(csvfile, delimiter=',')
    header = next(reader)

    # set 1st column as string and 2nd column as integer.
    data = np.array([tuple(row) for row in reader], dtype=('U25, i4'))
    dates, pl = data['f0'], data['f1']

    # compute areas of interest for financial analysis.
    total_months= len(np.unique(dates))
    net_total = np.sum(pl)
    average_change = np.mean(np.diff(pl))

    # print financial analysis to console.
    print('Financial Analysis')
    print('-' * 28)
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${round(average_change, 2)}')
    for x, y in zip([np.argmax(pl), np.argmin(pl)], ['Increase', 'Decrease']):
        print(f'Greatest {y} in Profits: {dates[x]} (${pl[x]})')
