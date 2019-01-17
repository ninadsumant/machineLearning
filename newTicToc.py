import random
list=[1,2,3,4,5,6,7,8,9]

def tic():
    print (list[0],list[1],list[2])
    print (list[3],list[4],list[5])
    print (list[6],list[7],list[8])

def checkTic(pos):
    if(list[pos-1]=='X' or list[pos-1]=='O'):
        return False
    else:
        return True
def doTic(p1,pos):
    if(p1==1):
        list[pos-1]="X"
    else:
       list[pos-1]="O"   
    tic()
def isEnd():
    count=0;
    for x in range(0,9):
        if(list[x]=='X' or list[x]=='O'):
            count+=1
    if count==9:
        print("Tie\nGame End")
        return True
    
def isWin():
    
    for x in range(0,3):
        y=x*3
        if(list[y]==list[y+1] and list[y]==list[y+2]):
            print ("winner player is ",p1)
            return True
        if(list[x]==list[x+3] and list[x]==list[x+6]):
            print ("winner player is ",p1)
            return True
        if(list[0]==list[4] and list[4]==list[8] or list[2]==list[4] and list[4]==list[6]):
            print ("winner player is ",p1)
            return True
    
while True:
    pos=int(input("Enter player 1 choice:"))
    p1=1
    if checkTic(pos)==False:
        print("Invalid Choice..");
        continue
    doTic(1,pos)

    if isWin()==True:
        break
    if isEnd()==True:
        break
    
    while True:
        pos=int(random.randint(1,9))
        if checkTic(pos)==True:
            break
    print("Computer Choose : "+str(pos))
    p1=2
    doTic(2,pos)

    if isWin()==True:
        break
    if isEnd()==True:
        break
    
