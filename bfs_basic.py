#Graph implementation...BFS....

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

def bfs(g,r):
    vis=[]
    q=[]
    q.append(r)
    vis.append(r)
    while q:
        x=q.pop()
        print(x,end=' ')
        for i in g[x]:
            if i not in vis:
                vis.append(i)
                q.append(i)

if __name__=="__main__":
    g={
        'A':['B','C','D'],
        'B':['A'],
        'C':['A','D'],
        'D':['A','C','E'],
        'E':['D'],
    }
    r=(input("Enter node for traversal:"))
    bfs(g,r)
    
    
Input:

Enter node for traversal:A

Output:
  
A D E C B 
