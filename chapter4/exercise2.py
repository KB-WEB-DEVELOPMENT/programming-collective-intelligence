# EXERCISE 2

# rewrite function getmatchrows(self,q) (p.63)
def getmatchrows(self,q):
  # Strings to build the query
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
     clauselist+='(w%d.wordid=%d or' % (tablenumber,wordid)
	   clauselist+='w%d.wordid=%d)' % (tablenumber-1,wordid+1)
     tablenumber+=1

	 # Create the query from the separate parts
     fullquery='select %s from %s where %s' % (fieldlist,tablelist,clauselist)
     cur=self.con.execute(fullquery)
     rows=[row for row in cur]

	 return rows,wordids
