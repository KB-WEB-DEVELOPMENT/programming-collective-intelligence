# EXERCISE 3: The idea is to modify the function wineset2(), p.178
# so that only relevant variables are entered by the user. 
# Only "realistic" variables are kept, i.e: between 0 and 100. With regard
# to the usefulness of a variable, there is no way for the computer to determine
# if a variable is more relevant than another one.

def eliminatingvar(var):
  if var<=0 or var>100:
     return 1
  else: return var	 
