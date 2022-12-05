#!/python

with open("./input",'r') as file:
    lines = file.readlines()

maxcals=0
elvecal = 0
rows = 0

elves = []
for line in lines:
    
    rows += 1
    if line == "\n":
        elves.append(elvecal)
        elvecal = 0
        print("newElve")
    else:
        line = int(line)
        
        elvecal = elvecal + line
        print(f"CurrentElve: {elvecal}")
    
    if elvecal > maxcals:
        maxcals = elvecal
    
print(rows)
print(f"{maxcals}")
elves.sort()
topthreeelves = elves[-1] + elves[-2] + elves[-3]
print(topthreeelves)