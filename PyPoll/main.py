from enum import unique
from fileinput import lineno
import os
import csv
from tkinter import W
from turtle import end_fill
from urllib.parse import uses_relative
 
csvpath  = os.path.join('Resources','election_data.csv')
txtpath = os.path.join('Analysis', 'analysis.txt')
count = 0
candlist = []
votewon  = {}
winnervote = 0
#Reading data set file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
       
    for row in csvreader:
        #Total Votes count calculated
        count +=1

        #Finding and adding individual candidate to Dictionary
        if row[2] not in candlist :
            candlist.append(row[2])
            votewon[row[2]] = 0
        votewon[row[2]] = votewon[row[2]] + 1

#Opening a txt file to write the output
with open(txtpath, 'w') as txtfile:
   # txtfile.write(f"{count}\n")

    print("\nElection Results ")
    print("------------------------------------------------------\nTotal Votes : ",count)
    print("------------------------------------------------------")

    txtfile.write("Election Results \n")
    txtfile.write("------------------------------------------------------")
    txtfile.write("\n Total Votes : " f"{count}\n")
    txtfile.write("------------------------------------------------------\n")

    #Retrieveing individual candidate and its votes to print
    for candname in votewon :
        votepercand = votewon[candname]
        cpercent = (votepercand / count)*100
        print(f"{candname} : {round((cpercent),3)}% ({votepercand})")
        txtfile.write(f"{candname} : {round((cpercent),3)}% ({votepercand})\n")

        #Finding winner with maximum votes
        if votepercand > winnervote:
            winnervote = votepercand
            winnername = candname
    print("------------------------------------------------------\nWinner  : ",winnername)
    print("------------------------------------------------------")
    txtfile.write("\n------------------------------------------------------\n")
    txtfile.write("Winner  : " f"{winnername}\n")
    txtfile.write("------------------------------------------------------")
