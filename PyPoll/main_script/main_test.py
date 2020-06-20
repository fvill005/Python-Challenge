import csv
import os

#csvpath = os.path.join('..', 'Resources', 'election_data.csv')
#csvpath = os.path.join('main_script', 'election_data.csv')

file = '../Resources/election_data.csv'

with open (file, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
#
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
