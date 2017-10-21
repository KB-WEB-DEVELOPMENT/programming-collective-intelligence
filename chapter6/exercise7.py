# EXERCISE 7: The design of the neural network is similar to fig4.4 (p74) but a bit different
# sketch of the neural network:
#
# feature_word1 (conn. to all feature categories) --> category_word1 (conn. to all feature words) --> hidden1 (connected to all cat query layers elements on LHS) -> document1 (connected to all hidden layers elements on LHS)  
#                        
# feature_word2 (conn. to all feature categories) --> category_word2 (conn. to all feature words) --> hidden2 (connected to all query layers elements on LHS) -> document2 (connected to all hidden layers elements on LHS)
#                       
# etc ...
#  
# etc ...

from math import tanh
from pysqlite2 import dbapi2 as sqlite

class searchnet:

  def __init__(self,dbname):
    self.con=sqlite.connect(dbname)

  def __del__(self):
    self.con.close( )

  def maketables(self):
    self.con.execute('create table hiddennode(create_key)')  
    self.con.execute('create table feature_to_cat(fromid,toid,strength)')
    self.con.execute('create table cat_to_hidden(fromid,toid,strength)')
    self.con.execute('create table document(fromid,toid,strength)')
    self.con.commit( )

  def getstrength(self,fromid,toid,layer):
    if layer==0: table='feature_to_cat'
    if layer==1: table='cat_to_hidden'
    if layer==2: table='hiddennode'
    if layer==3: table='document'
	
    res=self.con.execute('select strength from %s where fromid=%d and toid=%d' % (table,fromid,toid)).fetchone( )
    if res==None:
       if layer==1: return -0.2
       if layer==0: return 0
       if layer==2: return 0
       if layer==3: return 0	   
    return res[0]

   def setstrength(self,fromid,toid,layer,strength):
     if layer==0: table='feature_to_cat'
     if layer==1: table='cat_to_hidden'
     if layer==2: table='hiddennode'
     if layer==3: table='document'
	
       res=self.con.execute('select rowid from %s where fromid=%d and toid=%d' % (table,fromid,toid)).fetchone( )
	 if res==None:
           self.con.execute('insert into %s (fromid,toid,strength) values (%d,%d,%f)' % (table,fromid,toid,strength))
         else:
           rowid=res[0]
      self.con.execute('update %s set strength=%f where rowid=%d' % (table,strength,rowid))

  def generatehiddennode(self,wordids,docs):
    if len(wordids)>3: return None
    # Check if we already created a node for this set of words
    createkey='_'.join(sorted([str(wi) for wi in wordids]))
    res=self.con.execute("select rowid from hiddennode where create_key='%s'" % createkey).fetchone( )
    # If not, create it
    if res==None:
      cur=self.con.execute("insert into hiddennode (create_key) values ('%s')" % createkey)
      hiddenid=cur.lastrowid
    # Put in some default weights
    for wordid in wordids:
      self.setstrength(wordid,hiddenid,0,1.0/len(wordids))
    for docid in docs:
      self.setstrength(hiddenid,docid,1,0.1)
    self.con.commit( )

   def getallhiddenids(self,wordids,docids):
     l1={}
     for wordid in wordids:
       cur=self.con.execute('select toid from cat_to_hidden where fromid=%d' % wordid)
     for row in cur: l1[row[0]]=1
     for docid in docids:
       cur=self.con.execute('select fromid from document where toid=%d' % docid)
     for row in cur: l1[row[0]]=1
     return l1.keys( )

    def setupnetwork(self,wordids,docids):
    # value lists
      self.wordids=wordids
	  self.hiddenids=self.getallhiddenids(wordids,docids)
      self.docsids=docids
   # node outputs
	  self.ai = [1.0]*len(self.wordids)
	  self.ah = [1.0]*len(self.hiddenids)
      self.ao = [1.0]*len(self.docids)
    # create weights matrix
      self.wi = [[self.getstrength(wordid,hiddenid,0)for hiddenid in self.hiddenids] for wordid in self.wordids]
      self.wo = [[self.getstrength(hiddenid,docid,1) for docid in self.docids] for hiddenid in self.hiddenids]

    def feedforward(self):
      # the only inputs are the query words
      for i in range(len(self.wordids)):
        self.ai[i] = 1.0
      # hidden activations
      for j in range(len(self.hiddenids)):
        sum = 0.0
        for i in range(len(self.wordids)):
          sum = sum + self.ai[i] * self.wi[i][j]
        self.ah[j] = tanh(sum)
      # output activations
      for k in range(len(self.docids)):
        sum = 0.0
        for j in range(len(self.hiddenids)):
          sum = sum + self.ah[j] * self.wo[j][k]
        self.ao[k] = tanh(sum)
      
	  return self.ao[:]

    def getresult(self,wordids,docids):
      self.setupnetwork(wordids,docids)
      return self.feedforward( )

    def dtanh(y):
      return 1.0-y*y

    def backPropagate(self, targets, N=0.5):
      
	  # calculate errors for output
      output_deltas = [0.0] * len(self.docids)
      for k in range(len(self.docids)):
        error = targets[k]-self.ao[k]
        output_deltas[k] = dtanh(self.ao[k]) * error
      
	  # calculate errors for hidden layer
      hidden_deltas = [0.0] * len(self.hiddenids)
      for j in range(len(self.hiddenids)):
        error = 0.0
        for k in range(len(self.docids)):
          error = error + output_deltas[k]*self.wo[j][k]
        hidden_deltas[j] = dtanh(self.ah[j]) * error

    # update output weights
      for j in range(len(self.hiddenids)):
        for k in range(len(self.docids)):
            change = output_deltas[k]*self.ah[j]
            self.wo[j][k] = self.wo[j][k] + N*change
    
	# update input weights
      for i in range(len(self.wordids)):
          for j in range(len(self.hiddenids)):
          change = hidden_deltas[j]*self.ai[i]
          self.wi[i][j] = self.wi[i][j] + N*change

    def trainquery(self,wordids,docids,selecteddoc):
      # generate a hidden node if necessary
	  self.generatehiddennode(wordids,docids)
      
	  self.setupnetwork(wordids,docids)
      self.feedforward( )
      targets=[0.0]*len(docids)
      targets[docsids.index(selecteddoc)]=1.0
      error = self.backPropagate(targets)
      self.updatedatabase( )

    def updatedatabase(self):
    # set them to database values
    for i in range(len(self.wordids)):
       for j in range(len(self.hiddenids)):
         self.setstrength(self.wordids[i],self. hiddenids[j],0,self.wi[i][j])
    for j in range(len(self.hiddenids)):
       for k in range(len(self.docids)):
         self.setstrength(self.hiddenids[j],self.docids[k],1,self.wo[j][k])
    self.con.commit( )

 
