with open("./input",'r') as file:
    lines = file.readlines()

myscore = 0


converter = { "A": 1, "B":2,"C":3,"X":1,"Y":2,"Z":3 }
win = {1:2,2:3,3:1}
loose = {2:1,3:2,1:3}
for line in lines:
    line = line.split("\n")[0]
    op,my = line.split(" ")
    op = converter[op]
    if(my == "X"):
        my = loose[op]
    elif(my=="Z"):
        my = win[op]
    elif(my =="Y"):
        my = op
    if(op == my):
        myscore += 3
    elif(op == 1 and my == 2 ):
        myscore += 6
    elif (op == 2 and my == 3):
        myscore +=6
    elif (op == 3 and my == 1):
        myscore += 6
    
    myscore +=my

print(myscore)




    
