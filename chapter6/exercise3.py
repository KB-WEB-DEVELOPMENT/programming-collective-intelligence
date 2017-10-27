# EXERCISE 3: in file email.py, function getEmailMessages() below to download and return email messages from POP3 server 
# refer to the following blog and source code for classifying emails: 
# Blog: https://medium.com/towards-data-science/how-i-used-machine-learning-to-classify-emails-and-turn-them-into-insights-efed37c1e66
# github: https://github.com/anthdm/ml-email-clustering

import poplib
import getpass


def getEmailMessages:

  email=[]
  mServer = poplib.POP3('mail.test.org')

  #Login to mail server
  mServer.user(getpass.getuser())
  mServer.pass_(getpass.getpass())

  #Get the number of mail messages
  numMessages = len(mServer.list()[1])
 
  for mList in range(numMessages) :
    for msg in mServer.retr(mList+1)[1]:       
      email.append(msg)

  mServer.quit()
  return email  
  
