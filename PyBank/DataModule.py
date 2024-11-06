def importcsv(budget_data):
 print("budget_data")
 file=open(budget_data.csv,"r")
 reader =reader.csv(budget_data.csv)

 next(reader)

 months= [0]
 for row in reader:
     months.append(row[0])


total_months=len("months")

print("Financial Analysis")
print("------------------------")

print(f"Total Months:{total_months}")


