#water jug using bfs...

import os,sys,io,math
from re import *
from math import *
from array import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
from statistics import *
from collections import *

def bfs(a,b,t):
  m={};p=[]
  ok=False
  q=deque()
  q.append((0,0))
  while len(q)>0:
    u=q.popleft()
    #if this state already visited then continue..
    if (u[0],u[1]) in m:continue
    if u[0]>a or u[1]>b or u[0]<0 or u[1]<0:continue
    #now we know that not visited.so fill vector for soln
    p.append([u[0],u[1]])
    #marking the state visited so that no repetition occours..
    m[(u[0],u[1])]=1
    #if we reach soln state then updating res=1
    if u[0]==t or u[1]==t:
      ok=True
      if u[0]==t and u[1]:p.append([u[0],0])
      else:
        if u[0]:p.append([0,u[1]])
      #finally displaying the soln path
      for i in range(len(p)):
        if i+1<len(p):print('(',p[i][0],',',p[i][1],')',end='=>')
        else:print('(',p[i][0],',',p[i][1],')')
      break
    #if we dont reach final state,then start developing intermediate states..
    q.append([u[0],b])
    q.append([a,u[1]])
    for i in range(max(a,b)+1):
      #pour amount i from j2 to j1
      c,d=u[0]+i,u[1]-i
      if c==a or d>=0:q.append([c,d])
      #pour amount i from j1 to j2
      c,d=u[0]-i,u[1]+i
      if c>=0 or d==b:q.append([c,d])
    #empty j2
    q.append([a,0])
    #empty j1
    q.append([0,b])
  if not ok:print('No solution!!!')

if __name__=='__main__':
  print("Enter j1,j2 and target:")
  a,b,t=map(int,(input().split()))
  print('The path for given data is:')
  bfs(a,b,t)
  
  
  
Input:
  
Enter j1,j2 and target:
5 4 2

Output:
  
The path for given data is:
( 0 , 0 )=>( 0 , 4 )=>( 5 , 0 )=>( 5 , 4 )=>( 1 , 3 )=>( 2 , 2 )=>( 2 , 0 )
