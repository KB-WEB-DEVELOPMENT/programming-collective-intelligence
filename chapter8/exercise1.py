# EXERCISE 1: - solution: the function getidealneighborsnumbers, which makes use of the functions below it.

def getidealneighborsnumbers(data):
  scoremin=1000000
  kmin=0
  countmax=len(data)
  for k in range(countmax):
    def knn(d,v)=return.knnestimate(d,v,k)
	score=crossvalidate(knn,data)
	if score<scoremin:
	  scoremin=score
	  kmin=k
  return kmin  

def dividedata(data,test=0.05):
  trainset=[]
  testset=[]
  for row in data:
    if random( )<test:testset.append(row)
    else: trainset.append(row)
  return trainset,testset

def testalgorithm(algf,trainset,testset):
  error=0.0
  for row in testset:
    guess=algf(trainset,row['input'])
    error+=(row['result']-guess)**2
  return error/len(testset) 

def crossvalidate(algf,data,trials=100,test=0.05):
  error=0.0
  for i in range(trials):
    trainset,testset=dividedata(data,test)
    error+=testalgorithm(algf,trainset,testset)
  return error/trials

def knnestimate(data,vec1,k=3):
  # Get sorted distances
  dlist=getdistances(data,vec1)
  avg=0.0
  # Take the average of the top k results
  for i in range(k):
    idx=dlist[i][1]
    avg+=data[idx]['result']
    avg=avg/k
  return avg  
