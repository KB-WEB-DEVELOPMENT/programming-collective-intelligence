# EXERCISE 6: - rewrite function crosscount(v) - p.112/113

def crosscount(v):
  # Convert the number list into a dictionary of person:(x,y)
  loc=dict([(people[i],(v[i*2],v[i*2+1])) for i in range(0,len(people))])
  total=0
  smallanglecost=0
  # Loop through every pair of links
  for i in range(len(links)):
    for j in range(i+1,len(links)):
    # Get the locations
     (x1,y1),(x2,y2)=loc[links[i][0]],loc[links[i][1]]
     (x3,y3),(x4,y4)=loc[links[j][0]],loc[links[j][1]]
     den=(y4-y3)*(x2-x1)-(x4-x3)*(y2-y1)
     # den==0 if the lines are parallel
     if den==0: continue
     # Otherwise ua and ub are the fraction of the
     # line where they cross
     ua=((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3))/den
     ub=((x2-x1)*(y1-y3)-(y2-y1)*(x1-x3))/den
	 
	 # vectorA(xA,yA) goes through points P1(x1,y1) and P2(x2,y2)
	 # vectorB(xB,yB) goes through points P3(x3,y3) and P4(x4,y4)
	 # the angle through the 2 lines which extend vectorA and vectorB is very small if 
	 # abs(det(vectorA,vectorB)) <=0.1 (i.e:very small)  

	 xA=x2-x1
	 yA=y2-y1
	 xB=x4-x3
	 yB=y4-y3
	 
	 absdet=abs(xA*yB-xB*yA)
	 
	 if absdet <= 0.1: smallanglecost+=1   
	 
     # If the fraction is between 0 and 1 for both lines
     # then they cross each other
     if ua>0 and ua<1 and ub>0 and ub<1:
       total+=1
return total+smallanglecost
