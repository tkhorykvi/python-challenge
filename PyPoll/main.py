import csv
import os

election_data_csv = os.path.join('Resources', 'election_data.csv')

votes = []
voterID = []
county = []
candidates = []
percentage_votes_won = []
total_votes_won = []
winner_popular_vote = []

with open(election_data_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_file = next(csvreader)
    # for line in csvreader:
        # print(line)    
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
        
total_votes = (len(votes))
print(total_votes)   

khan = []
correy = []
li = []
otooley = []

for candidate in candidates:
    if candidate == "Khan":
        khan.append(candidates)
        khan_votes_won = len(khan)
    elif candidate == "Correy":
        correy.append(candidates)
        correy_votes_won = len(correy)
    elif candidate == "Li":
        li.append(candidates)
        li_votes_won = len(li)
    else:
        otooley.append(candidates)
        otooley_votes_won = len(otooley)
print(khan_votes_won)
print(correy_votes_won)
print(li_votes_won)
print(otooley_votes_won)

khan_percent_votes = round((khan_votes_won/total_votes)*100,2)
correy_percent_votes = round((correy_votes_won/total_votes)*100,2)
li_percent_votes = round((li_votes_won/total_votes)*100,2)
otooley_percent_votes = round((otooley_votes_won/total_votes)*100,2)

print(khan_percent_votes)
print(correy_percent_votes) 
print(li_percent_votes) 
print(otooley_percent_votes)

if khan_percent_votes > max(correy_percent_votes, li_percent_votes, otooley_percent_votes):
    winner = "Khan"
elif correy_percent_votes > max(khan_percent_votes, li_percent_votes, otooley_percent_votes):
    winner = "Correy"
elif li_percent_votes > max(khan_percent_votes, correy_percent_votes, otooley_percent_votes):
    winner = "Li"
else:
    winner = "O'Tooley"

print(winner)    


name = "Election Results"
print(name)
print("-----------------------")
print("Total Votes: ", (total_votes))
print("-----------------------")
print("Khan: ", (khan_percent_votes),"% ", "(", (khan_votes_won), ")")
print("Correy ", (correy_percent_votes),"% ", "(", (correy_votes_won), ")")
print("Li: ", (li_percent_votes),"% ", "(", (li_votes_won), ")")
print("O'Tooley: ", (otooley_percent_votes),"% ", "(", (otooley_votes_won), ")")
print("-----------------------")
print("Winner: ", (winner))
print("-----------------------")

output_path = os.path.join("Resources", "analysis.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["Total Votes: ", (total_votes)])
    csvwriter.writerow(["Khan: ", (khan_percent_votes),"% ", "(", (khan_votes_won), ")"])
    csvwriter.writerow(["Correy ", (correy_percent_votes),"% ", "(", (correy_votes_won), ")"])
    csvwriter.writerow(["Li: ", (li_percent_votes),"% ", "(", (li_votes_won), ")"])
    csvwriter.writerow(["O'Tooley: ", (otooley_percent_votes),"% ", "(", (otooley_votes_won), ")"])
    csvwriter.writerow(["Winner: ", (winner)])

