with open("./input",'r') as file:
    lines = file.readlines()
for i in range(0,len(lines)):
    lines[i] = lines[i].split("\n")[0]

line = lines[0]

for i in range(0,len(line),4):

    if line[i] in line[i+1] + line[i+2] + line[i+3]:
        continue
    elif  line[1] in line[x+2] + line[x+3]:
        continue
    elif line[x+2] in line[x+3]:
        continue
    else:
        print(i)
        break