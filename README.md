### Background

Analyze two real-world situtations with Python programming language. You are given Financial Records from a private business and Election Poll results from a fictitous state. Read the CSV files and summarize the important points of each dataset.

### Financial Records

First few lines of the CSV file:
```
Date,Profit/Losses
Jan-2010,867884
Feb-2010,984655
Mar-2010,322013
Apr-2010,-69417
May-2010,310503
Jun-2010,522857
Jul-2010,1033096
Aug-2010,604885
Sep-2010,-216386
```

The Python script analyzes the financial records calculates each of the following:
   - The total number of months included in the dataset
   - The total net amount of "Profit/Losses" over the entire period
   - The average change in "Profit/Losses" between months over the entire period
   - The greatest increase in profits (date and amount) over the entire period
   - The greatest decrease in losses (date and amount) over the entire period

Description | Value
--- | --- 
Total Months | 86
Total | $38,382,578.00
Average Change | -$2315.12
Greatest Increase in Profits | Feb-2012 ($1,170,593.00)
Greatest Decrease in Profits | Sep-2013 (-$1,196,225.00)

### Election Records

First few lines of the CSV file:
```
Voter ID,County,Candidate
12864552,Marsh,Khan
17444633,Marsh,Correy
19330107,Marsh,Khan
19865775,Queen,Khan
11927875,Marsh,Khan
19014606,Marsh,Li
17775191,Queen,Correy
14003692,Marsh,Khan
14255761,Marsh,Khan
```


The Python script analyzes the votes and calculates each of the following:
  - The total number of votes cast
  - A complete list of candidates who received votes
  - The percentage of votes each candidate won
  - The total number of votes each candidate won
  - The winner of the election based on popular vote.

Candidate | Votes
--- | ---
Khan | 63.0% (2218231)
Correy | 20.0% (704200)
Li | 14.0% (492940)
O'Tooley | 3.0% (105630)

Description | Value
--- | ---
Total Votes | 3521001
Winner | Khan
