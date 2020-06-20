import os
import csv

month_count = 0 
total_revenue = 0 
int_revenue = 0 
profit_change = 0
total_change = 0
average_change = []
running_tot = 0
running_diff = 0 
diff_tot =0 
last_amt = 0
greatest_inc = 0 
max_val = 0
min_val = 1000000000





budget_csv = os.path.join('..', 'Resources','budget_data.csv')
#output_path = os.path.join('..', 'output, 'Analysis.txt')



# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    

    # Read through each row of data after the header
    for row in csvreader:
        month_count += 1
        total_revenue += int(row[1])
        average_change.append(int(row[1]))
        avg_change = round(sum(average_change)/ month_count, 2)
        running_tot = running_tot + total_revenue
        running_diff = total_revenue - last_amt
        last_amt = total_revenue
        diff_tot = diff_tot + running_diff

        avg_diff = (round(diff_tot/ month_count - 1), 2)

        if int(row[1]) > max_val:
            max_val = int(row[1])
            greatest_month = str(row[0])
        
        if int(row[1]) < min_val:
            min_val = int(row[1])
            lowest_month = str(row[0])

    

      


print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${avg_diff}")
print(f"Greatest Increase in Profits: {greatest_month} (${max_val})")
print(f"Greatest Decrease in Profits: {lowest_month} (${min_val})")


output_path = os.path.join('..', 'analysis', 'analysis.txt')
#output to text file

with open(output_path,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Total Revenue: ${total_revenue}" + "\n")
    #text.write(f"Average Change: ${avg_change}" + "\n")
    text.write(f"Greatest Increase in Profits: {greatest_month} (${max_val}" + "\n")
    text.write(f"Greatest Decrease in Profits: {lowest_month} (${min_val})" + "\n")






