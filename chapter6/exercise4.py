# EXERCISE 4:

import re
import math

def extractNwords(doc, n):
  splitter=re.compile('\\*W')
  f={}
  
  words=[s.lower() for s in splitter.split(doc) if len(s)>2 and len(s)<20]
  
  if n<len(words)-1:
  
    nwords=' '.join(words[i:i+n])
    f[nwords]=1
  return f
