import string
with open("./input",'r') as file:
    lines = file.readlines()
    
Index = [0] + list(string.ascii_lowercase) + list(string.ascii_uppercase)
prio = 0
for line in lines:
    line = line.split("\n")[0]
    sep = int(len(line)/2)
    comp1 = line[:sep]
    comp2 = line[sep:]
    for element in comp1:
        if element in comp2:
            prio += Index.index(element)
            break
print(prio)
prio = 0
for i in range(0,len(lines)):
    lines[i] = lines[i].split("\n")[0]
    
for i in range(0,len(lines),3):
    """
    line = lines[i]
    for element in line:
        if element in lines[i+1]:
            if element in lines[i+2]:
                prio += Index.index(element)
                """
    result = set(lines[i]) & set(lines[i+1]) & set(lines[i+2])
    prio += Index.index(result.pop())
print(prio)
