# EXERCISE 7: The old eBay API is deprecated, refer to the following links
# http://developer.ebay.com/devzone/finding/concepts/findingapiguide.html#usekeywords 
# http://developer.ebay.com/devzone/finding/CallRef/findCompletedItems.html#Samples

# note: all other methods stay the same (p.190): getHeaders(),sendRequest(), detSingleValue()

def doSearch(categoryID=None,page=1):
  xml = "<?xml version="1.0" encoding="utf-8"?>" +\
        "<findCompletedItemsRequest xmlns='http://www.ebay.com/marketplace/search/v1/services'>" +\
           "<keywords>" + "Core Duo laptops" + "</keywords>" +\   
              "<entriesPerPage>" + int(200) + "</entriesPerPage>" +\
              "<pageNumber>" + int(1) + "</pageNumber>" +\
         "</findCompletedItemsRequest>"
		 
  data=sendRequest('findCompletedItems',xml)
  response = parseString(data)
  itemNodes = response.getElementsByTagName('Item');
  results = []
  for item in itemNodes:
    itemId=getSingleValue(item,'ItemID')
    itemTitle=getSingleValue(item,'Title')
    itemPrice=getSingleValue(item,'CurrentPrice')
    itemEnds=getSingleValue(item,'EndTime')
    results.append((itemId,itemTitle,itemPrice,itemEnds))
 return results
