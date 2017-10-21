# EXERCISE 1: 
# modify function classify(observation,tree) on p.153,p.154
# modify function modclassify(observation,tree) on p.157

def classify(observation,tree):
  probcats={}
  total=0
  if tree.results!=None:
     for count in tree.results.values():
	   total+=count
	 for service,count in tree.results.items():
	    probcats[service]=float(count)/total	 
  else:
    v=observation[tree.col]
    branch=None
    if isinstance(v,int) or isinstance(v,float):
       if v>=tree.value: branch=tree.tb
       else: branch=tree.fb
    else:
       if v==tree.value: branch=tree.tb
       else: branch=tree.fb
    return classify(observation,branch)
	
  return probcats
  
def mdclassify(observation,tree):
  probcats={}
  total=0
  if tree.results!=None:
	 for count in tree.results.values():
	   total+=count
	 for service,count in tree.results.items():
	    probcats[service]=float(count)/total  
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
	  if isinstance(v,int) or isinstance(v,float):
		if v>=tree.value: branch=tree.tb
		else: branch=tree.fb
	else:
	  if v==tree.value: branch=tree.tb
      else: branch=tree.fb
    return mdclassify(observation,branch)
  
    return probcats  
