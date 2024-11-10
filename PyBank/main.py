import csv

#Read the budget data from the CSV file
with open(r"PyBank\Resources\budget_data.csv",'r')as file:

    csv_reader=csv.reader(file)
    # Read the header row first

    next(csv_reader)# Skip the header row

    months=[]
    profit_losses=[]
    changes=[]

    for row in csv_reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))


#Calculate the total number of months

total_months=len(months)

#calculate the net total amount of Profit/Losses
net_total=sum(profit_losses)

#calculate the changes in Profit/Losses and store them in list
for i in range(0,total_months):
    change=profit_losses[i]-profit_losses[i-1]
    changes.append(change)

#calculate the average change

average_change=sum(changes)/len(changes)

#find the greatest increase and decrease in profits
greatest_increase=max(changes)
greatest_decrease=min(changes)
greatest_decrease_date=months[changes.index(greatest_decrease)]

 
#print the analysis results 

print("Financial Analysis")
print("------------------")

print(f"Total months:{total_months}")
print(f"Total:${net_total}")
print(f"average change:${average_change:.2f}")
print(f"greatest increase in profits:{greatest_increase}(${greatest_increase})")
print(f"great decrease in profits:{greatest_decrease}(${greatest_decrease})")



