import os
import csv

# path to csvfile
csvpath = os.path.join('Resources', 'election_data.csv')

# variables

total_votes = 0
candidates = []
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = 0

# Read csvfile
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # For loop to read each row after header
    for row in csvreader:
        total_votes += 1
        i = (row[2])
        #candidates.append(row[2])

        # Conditional to count votes
        if i in candidate_votes:
            candidate_votes[i] += 1
        else:
            candidate_votes[i] = 1

        # For loop to calculate candidate percentages
        #for key in candidate_votes.items():
            #votes = candidate_votes.get(key)
            #percent = (round((votes/ total_votes), 3)) * 100
            #candidate_percentages[key] = percent

            #if votes > winner_votes:
               # winner_votes = votes
                #winner = key

#print summary
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
for key, votes in candidate_votes.items():
    percent = (votes/total_votes)*100
    print(f"{key}: {percent}% ({votes})")
    print("-----------------------------")
    if votes > winner_votes:
                winner_votes = votes
                winner = key
print(f"Winner: {winner}")
print("-----------------------------")