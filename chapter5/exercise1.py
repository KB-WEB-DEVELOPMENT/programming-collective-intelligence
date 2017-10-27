# EXERCISE 1: rewrite function schedulecost(sol) - p.90

def schedulecost(sol):
  totalprice=0
  latestarrival=0
  totalminutescost=0
  pre8AMcost=0
  earliestdep=24*60
  for d in range(len(sol)/2):
    # Get the inbound and outbound flights
    origin=people[d][1]
    outbound=flights[(origin,destination)][int(sol[d])]
    returnf=flights[(destination,origin)][int(sol[d+1])]
    # Total price is the price of all outbound and return flights
    totalprice+=outbound[2]
    totalprice+=returnf[2]
    
    outboundstartingminutes=time.strptime(outbound[0],'%M')
    outboundarrivalminutes=time.strptime(outbound[1],'%M')
    returnfstartingminutes=time.strptime(returnf[0],'%M')
    returnfarrivalminutes=time.strptime(returnf[1],'%M')
	
    totalminutescost += 0.5*((outboundarrivalminutes-outboundstartingminutes) + (returnfarrivalminutes-returnfstartingminutes))
		
    airportarrivaloutboundhours = time.strptime(outbound[0],'%H')
    airportarrivalreturnfhours = time.strptime(returnf[0],'%H')
	
    if int(airportarrivaloutboundhours)<8: pre8AMcost+=20	
    if int(airportarrivalreturnfhours)<8: pre8AMcost+=20
	
    # Track the latest arrival and earliest departure
    if latestarrival<getminutes(outbound[1]): latestarrival=getminutes(outbound[1])
    if earliestdep>getminutes(returnf[0]): earliestdep=getminutes(returnf[0])
    # Every person must wait at the airport until the latest person arrives.
    # They also must arrive at the same time and wait for their flights.
    totalwait=0
    for d in range(len(sol)/2):
      origin=people[d][1]
      outbound=flights[(origin,destination)][int(sol[d])]
      returnf=flights[(destination,origin)][int(sol[d+1])]
      totalwait+=latestarrival-getminutes(outbound[1])
      totalwait+=getminutes(returnf[0])-earliestdep

    # Does this solution require an extra day of car rental? That'll be $50!
    if latestarrival>earliestdep: totalprice+=50
    return totalprice+totalwait+totalminutescost+pre8AMcost
