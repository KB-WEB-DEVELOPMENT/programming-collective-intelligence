# EXERCISE 3 

from pydelicious import get_userposts


# Returns a bookmarked ordered count of user_dict for person 1 (=p1) including url and tag
def getUserposts(p1):
  user_dict={}
  try:
    posts=get_userposts(p1)
  except:
    print "Failed user "+p1+", retrying"
    time.sleep(4)
  for post in posts:
    tag=post['tag']  
    url=post['url']
    count=post['count']
    user_dict[p1][tag]=tag
    user_dict[p1][tag][url]=url
    user_dict[p1][tag][url][count]=count
  
  
  user_dict[p1][tag][url][count].sort()
  user_dict[p1][tag][url][count].reverse()
  
  return user_dict

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
  # Get the list of mutually rated items
  si={}
  for item in prefs[p1]:
    if item in prefs[p2]: si[item]=1
    
  # Find the number of elements
  n=len(si)
  
  # if they are no ratings in common, return 0
  if n==0: return 0

  # Add up all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])

  # Sum up the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

  # Sum up the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

  # Calculate Pearson score
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0
   
  r=num/den
   
  return r
  
#Returns the first 5 best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]

  # Sort the list so the highest scores appear at the top
  scores.sort( )
  scores.reverse( )
  return scores[0:4]
  
# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
  totals={}
  simSums={}
  for other in prefs:
    # don't compare me to myself
    if other==person: continue
    sim=similarity(prefs,person,other)

	# ignore scores of zero or lower
    if sim<=0: continue
    for item in prefs[other]:

	  # only score movies I haven't seen yet
      if item not in prefs[person] or prefs[person][item]==0:
      # Similarity * Score
      totals.setdefault(item,0)
      totals[item]+=prefs[other][item]*sim
      # Sum of similarities
      simSums.setdefault(item,0)
      simSums[item]+=sim

  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items( )]
  
  # Return the sorted list
  rankings.sort( )
  rankings.reverse( )
  return rankings


