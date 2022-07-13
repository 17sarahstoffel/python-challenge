#importing and createing modeules to read csv file
import os
import csv

election_data= os.path.join("Resources","election_data.csv")

#opening the csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #pulling the headers
    csv_header = next(csvfile)

    #creating variables, lists, and dictionary
    total_votes = 0
    candidate_names = []
    votes_for_candidate = {}
    winning_count = 0
    

    for row in csvreader:
        
        #finding total votes
        total_votes = total_votes + 1

        #finding the list of candidates and counting their votes
        candidates_complete_list = (row[2])
        
        if candidates_complete_list not in candidate_names:
            candidate_names.append(candidates_complete_list)

            votes_for_candidate[candidates_complete_list] = 1
        
        
        else:
            votes_for_candidate[candidates_complete_list] = votes_for_candidate[candidates_complete_list] + 1

        #finding the total votes for each canidate and then vote percentage
        for (row[2]) in votes_for_candidate:

            votes = votes_for_candidate.get(row[2])
            vote_percentage = float(votes) / float(total_votes) *100
            round_vote_percentage = round(vote_percentage,3)

            #fininding the winner
            if (votes  > winning_count):
                winning_count = votes
                winning_candidate = row[2]

    candidate_results = f"{row[2]}: {round_vote_percentage}% ({votes})\n"
    
    

    #Printing final results to the terminal
    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(total_votes))
    print("-----------------------")
    print(str(candidate_results))
    print("-----------------------")
    print("Winner: " + str(winning_candidate))
    print("-----------------------")

    #Creating a text file
    with open ("analysis/PyPoll_analysis.txt", "w") as f:
        f.write("Election Results" + "\n")
        f.write("-----------------------" + "\n")
        f.write("Total Votes: " + str(total_votes) + "\n")
        f.write("-----------------------" + "\n")
        f.write(str(candidate_results)+ "\n")
        f.write("-----------------------" + "\n")
        f.write("Winner: " + str(winning_candidate) + "\n")
        f.write("-----------------------")