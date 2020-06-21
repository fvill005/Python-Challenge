import os
import csv

#declare variables and lists
month_count = 0 
total_revenue = 0 
int_revenue = 0 
profit_change = 0
total_change = 0
average_change = []
total_profit = []
monthly_profit_change = []
greatest_inc = 0 
max_val = 0
min_val = 1000000000

#read in the data
budget_csv = os.path.join('..', 'Resources','budget_data.csv')


# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    

    # Read through each row of data after the header
    #find the total months and revenue 
    for row in csvreader:
        month_count += 1
        total_revenue += int(row[1])
        total_profit.append(int(row[1]))
        average_change.append(int(row[1]))
    

        #find the greatest and lowest months 
        if int(row[1]) > max_val:
            max_val = int(row[1])
            greatest_month = str(row[0])
        
        if int(row[1]) < min_val:
            min_val = int(row[1])
            lowest_month = str(row[0])
    
    #find the average change month over month 
    for i in range(len(total_profit)-1):
        #ind the change and add it to the list 
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# print to terminal 
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_revenue}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {greatest_month} (${max_val})")
print(f"Greatest Decrease in Profits: {lowest_month} (${min_val})")

#create text file and 
output_path = os.path.join('..', 'analysis', 'analysis.txt')
#output to text file

with open(output_path,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Total Revenue: ${total_revenue}" + "\n")
    text.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}" + "\n")
    text.write(f"Greatest Increase in Profits: {greatest_month} (${max_val})" + "\n")
    text.write(f"Greatest Decrease in Profits: {lowest_month} (${min_val})" + "\n")







