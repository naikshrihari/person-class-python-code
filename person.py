class Person:
    def __init__(self,pid=0,nm='',mob=''):
        
        self.pid=pid
        self.nm=nm
        self.mob=mob
        
    def __str__(self):
        return 'Pid: '+str(self.pid)+'\nName: '+self.nm+'\nMobile no.: '+self.mob
    
    def setPid(self,pid):
        self.pid=pid
        
    def setName(self,nm):
        self.nm=nm
        
    def setMob(self,mob):
        self.mob=mob

    def getPid(self):
        return self.pid
    
    def getName(self):
        return self.nm
    
    def getMob(self):
        return self.mob 

if __name__=='__main__':
    p=Person(12, 'shrihari', '12345')
    print(p)
    print(p.getName())
