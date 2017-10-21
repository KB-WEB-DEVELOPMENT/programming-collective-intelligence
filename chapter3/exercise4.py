# EXERCISE 4

from math import abs
 
def manhattan_dist(v1,v2):
  # calculate pythagorian distance
  man_dist = return sum(abs(v1i-v2i) for v1i,v2i in zip(v1,v2))
  
  return man_dist 

# conclusion: since the distance is greater than pearson, more iteration are required to reduce the distance
# and create clusters. 
