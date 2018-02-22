import csv
import os

firstLine = True
totalMonths = 0
totalRevenue = 0
prevMonthRevenue = 0
diffRevenue = 0
diffRevenueList = []
#averageRev = 0
sumDiffRevenue = 0

budgetFile = os.path.join("budget_data_1.csv") # Input File
textFile = os.path.join("pyBankOutput.txt") #Output file

with open(budgetFile, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter = ",")

    for row in csvReader:

        #skip first line
        if(firstLine):
            firstLine = False
            continue
        totalMonths = totalMonths + 1

        diffRevenue = int(row[1]) - prevMonthRevenue
        sumDiffRevenue = sumDiffRevenue + diffRevenue
        prevMonthRevenue = int(row[1])
        diffRevenueList.append(diffRevenue)
        totalRevenue = totalRevenue + int(row[1])

    print("-------------------------------")
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Revenue: " + str(totalRevenue))
    print("Greatest Increase:"+ str(max(diffRevenueList)))
    print("Greatest Decrease:" + str(min(diffRevenueList)))
    averageRev = (sum(diffRevenueList))/len(diffRevenueList)
    print("Average revenue: " + str(averageRev))
    totalMonths = totalMonths
    print("Total months: " + str(totalMonths))

    txtFile = open(textFile, 'w')
    txtFile.write("-------------------------------"+"\n"
                  +"Financial Analysis"+ "\n"
                  +"-------------------------------"+"\n"
                  +"Total months: " + str(totalMonths) + "\n"
                  + "Total Revenue: " + str(totalRevenue) + '\n'
                  + "Greatest Increase:"+ str(max(diffRevenueList)) +"\n"
                  + "Greatest Decrease:" + str(min(diffRevenueList)) + "\n"
                  + "Average revenue: " + str(averageRev) + "\n" )
    txtFile.close()
