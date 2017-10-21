# EXERCISE 1

# all functions identical to the ones in the book (p29-53)

# key point: the dataset/file underneath has to match the variables returned by the function readfile(filename) below 
# for clustering to take place.

def readfile(filename):
  lines=[line for line in file(filename)]

 # First line is the column titles
 colnames=lines[0].strip( ).split('\t')[1:]
 rownames=[]
 data=[]
 for line in lines[1:]:
  p=line.strip( ).split('\t')
  # First column in each row is the rowname
  rownames.append(p[0])
  # The data for this row is the remainder of the row
  data.append([float(x) for x in p[1:]]) 
  return rownames,colnames,data 
  
# dataset/file structure: bookmarks.txt

#(line0)travels computing restaurants cars ...
#(line1)https://www.opentable.com [del.icio.us description item of this bookmark}
#(line2)https://www.skyparksecure.com/ [del.icio.us description item of this bookmark]
#(line3)https://www.viator.com [del.icio.us description item of this bookmark]
#......
#.....
#.....



