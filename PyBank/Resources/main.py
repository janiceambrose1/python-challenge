import os 
import csv 

PyBankcsv = os.path.join("Resources","budget_data.csv")
#lists
profit = []
monthly_changes = []
date = []

#initializing my variables 
count = 0
total = 0
change = 0
initial = 0

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count = count+1 

        date.append(row[0])

        profit.append(row[1])
        total = total + int(row[1])

        final_profit = int(row[1])
        monthly_changes = final_profit - initial

        monthly_changes.append(monthly)

        total = total + monthly
        initial = final_profit

        avg_profit = (total/count)

        increase = max(monthly)
        decrease = min(monthly)

print("Financial Analysis")
print("***********************")
print("Total Months:" + str(count))
print("Total Profit:" + str(total))
print("Average Change" + str(avg_profit))
print("Greatest Increase in Profits:" + str(increase))
print("Greatest Decrease in Proft" + str(decrease))
