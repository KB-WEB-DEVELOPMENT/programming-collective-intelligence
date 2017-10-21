# EXERCISE 4: - modify function flightsearch(sid,origin,destination,depart_date) in file kayak.py - p103
#             - modify function flightsearchresults(sid,searchid) in file kayak.py - p104

def flightsearch(sid,origin,destination,depart_date,return_date):
  # Construct search URL
  url='http://www.kayak.com/s/apisearch?basicmode=true&roundtrip=y&origin=%s' % (origin)
  url+='&destination=%s&depart_date=%s' % (destination,depart_date)
  url+='&return_date=%s&depart_time=a&return_time=a' % (return_date)
  url+='&travelers=1&cabin=e&action=doFlights&apimode=1'
  url+='&_sid_=%s&version=1' % (sid)
  # Get the XML
  doc=xml.dom.minidom.parseString(urllib2.urlopen(url).read( ))
  # Extract the search ID
  searchid=doc.getElementsByTagName('searchid')[0].firstChild.data
  return searchid
  
def flightsearchresults(sid,searchid):
  # Removes leading $, commas and converts number to a float
  def parseprice(p):
    return float(p[1:].replace(',',''))

  # Polling loop
  while 1:
    time.sleep(2)

  # Construct URL for polling
  url='http://www.kayak.com/s/basic/flight?'
  url+='searchid=%s&c=5&apimode=1&_sid_=%s&version=1' % (searchid,sid)
  doc=xml.dom.minidom.parseString(urllib2.urlopen(url).read( ))

  # Look for morepending tag, and wait until it is no longer true
  morepending=doc.getElementsByTagName('morepending')[0].firstChild
  if morepending==None or morepending.data=='false': break

  # Now download the complete list
  url='http://www.kayak.com/s/basic/flight?'
  url+='searchid=%s&c=999&apimode=1&_sid_=%s&version=1' % (searchid,sid)
  doc=xml.dom.minidom.parseString(urllib2.urlopen(url).read( ))

  # Get the various elements as lists
  outbound_prices=doc.getElementsByTagName('price')[0]
  outbound_departures=doc.getElementsByTagName('depart')[0]
  outbound_arrivals=doc.getElementsByTagName('arrive')[0]
  
  returnf_prices=doc.getElementsByTagName('price')[1]
  returnf_departures=doc.getElementsByTagName('depart')[1]
  returnf_arrivals=doc.getElementsByTagName('arrive')[1]
  
  # Zip them together
 return zip([p.firstChild.data.split(' ')[1] for p in outbound_prices],
            [p.firstChild.data.split(' ')[1] for p in outbound_departures],
            [parseprice(p.firstChild.data)   for p in outbound_prices],
		    [p.firstChild.data.split(' ')[1] for p in returnf_prices],
            [p.firstChild.data.split(' ')[1] for p in returnf_departures],
            [parseprice(p.firstChild.data)   for p in returnf_prices])
