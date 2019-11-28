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

    # custom function to print to screen and file.
    def cprint(text):
        print(text)
        with open('financial_summary.txt', 'a') as fname:
            print(text, file=fname)

    # print financial analysis to console and file with cprint custom function.
    cprint('Financial Analysis')
    cprint('-' * 28)
    cprint(f'Total Months: {total_months}')
    cprint(f'Total: ${net_total}')
    cprint(f'Average Change: ${round(average_change, 2)}')
    args = zip([np.argmax(pl), np.argmin(pl)], ['Increase', 'Decrease'])
    for x, y in args:
        cprint(f'Greatest {y} in Profits: {dates[x]} (${pl[x]})')
