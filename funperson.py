from person import Person 

def addPerson(lst):
    pid=int(input('Enter Id : '))
    name=input('Enter name : ')
    mob=input('Enter moblie : ')
    p=Person(pid,name,mob)
    lst.append(p)
    return True

def displayAllPerson(lst):
    for p in lst:
        print("\n")
        print(p)

    print("\n")   
        
def searchById(lst,pid):
    cnt=0
    for p in lst:
        if p.getPid()==pid:
            return cnt
        cnt+=1
    else:
        return -1

def searchByName(plist, pName):
         cnt=0
         for p in plist:
                  if p.getName==pName:
                          return cnt
                  cnt+=1
         else:
                  return -1

def removePerson(plist, pid):
         cnt=searchById(plist, pid)
         if cnt!=-1:
                  print("Person deleted successfully.", plist[cnt].getName())
                  plist.pop(cnt)
                  
                  return plist
         else:
                  print("Person Not Found")


def modifyName(plist, pid):
         nname=input("Enter the new name : ")
         cnt=searchById(plist, pid)
         if cnt!=-1:
                  plist[cnt].setName(nname)
                  print("updated successfully.",plist[cnt])
                  return plist

def modifyMobile(plist, pid):
         nmob=input("Enter the new mobile number : ")
         cnt=searchById(plist, pid)
         if cnt!=-1:
                  plist[cnt].setMob(nmob)
                  print("updated successfully.",plist[cnt])
                  return plist

def modifyAll(plist, pid):
         plist=modifyName(plist, pid)
         plist=modifyMobile(plist, pid)
         return plist

def displayId(plist, pName):
         cnt=searchByName(plist, pName)
         print(plist[cnt].getPid())
