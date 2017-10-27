# EXERCISE 2 - del.icio.us API dataset of tags and items

# get some tags dataset - can use import pydelicious library and call method get_tags(user, passwd) - Returns a list with all tags for user.
tags_dataset = [{ 'count': '2500', 'extended': '', 'hash': '', 'description': u'How To WriteUnmaintainable Code', 'tags': 'programming', 'href':
                   u'http://thc.segfault.net/root/phun/unmaintain.html', 'user': u'dorsia', 'dt': u'2006-08-19T09:48:56Z'
				},{'count': '3000','extended': '', 'hash': '', 'description': u'Threading in C#', 'tags': 'program', 'href':
					 u'http://www.albahari.com/threading/', 'user': u'mmihale', 'dt': u'2006-05-17T18:09:24Z'
				},{'count': '5500','extended': '', 'hash': '', 'description': u'Programming in Java', 'tags': 'computer science', 'href':
					u'http://www.kamibarut.de', 'user': u'barut', 'dt': u'2011-05-17T22:11:24Z'}]
tags = []

# save all tags contained in tags_dataset
for tags_dict in tags_dataset.items()
  tags.append(tags_dict['tags'])
  
# remove tags duplicates
unique_tags = list(set(tags))

# use Levenshtein distance ratio algorithm to check how similar two strings (here tags) are one to another
# https://people.cs.pitt.edu/~kirk/cs1501/Pruhs/Spring2006/assignments/editdistance/Levenshtein%20Distance.htm
# http://rosettacode.org/wiki/Levenshtein_distance#Python 
def levenshteinDistance(tag1, tag2):
    m = len(tag1)
    n = len(tag2)
    lensum = float(m + n)
    d = []           
    for i in range(m+1):
        d.append([i])        
    del d[0][0]    
    for j in range(n+1):
        d[0].append(j)       
    for j in range(1,n+1):
        for i in range(1,m+1):
            if tag1[i-1] == tag2[j-1]:
                d[i].insert(j,d[i-1][j-1])           
            else:
                minimum = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+2)         
                d[i].insert(j, minimum)
    ldist = d[-1][-1]
    ratio = (lensum - ldist)/lensum
    return {'ratio':ratio}

def topMatches(prefs,tag_chosen,n=3,similarity=levenshteinDistance):
    scores=[(similarity(prefs,tag_chosen,other),other) for other in unique_tags if other!=tag_chosen]
    return scores
	
#test 1 
# >> reload(exercise2)
# >> exercise2.topMatches(exercise2.tags_dataset, "some tag name I choose",n=3)

#test 2
# >> reload(exercise2)
# >> exercise2.topMatches(exercise2.tags_dataset, "programming",n=3)


