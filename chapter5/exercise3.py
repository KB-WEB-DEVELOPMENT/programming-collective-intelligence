# EXERCISE 3: - modify Main loop below - p98

def geneticoptimize(domain,costf,popsize=50,step=1,mutprod=0.2,elite=0.2,maxiter=100):

  # Mutation Operation
  def mutate(vec):
    i=random.randint(0,len(domain)-1)
    if random.random( )<0.5 and vec[i]>domain[i][0]:
      return vec[0:i]+[vec[i]-step]+vec[i+1:]
    elif vec[i]<domain[i][1]:
      return vec[0:i]+[vec[i]+step]+vec[i+1:]

   # Crossover Operation
   def crossover(r1,r2):
     i=random.randint(1,len(domain)-2)
     return r1[0:i]+r2[i:]

   # Build the initial population
   pop=[]
   for i in range(popsize):
     vec=[random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
     pop.append(vec)

   # How many winners from each generation?
   topelite=int(elite*popsize)

   # Main loop
   for i in range(maxiter):
   
       scores=[(costf(v),v) for v in pop]       
	   
       if i % 10 == 0 and scores[i][i] > scores[0][0]:	   
          break   
	   
       else:
	   scores.sort( )	   
	   ranked=[v for (s,v) in scores]

       # Start with the pure winners
       pop=ranked[0:topelite]

       # Add mutated and bred forms of the winners
       while len(pop)<popsize:
         if random.random( )<mutprob:
            # Mutation
            c=random.randint(0,topelite)
            pop.append(mutate(ranked[c]))
         else:
           # Crossover
           c1=random.randint(0,topelite)
           c2=random.randint(0,topelite)
           pop.append(crossover(ranked[c1],ranked[c2]))
	   
      # Print current best score
      print scores[0][0]
   return scores[0][1]
