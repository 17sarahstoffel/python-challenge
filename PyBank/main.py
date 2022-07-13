#importing and createing modeules to read csv file
import os
import csv

from numpy import average

budget_data= os.path.join("Resources","budget_data.csv")


#opening the csv file
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #pulling the headers
    csv_header = next(csv_file)

    #creating variables and lists
    total_months = 0
    total_profits_losses = 0
    profits_losses = []
    list_of_changes =[]
    list_of_months = []
    
    for row in csv_reader:

        #finding the total months
        total_months = total_months + 1

        #finding the net total of profits and losses
        total_profits_losses = total_profits_losses + int(row[1])

        #update list to hold the values in the profit/losses column and list for months
        profits_losses.append(int(row[1]))

        list_of_months.append(row[0])

    #updating the change list
    for i in range(1,len(profits_losses)):
        change = profits_losses[i] - profits_losses[i-1]
        list_of_changes.append(change)
    
    #finding the average change
    average_change = average(list_of_changes) 
    round_average_change = round(average_change,2)

    #finding the greatest increase and in what month
    greatest_increase = max(list_of_changes)
    
    increase_index = list_of_changes.index(greatest_increase)
    greatest_increase_month= list_of_months[increase_index + 1]

    #finding the greatest decrease and in what month
    greatest_decrease = min(list_of_changes)
    
    decrease_index = list_of_changes.index(greatest_decrease)
    greatest_decrease_month = list_of_months[decrease_index + 1]
    

    #printing the results to the terminal
    print("Financial Analysis")
    print("---------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_profits_losses))
    print("Average Change: $" + str(round_average_change))
    print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")


with open ("analysis/PyBank_analysis.txt", "w") as f:
    f.write("Financial Analysis" + "\n")
    f.write("---------------------------" + "\n")
    f.write("Total Months: " + str(total_months) + "\n")
    f.write("Total: $" + str(total_profits_losses) + "\n")
    f.write("Average Change: $" + str(round_average_change) + "\n")
    f.write("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")" + "\n")
    f.write("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")" + "\n")
    f.close  

    
        