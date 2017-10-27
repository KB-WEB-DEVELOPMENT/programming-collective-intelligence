# EXERCISE 5 - in file searchengine.py

import urllib2
from BeautifulSoup import *

def percentFrenquencyscore(self,rows):
  counts= dict([row[0],0) for row in rows])
  for row in rows:
    counts[row[0]]+=1
	cur=self.con.execute("select urllist.url form urllist, wordlocation where urllid=%d and urllist.rowid=wordlocation.urlid"  % row[0])
	res=cur.fetchone()
	if res!=None:
	   try:
	     c=urllib2.urlopen(res)
	   except:
	     print "Could not open %s" %res		 
	   else:
             soup=BeautifulSoup(c.read())
	     # refer to function gettextonly(self,soup) on p.60
	     text=gettextonly(self,soup)
	     # refer to function separatewords(self,text) on p.61
	     wordslist=separatewords(self,text)
	     wordscount=len(wordslist)
	     percentscore=counts/wordscount
	     #refer to function normalizescores(self,scores,smallisBetter=0) on p.66 - use big is better here
	    return self.normalizescores(percentscore)
	   
       return false	
