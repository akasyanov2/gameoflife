#!/usr/local/bin/python3

from sys import argv
import copy
import random
#from numpy import ndenumerate
import os
from time import sleep
#import figures

alivecells=0

x=45
y=45
timeout=.035
target = open('lastrun', 'w')

chars='x        '

currentstate= [ [ random.choice(chars) for i in range(y) ] for j in range(x) ]
target.write('[\n');
for item in currentstate:
  target.write("%s,\n" % item)
target.write(']\n');


#currentstate=figures.longlasting

nextstate=copy.deepcopy(currentstate)

def getneighbors(currentstate,row,col,val):
  neighbors=0
  if(row-1>=0 and currentstate[row-1][col]=='x'): 
    neighbors=neighbors+1
  #print ("1=",neighbors);
  if(row+1<x and currentstate[row+1][col]=='x'): 
    neighbors=neighbors+1
  #print ("2=",neighbors);
  if(col+1<y and currentstate[row][col+1]=='x'): 
    neighbors=neighbors+1
  #print ("3=",neighbors);
  if(col-1>=0 and currentstate[row][col-1]=='x'): 
    neighbors=neighbors+1
  #print ("4=",neighbors);
  if(col+1<y and row+1<x and currentstate[row+1][col+1]=='x'): 
    neighbors=neighbors+1
  #print ("5=",neighbors);
  if(col-1>=0 and row-1>=0 and currentstate[row-1][col-1]=='x'): 
    neighbors=neighbors+1
  #print ("6=",neighbors);
  if(col-1>=0 and row+1<x and currentstate[row+1][col-1]=='x'): 
    neighbors=neighbors+1
  #print ("7=",neighbors);
  if(col+1<y and row-1>=0 and currentstate[row-1][col+1]=='x'): 
    neighbors=neighbors+1
  #print ("8=",neighbors);
  return neighbors

def iterate(currentstate):
  alivecells=0
  for row in range(x):
    for col in range(y):
      neighbors=getneighbors(currentstate,row,col,currentstate[row][col])
      #print (currentstate[row][col],"=",neighbors);
      if(currentstate[row][col]=='x' and neighbors<2):
         nextstate[row][col]=' ' 
      elif(currentstate[row][col]=='x' and neighbors>3):
         nextstate[row][col]=' ' 
      elif(currentstate[row][col]==' ' and neighbors==3):
         nextstate[row][col]='x'
      else:
         nextstate[row][col]=copy.deepcopy(currentstate[row][col])
      if(nextstate[row][col]=='x'):
         alivecells=alivecells+1;
  print("alivecells=",alivecells)

for t in range(10000):
  os.system('clear')
  for row in nextstate:
    #print (row)
    print(*row, sep='')
  currentstate=copy.deepcopy(nextstate)
  iterate(currentstate)
  print("generation=",t)
  sleep(timeout)

