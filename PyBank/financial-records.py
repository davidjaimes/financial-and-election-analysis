# Title: Python challange
# Author: David Jaimes
# Email: david@djaimes.com
# Web: https://djaimes.com
# Due Date: 2019 December 02
# UCSD Extension: Data Science and Visualization Boot Camp
# Conda Version: 4.7.12
# Python Version: 3.7.4

import csv
import numpy as np
import sys

# make class to write print pfunctions to console and text file.
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('financial_analysis.txt', 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
sys.stdout = Logger()

with open('budget_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)

    # set 1st column as string and 2nd column as integer.
    dt = np.dtype([(header[0], 'U25'), (header[1], 'i4')])
    data = np.array([(row[0], row[1]) for row in reader], dtype=dt)
    dates, pl = data[header[0]], data[header[1]]

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
