# EXERCISE 5: - Say we allow a node to split into 3 branches
# for a numerical value num -> 3 representations: x<num or x=num or x>num
# for a string value -> 3 representations: x=string_value or "only first character of x is the same as first character of string_value"  or x!=string_value

# rewrite class decisionnode - p.144
# rewrite function divideset(rows, column, value) - p.146
# rewrite function buildtree(rows, scoref=entropy) - p.150
# rewrite function classify(observation,tree) - p.153 [similar changes for function mdclassify(observation,tree) - p.157]

class decisionnode:
def __init__(self,col=-1,value=None,results=None,branch1=None,branch2=None,branch3=None):
  self.col=col
  self.value=value
  self.results=results
  self.branch1=branch1
  self.branch2=branch2
  self.branch3=branch3

def divideset(rows,column,value):
  split_function=None
  if isinstance(value,int) or isinstance(value,float):
   split_function1=lambda row:row[column]>value
   split_function2=lambda row:row[column]=value
   split_function3=lambda row:row[column]<value
  else:
   split_function4=lambda row:row[column]==value
   split_function5=lambda row:row[column][0]==value[0] and row:row[column][1:]!=value[1:]
   split_function6=lambda row:row[column]!=value
	
  set1=[row for row in rows if split_function1(row)]
  set2=[row for row in rows if split_function2(row)]
  set3=[row for row in rows if split_function3(row)]
  
  set1=[row for row in rows if split_function4(row)]
  set2=[row for row in rows if split_function5(row)]
  set3=[row for row in rows if split_function6(row)]
  
  return (set1,set2,set3)
  
def buildtree(rows,scoref=entropy):
  if len(rows)==0: return decisionnode( )
  current_score=scoref(rows)
  # Set up some variables to track the best criteria
  best_gain=0.0
  best_criteria=None
  best_sets=None
  
  column_count=len(rows[0])-1
  for col in range(0,column_count):
   # Generate the list of different values in
   # this column
     column_values={}
  for row in rows:
    column_values[row[col]]=1
   # Now try dividing the rows up for each value
   # in this column
  for value in column_values.keys( ):
    (set1,set2,set3)=divideset(rows,col,value)

   # Information gain
   p1=float(len(set1))/len(rows)
   p2=float(len(set2))/len(rows)
   p3=float(len(set3))/len(rows)
   gain=current_score-p1*scoref(set1)-p2*scoref(set2)-p3*scoref(set3)
   if gain>best_gain and len(set1)>0 and len(set2)>0 and len(set3)>0:
      best_gain=gain
      best_criteria=(col,value)
      best_sets=(set1,set2,set3)
   # Create the subbranches
   if best_gain>0:
      firstBranch=buildtree(best_sets[0])
      secondBranch=buildtree(best_sets[1])
      thirdBranch=buildtree(best_sets[2])
      return decisionnode(col=best_criteria[0],value=best_criteria[1],branch1=firstBranch,branch2=secondBranch,branch3=thirdBranch)
    
   else:
      return decisionnode(results=uniquecounts(rows))
