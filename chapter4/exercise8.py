# EXERCISE 8

from math import tanh
from pysqlite2 import dbapi2 as sqlite

class searchnet:
      def __init_ _(self,dbname,totalhiddenlayerscount):
        self.con=sqlite.connect(dbname)
		self.totalhiddenlayerscount=totalhiddenlayerscount

	  def __del_ _(self):
		self.con.close( )
      
	  def maketables(self):
	  	    		 
		self.con.execute('create table hiddennode(create_key)')
		self.con.execute('create table hiddenurl(fromid,toid,strength)')
		
		count = 1
		
		while count <=totalhiddenlayerscount:
		  sqlquery='create table wordhidden' + count + '(fromid,toid,strength)'
		  self.con.execute(sqlquery)
		  count +=1
		
		self.con.commit( )

         def getstrength(self,fromid,toid,layers,hiddenlayerstablename):
        
		for layer in layers:
		   #example: table="wordhidden55" or table="wordhidden1"
		  if layer==0: table=hiddenlayerstablename		  
                  else: table='hiddenurl'
                  res=self.con.execute('select strength from %s where fromid=%d and toid=%d' %
                      (table,fromid,toid)).fetchone( )
                  if res==None:
                    if layer==0: return -0.2
                    if layer==1: return 0
                  return res[0]

	  def setstrength(self,fromid,toid,layer,hiddenlayerstablename,strength):
               #example: table="wordhidden55" or table="wordhidden1"
		if layer==0: table=hiddenlayerstablename
                else: table='hiddenurl'
                res=self.con.execute('select rowid from %s where fromid=%d and toid=%d' %
                    (table,fromid,toid)).fetchone( )
                if res==None:
                   self.con.execute('insert into %s (fromid,toid,strength) values (%d,%d,%f)' %
                  (table,fromid,toid,strength))
                else:
                  rowid=res[0]
                  self.con.execute('update %s set strength=%f where rowid=%d' %
                     (table,strength,rowid))
