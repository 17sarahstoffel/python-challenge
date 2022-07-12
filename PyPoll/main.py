#importing and createing modeules to read csv file
import os
import csv

election_data= os.path.join("Resources","election_data.csv")

#opening the csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #pulling the headers
    csv_header = next(csvfile)

    #creating variables
    total_votes = 0

    for row in csvreader:
        
        #finding total votes
        total_votes = total_votes + 1


    #Printing final results to the terminal
    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(total_votes))
    print("-----------------------")