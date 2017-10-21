# EXERCISE 7

def trainquery(self,wordids,urlids,selectedurl):
  # generate a hidden node if necessary
  self.generatehiddennode(wordids,urlids)
  self.setupnetwork(wordids,urlids)
  self.feedforward( )
  targets=[0.0]*len(urlids)
  targets[urlids.index(selectedurl)]=input("Please rate the result from 1 to 5: ")
  
  try:
    targets[urlids.index(selectedurl)]=int(targets[urlids.index(selectedurl)])  
  except InputTypeError:
    print("You must enter an integer.")
  else:
    while targets[urlids.index(selectedurl)] < 1 or targets[urlids.index(selectedurl)] > 5:
       print("You must rate the result between 1 and 5.")        
  
  error = self.backPropagate(targets)
  self.updatedatabase( )
