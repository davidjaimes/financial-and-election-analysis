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

with open('election_data.csv', newline='') as csvfile:
    reader = csvreader(csvfile, delimiter=',')
    header = next(reader)

    # set 1st column as string and 2nd column as integer.
    data = np.array([tuple(row) for row in reader], dtype=('i4, U25, U25'))
    voter_id, county, candidate = data['f0'], data['f1'], data['f2']

    # compute areas of interest for election analysis.
    total_votes = len(voter_id)
    unique, counts = np.unique(candidate, return_counts=True)
    ind_sort = np.argsort(counts)[::-1]

    # custom function to print to screen and file.
    def cprint(text):
        print(text)
        with open('election_results.txt', 'a') as fname:
            print(text, file=fname)

    # print election results to console and file with cprint custom function.
    cprint('Election Results')
    cprint('-' * 28)
    cprint(f'Total Votes: {total_votes}')
    cprint('-' * 28)
    for ind in ind_sort:
        percent = round(100 * counts[ind] / total_votes, 3)
        cprint(f'{unique[ind]}: {percent}% ({counts[ind]})')
    cprint('-' * 28)
    cprint(f'Winner: {unique[ind_sort][0]}')
    cprint('-' * 28)
