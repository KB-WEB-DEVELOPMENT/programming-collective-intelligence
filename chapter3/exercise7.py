# EXERCISE 7 (p51,p52)

#scaling in 1-D

def draw1d(data,labels,jpeg='mds1d.jpg'):
  img=Image.new('RGB',(2000,2000),(255,255,255))
  draw=ImageDraw.Draw(img)
  for i in range(len(data)):
    x=(data[i][0]+0.5)*1000
    draw.text(x,labels[i],(0,0,0))
   
  img.save(jpeg,'JPEG')

#scaling in 3-D

def draw3d(data,labels,jpeg='mds3d.jpg'):
  img=Image.new('RGB',(2000,2000),(255,255,255))
  draw=ImageDraw.Draw(img)
  for i in range(len(data)):
    x=(data[i][0]+0.5)*1000
    y=(data[i][1]+0.5)*1000
	z=(data[i][1]+0.5)*1000
    draw.text((x,y,z),labels[i],(0,0,0))
   
  img.save(jpeg,'JPEG')
