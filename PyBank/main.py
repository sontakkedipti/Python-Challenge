import os
import csv
from tkinter import W
 
csvpath  = os.path.join('Resources','budget_data.csv')
txtpath = os.path.join('Analysis', 'analysis.txt')
count = 0
total = 0
prevvalue = 0
profloss_list = []
minmaxdate_list = []

#Reading data set file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skipping header row
    next(csvreader)

    #Reading each row for calculation
    for row in csvreader:
        count = count + 1
        total = int(row[1])+total
        if(row[0] == "Jan-10") :
            profloss_list.append(0)
        else :

            profloss_list.append(int(row[1])- prevvalue)

        prevvalue = int(row[1])
        minmaxdate_list.append(row[0])

with open(txtpath, 'w') as txtfile:
    
    # Printing to Terminal

    print("\nFinantial Analysis")
    print("--------------------------------------")   
    print("Total Months : " ,str(count))
    print("Total : " ,"$",total)
    
    print("Average Change ", f"${sum(profloss_list)/(len(profloss_list)-1):.2f}")
    tempmax= max(profloss_list)
    tempmin = min(profloss_list)
    maxindex = profloss_list.index(tempmax)
    minindex = profloss_list.index(tempmin)
    print("Greatest Increase in Profits: ",f"{minmaxdate_list[maxindex]}  (${max(profloss_list)}) ")
    print("Greatest Decrease in Profits: ",f"{minmaxdate_list[minindex]}  (${min(profloss_list)})  ")
    print("-----------------------------------")

    #Exporting to CSV File
    txtfile.write("\nFinantial Analysis \n")
    txtfile.write("-----------------------------------")
    txtfile.write("\nTotal Months : " f"{count}\n")
    txtfile.write("Total : $" f"{total}\n")
    txtfile.write("Average Change " f"${sum(profloss_list)/(len(profloss_list)-1):.2f}\n")
    txtfile.write("Greatest Increase in Profits: "f"{minmaxdate_list[maxindex]}  (${max(profloss_list)}) \n")
    txtfile.write("Greatest Decrease in Profits: "f"{minmaxdate_list[minindex]}  (${min(profloss_list)})  \n")
    txtfile.write("-----------------------------------")