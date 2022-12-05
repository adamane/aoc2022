with open("./input",'r') as file:
    lines = file.readlines()
for i in range(0,len(lines)):
    lines[i] = lines[i].split("\n")[0]
i = 0
numberofallingments = 0
for line in lines:
    elf1,elf2 = line.split(",")
    lower,upper = elf1.split("-")
    upper = int(upper)
    lower = int(lower)
    elf1 = set(range(lower, upper+1))
    lower, upper = elf2.split("-")
    upper = int(upper)
    lower = int(lower)
    elf2 = set(range(lower, upper+1))
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        numberofallingments += 1

print(numberofallingments)

numberofallingments = 0
for line in lines:
    elf1,elf2 = line.split(",")
    lower,upper = elf1.split("-")
    upper = int(upper)
    lower = int(lower)
    elf1 = set(range(lower, upper+1))
    lower, upper = elf2.split("-")
    upper = int(upper)
    lower = int(lower)
    elf2 = set(range(lower, upper+1))
    if elf1.intersection(elf2) or elf2.intersection(elf1):
        numberofallingments += 1

print(numberofallingments)
