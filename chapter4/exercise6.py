# EXERCISE 6 

def bothinboundandsearchtermsscore(self,q):
  # modify function getmatchrows(self,q) (p.63)
  fieldlist='w0.urlid'
  tablelist=''
  clauselist=''
  wordids=[]
  
  # Split the words by spaces
  words=q.split(' ')
  tablenumber=0

  for word in words:
    # Get the word ID
    wordrow=self.con.execute(
    "select rowid from wordlist where word='%s'" % word).fetchone( )
    if wordrow!=None:
      wordid=wordrow[0]
      wordids.append(wordid)

  if tablenumber>0:
    tablelist+=','
    clauselist+=' and '
    clauselist+='w%d.urlid=w%d.urlid and ' % (tablenumber-1,tablenumber)
    fieldlist+=',w%d.location' % tablenumber
    tablelist+='wordlocation w%d' % tablenumber
    clauselist+='w%d.wordid=%d' % (tablenumber,wordid)
    tablenumber+=1

    # Create the query from the separate parts
    fullquery='select %s from %s where %s' % (fieldlist,tablelist,clauselist)
    cur=self.con.execute(fullquery)
    rows=[row for row in cur]
    rowscount=len(rows)
	
  #refer to function inboundlinkscore(self,rows) on p.69
  uniqueurls=set([row[0] for row in rows])
  inboundcount=dict([(u,self.con.execute( \
    'select count(*) from link where toid=%d' % u).fetchone( )[0]) \
      for u in uniqueurls])

  totalcount=rowscount+inboundcount
  #refer to function normalizescores(self,scores,smallisBetter=0) on p.66 - use big is better here
  return self.normalizescores(totalcount)
  
   
