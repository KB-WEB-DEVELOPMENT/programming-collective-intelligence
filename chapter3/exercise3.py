# EXERCISE 3

from math import sqrt
def pythagorian_dist(v1,v2):
  # calculate pythagorian distance
  pyth_dist = math.sqrt(sum([v1i - v2i])**2 for v1i,v2i in zip(v1,v2)) 

  return pyth_dist

# conclusion : since pyth_dist may be large >> 1, blogs become highly uncorrelated and move away from one another.
