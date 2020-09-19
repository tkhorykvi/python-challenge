import csv
import os

budget_csv = os.path.join('Resources', 'budget_data.csv')

months = []
revenue = []
date = []
profitloss = []
difflist = []
with open(budget_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    header = next(csvreader)
    print(csvreader)
    for row in csvreader:
        date.append(row[0])
        profitloss.append(int(row[1]))
# print(profitloss)
# print(months)
     
for x in range(1, len(profitloss)):
    diff = (profitloss[x]) - (profitloss[x-1])
    difflist.append(diff)
print(sum(difflist))

sumofdiff = sum(difflist)
lengthofdifflist = len(difflist)
averagechange = round(sumofdiff/lengthofdifflist, 2)
x = round(-2315.1176470588234, 2)
print(averagechange)
print(x)

maxincrease = max(difflist)
indexofmaxincrease = difflist.index(maxincrease)
maxincreasemonths = date[indexofmaxincrease + 1]
print(maxincreasemonths)

maxdecrease = min(difflist)
indexofmaxdecrease = difflist.index(maxdecrease)
maxdecreasemonths = date[indexofmaxdecrease + 1]
print(maxdecreasemonths)

months = len(date)
revenue = sum(profitloss)
print(months)
print(revenue)

name = "Financial Analysis"
print(name)
print("-----------------------")
print("Total Months: ", (months))
print("Total :", "$",(revenue))
print("Average Change :", "$",(averagechange))
print("Greatest Increase in Profits :", maxincreasemonths, "$",maxincrease)
print("Greatest Decrease in Profits :", maxdecreasemonths, "$",maxdecrease)

output_path = os.path.join("Resources", "analysis.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Total Months: ", (months)])
    csvwriter.writerow(["Total :", "$",(revenue)])
    csvwriter.writerow(["Average Change :", "$",(averagechange)])
    csvwriter.writerow(["Greatest Increase in Profits :", maxincreasemonths, "$",maxincrease])
    csvwriter.writerow(["Greatest Decrease in Profits :", maxdecreasemonths, "$",maxdecrease])
