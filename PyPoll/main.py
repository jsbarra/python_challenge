#Import Dependencies

import os
import csv

#Read CSV File/Provide Path

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, newline="") as data_file:
    data_reader = csv.reader(data_file, delimiter=",")
    print(data_reader)
    data_header = next(data_reader)
    print(data_header)

#Declare Variables for rows
    votes = []
    county = []
    candidates = []

 #Declare variables for candidate list (for count)  
    
    khan = []
    correy = []
    li = []
    otooley = []

#Loop through data 

    for row in data_reader:

# Append data to specific lists

        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

#Calculate total votes

    total_votes = (len(votes))
    print(total_votes)

#Votes per candidate

    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            votes_for_khan = len(khan)
        
        elif candidate == "Correy":
            correy.append(candidates)
            votes_for_correy = len(correy)
        
        elif candidate == "Li":
            li.append(candidates)
            votes_for_li = len(li)
        
        else:
            otooley.append(candidates)
            votes_for_otooley = len(otooley)
    
    print(votes_for_khan)
    print(votes_for_correy)
    print(votes_for_li)
    print(votes_for_otooley)

#Calculate percentages for each candidate

    khan_percent = round(((votes_for_khan / total_votes) * 100), 2)
    correy_percent = round(((votes_for_correy / total_votes) * 100), 2)
    li_percent = round(((votes_for_li / total_votes) * 100), 2)
    otooley_percent = round(((votes_for_otooley / total_votes) * 100), 2)

    print(khan_percent)
    print(correy_percent)  
    print(li_percent)
    print(otooley_percent)

#Find the winner by using if statements

if votes_for_khan > max(votes_for_correy, votes_for_li, votes_for_otooley):
    winner = "Khan"

elif votes_for_correy > max(votes_for_khan, votes_for_li, votes_for_otooley):
    winner = "Correy"

elif votes_for_li > max(votes_for_correy, votes_for_khan, votes_for_otooley):
    winner = "Li"

else:
    winner = "O'Tooley"



print("-------------------")
print("Election Results")
print("-------------------")
print("Total Votes:" + str(total_votes))
print("-------------------")
print(f"Khan- {khan_percent}% : {votes_for_khan}")
print(f"Correy- {correy_percent}% : {votes_for_correy}")
print(f"Li- {li_percent}% : {votes_for_li}")
print(f"O'Tooley- {otooley_percent}% : {votes_for_otooley}")
print("-------------------")
print(f"Winner- {winner}")


#Output Analysis to text file

output_file = "election_results.txt"

with open(output_file, 'w', newline="") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("Total Votes: " + str(total_votes))
    file.write("\n")
    file.write(f"Khan- {khan_percent}% : {votes_for_khan}")
    file.write("\n")
    file.write(f"Correy- {correy_percent}% : {votes_for_correy}")
    file.write("\n")
    file.write(f"Li- {li_percent}% : {votes_for_li}")
    file.write(f"\n")
    file.write(f"O'Tooley - {otooley_percent}% : {votes_for_otooley}")


