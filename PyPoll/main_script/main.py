import os
import csv

total_votes = 0
candidates = []
candidates_votes = {}


election = os.path.join('..', 'Resources','election_data.csv')

with open (election) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    #print (f"CSV Header: {csv_header}")

    for row in csvreader:
        total_votes += 1
        candidates_name= row[2]

        if candidates_name not in candidates:
            candidates.append(candidates_name)
            candidates_votes[candidates_name] = +1
            #candidates_votes[candidates_name] = candidates_votes[candidates_name] + 1
    
    
   



print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
#print(candidates)
print(candidates_votes)

print("----------------------------------------")
print("Winner:")
print("----------------------------------------")


