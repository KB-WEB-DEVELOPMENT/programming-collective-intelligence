# EXERCISE 5: - add the following lines to the function entryfeatures(entry) - p 137

import re

#http://www.regular-expressions.info/ip.html
ip_pattern = re.compile('(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])')

ip_addresses=[s.lower( ) for s in splitter.split(entry['summary']) if len(s)>2 and len(s)<20]

for i in range(len(ip_addresses)):
   ip_address=re.findall(ip_pattern,ip_addresses[i])
   
   if ip_address == None: 
      pass
   else:
     f['IP ADDRESS']= ip_address
     f['IP']=1
	 
#http://www.regexlib.com/Search.aspx?k=phone&AspxAutoDetectCookieSupport=1
phoneNumber_pattern = re.compile('((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}')

phoneNumbers=[s.lower( ) for s in splitter.split(entry['summary']) if len(s)>2 and len(s)<20]

for i in range(len(phoneNumbers)):
   phoneNumber=re.findall(phoneNumber_pattern,phoneNumbers[i])	
   
   if phoneNumber == None: 
      pass
   else:
     f['PHONE NUMBER']= phoneNumber
     f['PHONE']=1
	
	
