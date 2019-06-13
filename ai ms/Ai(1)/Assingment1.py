# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:31:46 2018

@author: kevin
"""

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

def print_path(source):
    while source.parent:
        print (source.city)
        source = source.parent
file = open("C:\\Users\\kevin\\Desktop\\input1.txt")
links = {}
val = file.readline()
while val:
    source,dest,dist = val.split()
    links[source,dest] = int(dist)
    val = file.readline()
    if str.strip(val) == 'END OF INPUT':
        break
source = Node()
source.city = 'head'
fringe = [('Luebeck',0)]
visited = []
dest = 'Munich'
while True:
    if len(fringe) <= 0:
        break
    first = fringe.pop(0)[0]
    if first in visited:
        continue
    visited.append(first)
    node = Node()
    node.city = first
    node.parent = source
    if (source.city,first) in links:
            node.data = source.data+links[source.city,first]
    elif (first,source.city) in links:
            node.data = source.data+links[first,source.city]
    if first == dest:
        print_path(node)
        print(node.data)
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
        fringe.append((new.city,new.data))
    source = node    
    fringe.sort(key = lambda x:x[1])
