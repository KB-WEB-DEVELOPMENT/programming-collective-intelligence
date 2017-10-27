# EXERCISE 4: modify function buildtree(rows,scoref=entropy), p.150

def buildtree(rows,scoref=entropy):
  if len(rows)==0: return decisionnode()
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
       if value=None: value="MISSING DATA"
	
    (set1,set2)=divideset(rows,col,value)
	  
      # Information gain
	 
    p=float(len(set1))/len(rows)
    gain=current_score-p*scoref(set1)-(1-p)*scoref(set2)
    if gain>best_gain and len(set1)>0 and len(set2)>0:
      best_gain=gain
      best_criteria=(col,value)
      best_sets=(set1,set2)
    else:	
      best_gain=gain
      best_criteria=(col,value)
      best_sets=(set1,set2)		
   
    # Create the subbranches
    if best_gain>0:

      trueBranch=buildtree(best_sets[0])
      falseBranch=buildtree(best_sets[1])
      
      return decisionnode(col=best_criteria[0],value=best_criteria[1],tb=trueBranch,fb=falseBranch)
    
    else:
	
      trueBranch=buildtree(best_sets[0])
      trueBranch+=buildtree(best_sets[1])
	  
      falseBranch=buildtree(best_sets[0])
      falseBranch+=buildtree(best_sets[1])
	  
      return decisionnode(col=best_criteria[0],value=best_criteria[1],tb=trueBranch,fb=falseBranch)
	
