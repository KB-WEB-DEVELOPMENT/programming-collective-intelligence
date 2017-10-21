# EXERCISE 1 - Returns Tanimoto coefficient T - applicable only for binary variables a, b  
# - each of dimension at least k greater than 0

def sim_tanomoto(prefs,a,b):
  # Get all k similar items in a and b
  si={}
  for item in prefs[a]:
 	if item in prefs[b]: si[item]=1  

  # Find dimension k - only needed to check if k is 0
  k=len(si)
  
  #if a and b have no items in common, return 0
  if k==0: return 0
  
  #Calculate product sum of "ratings" of all k common items in a and b
  sum_product = sum([prefs[a][it]*prefs[b][it] for it in si])
  
  #Calculate squared sum of "ratings" of all k common items in a and b
  sum_all_a_squared = sum([pow(prefs[a][it],2) for it in si])
  sum_all_b_squared = sum([pow(prefs[b][it],2) for it in si])
  
  #calculate Tanimoto coefficient T
  t=sum_product/(sum_all_a_squared+sum_all_b_squared-sum_product)
  
  return t
