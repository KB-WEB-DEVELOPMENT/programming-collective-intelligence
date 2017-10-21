# EXERCISE 4

#weighting function to give preference to longer documents
def maxlengthdocscore(self,rows)
  maxdocsize=dict([(row[0],1000000) for row in rows])
  for row in rows:
    maxsize=max((row[i]) for i in range(2,len(row)))
	if maxsize>maxdocsize[row[0]]:maxdocsize[row[0]]=maxsize
  #choice:higher score means longer document,i.e: "bigger is better"
  return self.normalizescores(maxdocsize)
  
#weighting function to give preference to shorter documents
def minlengthdocscore(self,rows)
  mindocsize=dict([(row[0],1000000) for row in rows])
  for row in rows:
    minsize=min((row[i]) for i in range(2,len(row)))
	if minsize<mindocsize[row[0]]:mindocsize[row[0]]=minsize
  #choice:lower score means shorter document,i.e: "smaller is better"
  return self.normalizescores(mindocsize,smallisBetter=1) 
