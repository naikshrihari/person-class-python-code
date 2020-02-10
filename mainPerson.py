from person import Person 
import funperson as p
import sys


choice=0
plist=[]


while True:
    
    print('1.Add Person')
    print('2.Del Person')
    print('3.Modify Person')
    print('4.Display All')
    print('5.Display Id')
    print('6.Exit')
    
    choice=int(input('Enter Your choice :  '))
    
    if choice==1:
        ans=p.addPerson(plist)
        if ans == True:
            print('Added successfully')
            
    elif choice==2:
        pid=int(input("Enter the id to remove person : "))
        plist=p.removePerson(plist, pid)
        
    elif choice==3:
        print("a. Modify name of person : ")
        print("b. Modify mobile of person : ")
        print("c. Modify all :")
        choice=input("Enter your choice : ")
        pid=int(input("Enter the person id : "))
        if choice=="a":
            plist=p.modifyName(plist, pid)
        elif choice=="b":
            plist=p.modifyMobile(plist, pid)
        elif choice=="c":
            plist=p.modifyAll(plist, pid)
        else:
            print("Please Enter right choice Please!!!!!!!!!")
            
    elif choice==4:
        p.displayAllPerson(plist)
        
    elif choice==5:
        pName=input('Enter person name : ')
        p.displayId(plist, pName)
##        pos=p.searchById(plist,pid)
##        if pid!= -1:
##            print(plist[pos])
##            
##        else:
##            print('not found')
            
    elif choice==6:
        sys.exit(0)

    else:
        print("Enter the right choice!!!!!!!")
