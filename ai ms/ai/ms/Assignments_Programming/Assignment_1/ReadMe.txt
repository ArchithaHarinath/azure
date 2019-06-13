Name: Harsha Keerthipati
Uta Id: 1001374263

Submission proof: fbc3a3a0-ce2f-4496-bdd9-2f2f68a52a78
5b51b605-9e61-4d01-969d-773eab81e336

Programming Language used: Python

Note: Make sure all the files are in the same directory.

Code Structure:
There are 3 files in total:
1) ucs.py
2) Node.py
3)<input_file>

ucs.py:

This file contains gthe following methods:
1) read_file(file_name): 
This method takes a file as input and reads it and returns the data in the file.

2) adj_node(fringe, routes, vis_node): 
This method returns all the adjacent nodes connected to a node.
It has parameters like fringe (Contains the current nodes that can be used to find a path), routes (contains all the routes in the map which helps us to find all the nodes), vis_node (Holds all the visited nodes). This method returns nothing.

3) get_fringe(routes, source, des_city):
This method sorts the fringe based on the least cost.
It returns nothing

4) path_retrace(des_node):
This method retraces the path from the destination node to source.
It returns nothing

5)ucs(routes, source, des):
This method implements Uninformed cost search on the routes from source to destination.
It returns nothing

6)main():
Code starts from this method

How to run the code:

The command to run the code is:
	python ucs.py <input_file.ext> <source> <destination>
Example:
	python ucs.py input1.txt luebeck kassel

References:

1)https://www.youtube.com/watch?v=5OJv6iHMtVw
2)http://www.seas.upenn.edu/~cis391/Lectures/uninformed-search%20fall%202015.pdf