import os
import csv

file = os.path.join('..', 'Resources', 'budget_data.csv')

with open('budget_data.csv','r') as csvfile:
    
    budget_data = csv.reader(csvfile, delimiter = ',')
    readNextRow = next(budget_data)

    delta_profit = []
    changeInProfit = []
    NumberOfMonths = []

    for row in budget_data:
        
        NumberOfMonths.append(row[0])
        delta_profit.append(int(row[1]))

    for i in range(len(delta_profit)-1):
        changeInProfit.append(delta_profit[i+1] - delta_profit[i])
                      
        increase_profit = max(changeInProfit)
        decrease_profit = min(changeInProfit)

        month_increase = changeInProfit.index(max(changeInProfit)) + 1
        month_decrease = changeInProfit.index(min(changeInProfit)) + 1

    print("\n")
    print("Financial Analysis")
    print("-----------------------------------------")
    print(f"Total # of Months:  {len(NumberOfMonths)}")
    print(f"Total: ${sum(delta_profit)}")
    print(f"Average Change: {round(sum(changeInProfit)/len(changeInProfit),2)}")
    print(f"Greatest Increase in Profits: {NumberOfMonths[month_increase]} (${(str(increase_profit))})")
    print(f"Greatest Decrease in Profits: {NumberOfMonths[month_decrease]} (${(str(decrease_profit))})")      

output = os.path.join(".", 'output.txt')
with open(output,"w") as csvwriter:
    
    csvwriter.write("Financial Analysis")
    csvwriter.write("\n")
    csvwriter.write("-----------------------------------------")
    csvwriter.write("\n")
    csvwriter.write(f"Total # of Months:  {len(NumberOfMonths)}")
    csvwriter.write("\n")
    csvwriter.write(f"Total: ${sum(delta_profit)}")
    csvwriter.write("\n")
    csvwriter.write(f"Average Change: {round(sum(changeInProfit)/len(changeInProfit),2)}")
    csvwriter.write("\n")
    csvwriter.write(f"Greatest Increase in Profits: {NumberOfMonths[month_increase]} (${(str(increase_profit))})")
    csvwriter.write("\n")
    csvwriter.write(f"Greatest Decrease in Profits: {NumberOfMonths[month_decrease]} (${(str(decrease_profit))})")