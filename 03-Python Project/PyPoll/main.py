import os 
import csv

election_data = os.path.join('election_data.csv')

total_votes_cast = 0
percentage_of_votes = []
candidatesList = []  
total_number_of_votes = []
dataPoll = {}
winner_of_election = []

with open(election_data, 'r') as csvfile:
   
    csvread_election_dataFile = csv.reader(csvfile)
    
    next(csvread_election_dataFile, None)

    for row in csvread_election_dataFile:
       
        total_votes_cast = total_votes_cast + 1
        
        if row[2] in dataPoll.keys():
            dataPoll[row[2]] = dataPoll[row[2]] + 1
        else:
            dataPoll[row[2]] = 1

    for key, value in dataPoll.items():
        candidatesList.append(key)
        total_number_of_votes.append(value)
  
    for n in total_number_of_votes:
        percentage_of_votes.append(round(n / total_votes_cast * 100, 1))
 
    new_election_data = list(zip(candidatesList, total_number_of_votes, percentage_of_votes))
    

    for candidateName in new_election_data:
        if max(total_number_of_votes) == candidateName[1]:
            winner_of_election.append(candidateName[0])
            electionWinner = winner_of_election[0]

print ("Election Results")
print("-----------------------------")
print("Total Votes: " + str(total_votes_cast)) 
print("-----------------------------")
for count in range(len(candidatesList)):
    print(f"{candidatesList[count]}: {percentage_of_votes[count]}% ({total_number_of_votes[count]})")
print("-----------------------------") 
print("Winner: " +electionWinner)
print("-----------------------------")

csvwriter = open("output.txt", "w+")
csvwriter.write("Election Results")
csvwriter.write("\n")
csvwriter.write("-----------------------------")
csvwriter.write("\n") 
csvwriter.write('\n' + "Total Votes:  " + str(total_votes_cast)) 
csvwriter.write("\n")
csvwriter.write("-----------------------------")
csvwriter.write("\n")
for count in range(len(candidatesList)):
    csvwriter.write(f"{candidatesList[count]}: {percentage_of_votes[count]}% ({total_number_of_votes[count]})\n")
csvwriter.write("\n")
csvwriter.write("-----------------------------")
csvwriter.write("\n") 
csvwriter.write("Winner:  " + electionWinner)
csvwriter.write("\n")
csvwriter.write("-----------------------------") 