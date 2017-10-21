# EXERCISE 6 - To make the  Grid War game MOSTLY random (as opposed 
# to completely random), I make a slight modification to the function 
# gridgame(p) on p.269
# "Mostly random" programs evolve faster (i.e: the evolve function returns 0
# with less iterations ). To improve, revert to the original function gridgame(p) which 
# is "more random".

def gridgame(p):

  max=(3,3)
  
  lastmove=[-1,-1]

  k=0
  
  while k<=max[0]:
  
     location=[[randint(0,max[k]),randint(0,max[k])]]
  
     location.append([(location[0][0]+2)%4,(location[0][1]+2)%4])

	 for o in range(50):

		 for i in range(2):
		   locs=location[i][:]+location[1-i][:]
		   locs.append(lastmove[i])
		   move=p[i].evaluate(locs)%4

		   if lastmove[i]==move: return 1-i
		   lastmove[i]=move
		   
		   if move==0:
			  location[i][0]-=1
			  if location[i][0]<0: location[i][0]=0
			
		   if move==1:
			  location[i][0]+=1
			  if location[i][0]>max[0]: location[i][0]=max[0]
		   
		   if move==2:
			  location[i][1]-=1
			  if location[i][1]<0: location[i][1]=0
			
		   if move==3:
			  location[i][1]+=1
			  if location[i][1]>max[1]: location[i][1]=max[1]
			  if location[i]==location[1-i]: return i
	   
	    return -1
		
	 k+=1	
