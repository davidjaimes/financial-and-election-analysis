import pandas as pd
import numpy as np

df = pd.read_csv('budget_data.csv', parse_dates=[0])
diff_date = df['Date'].max() - df['Date'].min()
total = np.sum(df['Profit/Losses'])
average_change = np.mean(df['Profit/Losses'])

greatest_increase = np.max(df['Profit/Losses'])
greatest_decrease = np.min(df['Profit/Losses'])

greatest_increase_date = df['Date'][np.argmax(df['Profit/Losses'])]
print(diff_date, total, average_change)
print(greatest_increase, greatest_decrease)
print(greatest_increase_date)
