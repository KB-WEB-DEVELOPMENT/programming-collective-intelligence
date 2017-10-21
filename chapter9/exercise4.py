# EXERCISE 4: # rewrite function matchcount - p.206
# Hierarchy of interests setup:

# A SPORTS IN WATER 
#    A1  SPORTS WITH A BALL
#         A11 some sport
#         A12 some sport
#    A2 SPORTS WITHOUT A BALL
#         A21 some sport
#         A22 some sport
# B SPORTS ON GRASS
#    B1  SPORTS WITH A BALL
#         B11 some sport
#         B12 some sport
#    B2 SPORTS WITHOUT A BALL
#         B21 some sport
#         B22 some sport
#
# C SPORTS IN THE AIR
#   C1 some sport
#   C2 some sport
#   C3 some sport
#   C4 some sport

# note: if 2 interests match in categories A,B or C -> weight=0.3
# note: if 2 interests match in categories (A1 or A2),(B1 or B2) -> weight=0.5
# note: if 2 interests match in (end) nodes --> weight=1.0

def matchcount(interest1, interest2):
  sportsinair=['C1','C2','C3','C4']
  x=0.0
  l1=interest1.split(':')   
  l2=interest1.split(':')
  
  for v1 in l1:
    for v2 in l2:
      if v1=v2 and v1 in sportsinair:x+=1.0
      elif v1=v2:x+=1.0
      elif v1[:2]=v2[:2]:x+=0.5
      elif v1[:1]=v2[:1]:x+=0.3	  
  return x  
  
  
  
  
  
  
  
  
  
