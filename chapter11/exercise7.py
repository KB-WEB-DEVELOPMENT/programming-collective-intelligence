# EXERCISE 7: 
#
#           0 | 1 | 2
#           -   -   -
#           3 | 4 | 5
#           -   -   -
#           6 | 7 | 8

# returns 0 if player1 wins, returns 1 if player2 wins, returns 2 if there is a tie
# winning combinations: (0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)
# notice that summing winning numbers combinations, we can only get 3,9,12 or 15 
# tournament function similar to p. 271
def tictactoegame(p):

  maxmoves=9
  move=0

  #remember numbers already occupied
  numbersoccupied=[]
  winningcombinations=(3,9,12,15)
  player1numbers=[]
  player2numbers=[]
  
  while move<maxmoves:
  
    entry = randint(0,8)
	
	while entry in numbersoccupied: entry=randint(0,8)
	
	if move%2=1:
	   player1numbers.append(entry)  
	   numbersoccupied.append(entry)
	   if sum(player1numbers) in winningcombinations and len(player1numbers)%3==0: return 0	   
	   move+=1
      
	else:
	  player2numbers.append(entry)  
	  numbersoccupied.append(entry)
	  if sum(player2numbers) in winningcombinations	and len(player2numbers)%3==0: return 1	
	  move+=1
	  
  return 2 
  
def tournament(pl):

  losses=[0 for p in pl]

  for i in range(len(pl)):
    for j in range(len(pl)):
        if i==j: continue

       winner=tictactoegame([pl[i],pl[j]])

	   # Two points for a loss, one point for a tie
		if winner==0:
		   losses[j]+=2
		elif winner==1:
		   losses[i]+=2
		elif winner==2:
		   losses[i]+=1
		   losses[i]+=1
		pass

  z=zip(losses,pl)
  z.sort( )
  return z
	  
	   
