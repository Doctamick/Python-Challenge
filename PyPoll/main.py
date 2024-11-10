import csv

with open(r"Pypoll\Resources\election_data.csv.csv","r") as file:
    reader=csv.reader(file)
    next(reader)

    total_vote=0
    candidates={}

    for row in reader:
        candidate=row[2]
        total_vote +=1
        candidates[candidate]=candidates.get(candidate,0)+1

results=[]
for candidate,votes in candidates.items():
    percentage=(votes/total_vote)*100
    results.append((candidate,percentage,votes))

#find the winner based on popular vote
winner=max(results,key=lambda x:x[2])

#print the analysys results
print("Election Results")
print("------------------------")
print(f"Total Votes:{total_vote}")
print("-------------------------")
for candidate,percentage,votes in results:
    print(f"{candidate}:{percentage:.3f}%({votes})")



print("-----------------------------")
print(f"winner:{winner[0]}")

      

