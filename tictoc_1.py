import random
list=[1,2,3,4,5,6,7,8,9]
f=0
f1=0
def tic():
    print (list[0],list[1],list[2])
    print (list[3],list[4],list[5])
    print (list[6],list[7],list[8])

for i in range(0,9):
    tic()
    if(f1==1):
        i=i-1
    if(i%2!=0):
        li=int(input("Enter player 1 choice:"))
        p1=1
        f1=0
    else:
        li=int(random.randint(0,8)) #int(input("Enter player 2 choice:"))
        print("Computer choose : "+str(li))
        p1=2
        f1=0

    if(list[li-1]=='X' or list[li-1]=='O'):
        print ("Invalid choice!!!!")
        f1=1
        i=i-1
        continue
    if(i%2!=0):
        list[li-1]="X"
    else:
       list[li-1]="O"
    for x in range(0,3):
        y=x*3
        if(list[y]==list[y+1] and list[y]==list[y+2]):
            print ("winner player is ",p1)
            f=1
            break
        if(list[x]==list[x+3] and list[x]==list[x+6]):
            print ("winner player is ",p1)
            f=1
            break
        if(list[0]==list[4] and list[4]==list[8] or list[2]==list[4] and list[4]==list[6]):
            print ("winner player is ",p1)
            f=1
            break
    if(f==1):
        tic()
        break
    
