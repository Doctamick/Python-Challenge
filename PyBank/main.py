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



print("Financial Analysis")
print("------------------")

print(f"Total months:{total_months}")

