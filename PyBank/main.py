#importing and createing modeules to read csv file
import os
import csv

budget_data= os.path.join("Resources","budget_data.csv")


#opening the csv file
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #pulling the headers
    csv_header = next(csv_file)

    #creating variables
    total_months = 0
    total_profits_losses = 0
    

    for row in csv_reader:

        #finding the total months
        total_months = total_months + 1

        #finding the net total of profits and losses
        total_profits_losses = total_profits_losses + int(row[1])

        #Average change
       
    #printing the results to the terminal
    print("Financial Analysis")
    print("---------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_profits_losses))
    


        
        