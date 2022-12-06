with open("./input",'r') as file:
    lines = file.readlines()
for i in range(0,len(lines)):
    lines[i] = lines[i].split("\n")[0]
line = lines[0]

wortlange = 14
first = True
for i in range(0,len(line)-wortlange):
    partition = line[i:i+wortlange]
    cont = True
    for char in partition:
        if partition.count(char) > 1:
            cont = False
            break
    if cont and first:
        first = False
        print(f"last {i+len(partition)}")
