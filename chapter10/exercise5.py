# EXERCISE 5:  

# question 1: Rewrite function showarticles (p.242),renamed showhighlightedfeatures below
# question 2: modify code at the end of the file stockvolume.py (p.246) below

# question 1:
def showhighlightedfeatures(titles,toppatterns,patternnames,out='articles.html'):
  outfile=file(out,'w')
  for j in range(len(titles)):
    titlewordsarray = list(titles[j].encode('utf8'))
    toppatterns[j].sort()
    toppatterns[j].reverse()
    
    outfile.write('<html><head>Results</head><body>')	
    
    for k in range(len(titlewordsarray)):
    
      for i in range(3):
        if titlewordsarray[k]==str(toppatterns[j][i][0]) or titlewordsarray[k]==str(patternnames[toppatterns[j][i][1]]):
          output.write('<span style="color:yellow"' + titlewordsarray[k] + '</span>')
        else:
          output.write(titlewordsarray[k])
        outfile.write('\n')	
        
        outfile.write(str(toppatterns[j][i][0]) + ' ' +str(patternnames[toppatterns[j][i][1]])+ '\n')
        
        outfile.write('\n')
        
    outfile.write('</body><html>')
    
    outfile.close( )
	
# question 2:
for i in range(shape(h)[0]):
  print "Feature %d" %i

ol=[(h[i,j],tickers[j]) for j in range(shape(h)[1])]
ol.sort( )
ol.reverse( )

for j in range(12):
  print ol[j]
print

porder=[(w[d,i],d) for d in range(300)]
porder.sort( )
porder.reverse( )

print [(p[0],formatdates(dates[p[1]]) for p in porder[0:3]]
print

def formatdates(dates):
  day=dates[p[1]][0] + dates[p[1]][1]
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Jan": month="January"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Feb": month="February"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Mar": month="March"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Apr": month="April"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "May": month="May"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Jun": month="June"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Jul": month="July"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Aug": month="August"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Sep": month="September"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Oct": month="October"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Nov": month="November"
  if dates[p[1]][3] + dates[p[1]][4] + dates[p[1]][5] == "Dec": month="December"  
 
  fullyear= "20" + dates[p[1]][7] + dates[p[1]][8]
  fulldate = day + month  + fullyear
  return fulldate
  

