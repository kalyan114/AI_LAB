#Graph implementation...DFS....
                
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
  
def dfs(g,r,vis=None):
    if vis is None:vis=set()
    vis.add(r)
    print(r,end=' ')
    for i in g[r]:
      if i not in vis:dfs(g,i,vis)

if __name__=="__main__":
    g={
        'A':['B','C','D'],
        'B':['A'],
        'C':['A','D'],
        'D':['A','C','E'],
        'E':['D'],
    }
    r=(input("Enter node for traversal:"))
    dfs(g,r)
    
    
Input:
  
Enter node for traversal:A
  
Output:
  
A B C D E 
