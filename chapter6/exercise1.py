# EXERCISE 1: 
# question 1: add variables and functions to class classifier contained in file docclass.py (p.119)
# question 2: modify function weightedprob() below   

class classifier(second_classifier):
  def __init__(self,getfeatures,getfeatures2,filename=None,filename2=None):

    self.fc={}
    self.fc2={}
    self.cc={}
    self.cc2={}
    self.getfeatures=getfeatures
    self.getfeatures=getfeatures2
	
  def incf(self,f,cat):
    self.fc.setdefault(f,{})
    self.fc[f].setdefault(cat,0)
    self.fc[f][cat]+=1

  def incf2(self,f2,cat2):
    self.fc2.setdefault(f2,{})
    self.fc2[f2].setdefault(cat2,0)
    self.fc2[f2][cat2]+=1		
		
  def incc(self,cat):
    self.cc.setdefault(cat,0)
     self.cc[cat]+=1
  
  def incc2(self,cat2):
    self.cc2.setdefault(cat2,0)
    self.cc2[cat2]+=1	

  def fcount(self,f,cat):
    if f in self.fc and cat in self.fc[f]:
       return float(self.fc[f][cat])
    return 0.0

  def fcount2(self,f2,cat2):
    if f2 in self.fc2 and cat2 in self.fc2[f2]:
       return float(self.fc2[f2][cat2])
    return 0.0	
		
  def catcount(self,cat):
    if cat in self.cc:
       return float(self.cc[cat])
    return 0

  def catcount2(self,cat2):
    if cat2 in self.cc2:
       return float(self.cc2[cat2])
    return 0	   

  def totalcount(self):
    return sum(self.cc.values( ))
	
  def totalcount2(self):
     return sum(self.cc2.values( ))

  def categories(self):
    return self.cc.keys( )
	
  def categories2(self):
    return self.cc2.keys( )

  def train(self,item,cat):
    features=self.getfeatures(item)

    for f in features:
      self.incf(f,cat)
      self.incc(cat)
	  
  def train2(self,item,cat2):
    features2=self.getfeatures2(item)
    
    for f2 in features2:
      self.incf2(f2,cat2)
      self.incc2(cat2)
 
   # question 2:  increase ap value for both functions from 0.5 to 0.8
   def weightedprob(self,f,cat,prf,weight=1.0,ap=0.8):
     basicprob=prf(f,cat)
     totals=sum([self.fcount(f,c) for c in self.categories( )])
     bp=((weight*ap)+(totals*basicprob))/(weight+totals)
     return bp
	 
   def weightedprob2(self,f2,cat2,prf2,weight2=1.0,ap2=0.8):
     basicprob2=prf2(f2,cat2)
     totals2=sum([self.fcount2(f2,c2) for c2 in self.categories2( )])
     bp2=((weight2*ap2)+(totals2*basicprob2))/(weight2+totals2)
     return bp2
