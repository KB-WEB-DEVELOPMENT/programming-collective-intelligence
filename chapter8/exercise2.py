# EXERCISE 2: - the 3 functions below are needed, changes are made only to dividedata(data,test=0.05)
# consequence of change: it increases the returned value of function testalgorithm
# it increases the returned value of function crossvalidate
# the results are worse for the dataset function

def dividedata(data,test=0.05):
  trainset=[]
  testset=[]
  for row in data:
    testset.append(row)
    trainset.append(row)
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
