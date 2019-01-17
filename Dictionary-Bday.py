# dict with 10 name and bDate
# add ,show, count 
# add on select opt add
# show bday of person name on show
# count by month on count
dis={'abc':'02/01/1998',
     'aqa':'12/11/1987',
     'aqt':'22/11/1984',
     'era':'32/12/1987',
     'dis':'02/11/1982',
     'ha':'04/10/1982',
     'ja':'06/10/1988',
     'nvi':'04/9/1989',
     'ars':'04/8/1985',
     'hit':'01/8/1985'}

def getByMonth():
    val=dis.values();
    mn=input("Select Month (1-12): ")
    count=0
    for a in val:
        ans=a.split('/');
        if ans[1]==mn:
            count=count+1;
    print("In month "+mn+" : "+str(count))
ch=0
while ch!=5:
    print("1. Add new Data")
    print("2. Check Birthdate")
    print("3. Count Birthdate by month")
    print("4. Show Dictionary")
    print("5. Exit")
    ch=int(input("Select one : "))
    if ch == 1:
        name=input("Enter name : ")
        bd=input("Enter birthdate (dd/mm/yyyy) : ")
        dis[name]=bd;
        print("Added successfully")
    elif  ch == 2:
        name=input("Enter name : ")
        print("Birthday of "+name+" : "+dis[name])
    elif ch == 3:
        getByMonth()
    elif ch == 4:
        print();
        print(dis);
        print();
    elif ch == 5:
        print("Bby");
    else :
        print("Invalid Choice..");
         
