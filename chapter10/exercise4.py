# EXERCISE 4: 

#modify function factorize, p.238

def factorize(v,pc=10):
  previouscost=10e9
  ic=shape(v)[0]
  fc=shape(v)[1]

  w=matrix([[random.random( ) for j in range(pc)] for i in range(ic)])
  h=matrix([[random.random( ) for i in range(fc)] for i in range(pc)])

  while cost <0.99*previouscost:
  
    previouscost=cost
    wh=w*h
    cost=difcost(v,wh)
  
    if i%10==0: print cost
    if cost==0: break

    hn=(transpose(w)*v)
    hd=(transpose(w)*w*h)
    h=matrix(array(h)*array(hn)/array(hd))

    wn=(v*transpose(h))
    wd=(w*h*transpose(h))
    w=matrix(array(w)*array(wn)/array(wd))

  return w,h
