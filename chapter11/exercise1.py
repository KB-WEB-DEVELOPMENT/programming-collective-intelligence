# EXERCISE 1: 
# question (a): function divw, function hasmorecharacters(l) question (b): class euclidistancenode

divw = fwrapper(lambda l:l[0]/l[1],2,'divide')

# function determines which of 2 strings has more characters
def hasmorecharacters(l):
  if len(l[0])>len(l[1]):return 1
  if len(l[0])<len(l[1]):return 2
  else: return 0
  
class euclidistancenode:
   def __init__(self,param1,param2,param3,param4):
      self.p1=param1
      self.p2=param2
      self.p3=param3
      self.p4=param4
    def calceuclidistance(self,dist):
      self.dist=(p1**2+p2**2+p3**2+p4**2)**0.5  
