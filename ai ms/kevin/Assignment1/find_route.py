# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:08:05 2018

@author: kevin
"""
import sys
class Node:
    def __init__(self):
        self.data = 0
        self.next = None
        self.parent = None
        self.depth = 0
        self.city = ''
    def getData(self):
        return self.data

def find_neighbours(source,links):
    neighbours = []
    for s,d in links.keys():
        if s==source:
            neighbours.append(d)
        elif d==source:
            neighbours.append(s)
    return neighbours    

def print_path(source,links):
    l = []
    while source.parent:
        if (source.city,source.parent.city) in links:
            l.append([source.city,source.parent.city,links[source.city,source.parent.city]])
        else:
            l.append([source.parent.city,source.city,links[source.parent.city,source.city]])
        source = source.parent
    l.reverse()
    for i,j,k in l:
        print(i+"->"+j,k)
        
file = open(sys.argv[1])
links = {}
val = file.readline()
s_input = sys.argv[2]
d_input = sys.argv[3]
while val:
    source,dest,dist = val.split()
    links[source,dest] = int(dist)
    val = file.readline()
    if str.strip(val) == 'END OF INPUT':
        break
source = Node()
source.city = 'head'
fringe = [(s_input,0,None)]
visited = []
dest = d_input
f = 0
while True:
    if len(fringe) <= 0:
        break
    first,d,parent = fringe.pop(0)
    #print(source.city,first,fringe,1)
    if first in visited:
        #print('continued')
        continue
    node = Node()
    source = parent
    if first ==s_input:
        node.data = 0
    elif (first,source.city) in links:
        node.data = source.data+links[first,source.city]
    elif (source.city,first) in links:
        node.data = source.data+links[source.city,first]
    else:
        continue
    node.parent = source
    node.city = first
    visited.append(first)
    if first == dest:
        print_path(node,links)
        print(node.data)
        f = 1
        break
    successors = find_neighbours(first,links)
    for s in successors:
        new = Node()
        new.city = s
        new.parent = node
        new.depth = node.depth + 1
        if (node.city,s) in links:
            new.data = node.data+links[node.city,s]
        elif (s,node.city) in links:
            new.data = node.data+links[s,node.city]
        fringe.append((new.city,new.data,node))
    #print(first,successors,3)        
    fringe.sort(key = lambda x:x[1])
    #print(fringe)
    #print(visited)  
if f==0:
    print('No path exists')
    print('Infinite')