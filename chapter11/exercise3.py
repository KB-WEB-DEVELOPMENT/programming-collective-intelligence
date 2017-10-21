# EXERCISE 3: It takes much longer for the evolve function to return 0 when it 
# uses the following crossover function. 

def crossover(t,probswap=0.7,top=1,pc,fpr=0.5,ppr=0.6,maxdepth=4):
  if random()<probswap and not top:
    return deepcopy(t)
  else:
    #flist param and choice function available in gp.py file
    f=choice(flist)
    result=deepcopy(t)
    
    childrenA=[makerandomtree(pc,maxdepth-1,fpr,ppr) for i in range(f.childcount)]
    childrenB=[makerandomtree(pc,maxdepth-1,fpr,ppr) for i in range(f.childcount)]
    
    nodeA=node(f,childrenA)
    nodeB=node(f,childrenB)
    
    if isinstance(t,nodeA) and isinstance(t,nodeB):
      result.children=[crossover(c,choice(t.childrenB),probswap,0) for c in t.childrenA]
      
  return result
