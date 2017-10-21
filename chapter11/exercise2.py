# EXERCISE 2: It takes much longer for the evolve function to return 0 when it 
# uses the following mutate function.

def randomnodechange(pc,probchange=0.1,maxdepth=4,fpr=0.5,ppr=0.6):
  if random()<probchange:
    return makerandomtree(pc)
  else:
    f=choice(flist)
    children=[makerandomtree(pc,maxdepth-1,fpr,ppr) for i in range(f.childcount)]
    
  return node(f,children),paramnode(randint(0,pc-1)),constnode(randint(0,10)) 	 
