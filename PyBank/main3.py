import os
import csv

# path to csvfile
csvpath = os.path.join('Resources', 'budget_data.csv')

# variables
total_months = 0
net_profit = 0 
current_month_profit = 0
previous_month_profit = 867884
profit_change = 0
profit_changes = []
months = []

# Read csvfile
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # For loop to read each row after header
    for row in csvreader:
        total_months +=1
        months.append(row[0])
        net_profit += int(row[1])
        current_month_profit = int(row[1])
        if total_months > 1:
            profit_change = current_month_profit - previous_month_profit
            profit_changes.append(profit_change)
            previous_month_profit = current_month_profit

# month by month results
sum_profit_changes = sum(profit_changes)
average_change = round(sum_profit_changes / (total_months-1), 2)
max_change = max(profit_changes)
min_change = min(profit_changes)
max_month = months[profit_changes.index(max_change) + 1]
min_month = months[profit_changes.index(min_change) + 1]

# Print summary
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${net_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

# Output summary to txt
save_file = csvpath.strip(".csv") + "_results.txt"
csvpath = os.path.join(save_file)
with open(csvpath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {total_months}" + "\n")
    text.write(f"Total Revenue: ${net_profit}" + "\n")
    text.write(f"Average Revenue Change: ${average_change}" + "\n")
    text.write(f"Greatest Increase in Revenue: {max_month} (${max_change})" + "\n")
    text.write(f"Greatest Decrease in Revenue: {min_month} (${min_change})" + "\n")