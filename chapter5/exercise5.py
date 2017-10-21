# EXERCISE 5: create file student.py
# create two functions: printsolution(vec) and studentcost(vec) - p 108,109

import random
import math

students=['Toby','Steve','Andrea','Sarah','Dave','Jeff', 'Fred', 'Suzie', 'Laura', 'Neil']

prefs=[('Toby', ('Steve', 'Andrea')),
('Steve', ('Sarah', 'Dave')),
('Andrea', ('Dave', 'Zeus')),
('Sarah', ('Jeff', 'Laura')),
('Dave', ('Andrea', 'Jeff')),
('Jeff', ('Andrea', 'Dave')),
('Fred', ('Neil', 'Andrea')),
('Suzie', ('Bacchus', 'Sarah')),
('Laura', ('Fred', 'Sarah')),
('Neil', ('Hercules', 'Andrea'))]

# [(0,9),(0,8),(0,7),(0,6),...,(0,0)]
domain=[(0,(len(students)*2)-i-1) for i in range(0,len(students)*2)]

def printsolution(vec):
  slots=[]

  for i in range(len(tudents): slots+=[i,i]
  
  for i in range(len(vec)):
    
	x=int(vec[i])
    student=students[slots[x]]
    print prefs[i][0],student
    del slots[x]

def studentcost(vec):
  cost=0
  slots=[0,0,1,1,2,2,3,3,4,4]

  for i in range(len(vec)):
    x=int(vec[i])
    student=students[slots[x]]
    pref=prefs[i][1]

    if pref[0]==student: cost+=0
    elif pref[1]==student: cost+=1
    else: cost+=3

del slots[x]
  return cost

 
