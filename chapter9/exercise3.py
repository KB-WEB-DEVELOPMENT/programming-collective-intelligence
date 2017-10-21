# EXERCISE 3: we rewrite the function getoffset(rows,gamma) on p.213 to obtain optimal gamma

def getoffset(rows)
  bestgamma=1000000
  bestresult=0
  l0=[]
  l1=[]
  
  for row in rows:
    if row.match=0: l0.append(row.data)
    else: l1.append(row.data)
	
  for gamma in range(1,1000):
    sum0=sum(sum([rbf(v1,v2,gamma) for v1 in l0]) for v2 in l0)  
    sum1=sum(sum([rbf(v1,v2,gamma) for v1 in l1]) for v2 in l1)
	
   result=(1.0/(len(l1)**2))*sum1-(1.0/(len(l0)**2))*sum0
	
    if result>bestresult:
      bestgamma=gamma
      bestresult=result
	   
  return bestgamma, bestresult
