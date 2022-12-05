import re
with open("./input",'r') as file:
    lines = file.readlines()
for i in range(0,len(lines)):
    lines[i] = lines[i].split("\n")[0]

stacks = []

[stacks.append([]) for x in range(9) ]
print()
linenr = 0
for line in lines:
    i = 0
    if not line.startswith(" 1"):
        for stack in stacks:
            charPos = i * 4 + 1
            i = i+1
            if line[charPos] == ' ':
                continue
            stack.append(line[charPos])
    else:
        break

for stack in stacks:
    stack.reverse()

print()

for line in lines:
    if not line.startswith("move"):
        continue
    iter,fro,to = re.findall(r'\d+',line)
    fro = int(fro) - 1
    to = int(to) - 1
    iter = int(iter)
    tmp = []
    for i in range(iter):
        tmp.insert(0,stacks[fro].pop())
    for i in tmp:
        stacks[to].append(i)
        
for stack in stacks:
    print(stack.pop())