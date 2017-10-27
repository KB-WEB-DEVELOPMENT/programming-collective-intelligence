# EXERCISE 4: 

def evolve(pc,popsize,rankfunction,maxgen=500,mutationrate=0.1,breedingrate=0.4,pexp=0.7,pnew=0.05,noimprovementitervar=20):

def selectindex():
    
   j=0
   maxscore=10e10
	
   return int(log(random())/log(pexp))
   population=[makerandomtree(pc) for i in range(popsize)]

   for i in range(maxgen):	
     while j<=noimprovementitervar:	  
      scores=rankfunction(population)	  
        
      if scores[0][0]<maxscore:
        print scores[0][0]
        if scores[0][0]==0: break
        maxscore=scores[0][0]
      else:
       j+=1
	  
      newpop=[scores[0][1],scores[1][1]]

    while len(newpop)<popsize:
      if random()>pnew:
	 newpop.append(mutate(
	    crossover(scores[selectindex()][1],
	    scores[selectindex( )][1],
	    probswap=breedingrate),
           pc,probchange=mutationrate))
      else:
        newpop.append(makerandomtree(pc))
      
    population=newpop
    
  scores[0][1].display()
  return scores[0][1]
