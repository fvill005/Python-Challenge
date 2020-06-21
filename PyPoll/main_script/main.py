import os
import csv

#declare variables, list, dict
total_votes = 0
candidates = []
candidates_votes = []
election_results = {}
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0 

#find file and read data
election = os.path.join('..', 'Resources','election_data.csv')

with open (election) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)

    #tally the total votes
    for row in csvreader:
        total_votes += 1
        candidates_name= row[2]

        #find the candidates
        if candidates_name not in candidates:
            candidates.append(candidates_name)
         #found 4 candidates who recieved votes, and add up each time their name appears    
        if candidates_name == "Khan":
            Khan_votes += 1
        elif candidates_name == "Correy":
            Correy_votes += 1
        elif candidates_name == "Li":
            Li_votes += 1
        elif candidates_name == "O'Tooley":
            Otooley_votes += 1
    
    #find percentage of votes
    khan_percent = (Khan_votes/total_votes) *100
    correy_percent = (Correy_votes/total_votes) *100
    li_percent = (Li_votes/total_votes) *100
    otooley_percent = (Otooley_votes/total_votes) *100

    #find out who won
    election_results ={"Khan": khan_percent, 
                        "Correy": correy_percent, 
                        "Li": li_percent, 
                        "O'Tooley": otooley_percent}
    #results
    max_key = max(election_results, key = election_results.get)

           
    
    
   


#print to terminal 
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
print(f"Khan: {khan_percent: .3f}% ({Khan_votes})")
print(f"Correy: {correy_percent: .3f}% ({Correy_votes})")
print(f"Li: {li_percent: .3f}% ({Li_votes})")
print(f"O'Tooley: {otooley_percent: .3f}% ({Otooley_votes})")
print("----------------------------------------")
print(f"Winner: {max_key}")
print("----------------------------------------")

#create text file 
output_path = os.path.join('..', 'analysis', 'analysis.txt')
#output to text file

with open(output_path,'w') as text:
    text.write("Election Results" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Votes: {total_votes}" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Khan: {khan_percent: .3f}% ({Khan_votes})"+ "\n")
    text.write(f"Correy: {correy_percent: .3f}% ({Correy_votes})"+ "\n")
    text.write(f"Li: {li_percent: .3f}% ({Li_votes})" + "\n")
    text.write(f"O'Tooley: {otooley_percent: .3f}% ({Otooley_votes})" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Winner: {max_key}" + "\n")
    text.write("----------------------------------------" + "\n")

