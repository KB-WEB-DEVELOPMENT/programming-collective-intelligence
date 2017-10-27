# EXERCISE 2: modify function modclassify(observation,tree) on p.157

def mdclassify(observation,tree):
  allowed_values=(20,25)
  if tree.results!=None:
     return tree.results
  else:
    v=observation[tree.col]
    if v==None:
       tr,fr=mdclassify(observation,tree.tb),mdclassify(observation,tree.fb)
       tcount=sum(tr.values( ))
       fcount=sum(fr.values( ))
       tw=float(tcount)/(tcount+fcount)
       fw=float(fcount)/(tcount+fcount)
       result={}
	 
       for k,v in tr.items( ): result[k]=v*tw
       for k,v in fr.items( ): result[k]=v*fw
    return result

    else:
      if int(v) in allowed_values:
	 if v>=tree.value: branch=tree.tb
         else: branch=tree.fb
      else:
        if v==tree.value: branch=tree.tb
        else: branch=tree.fb
      
    return mdclassify(observation,branch)
  
  return probcats  
