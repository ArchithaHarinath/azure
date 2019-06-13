                                                         ASSIGNMENT 1

Name :Kevin Thomas 

UTA ID:1001544593

Programming language used is phyton.

Section: 5360-001

How the code is structured:
Tree Search function is created which returns the solution or failure for the fuction based on the fringe that we have created using linked list and a node is created and if the fringe is 
empty then it will return failure.If it attains goals state it will output the fringe which contains the nodes in the path and the total distance it took to travel and it outputs the shortest path.
The fringe is  sorted based on the cumulative cost in an ascending order.The Expand function which is implemented is used to expand its successors from the given node.The successor function adds the neighbouring nodes and stores its distance along with its cost and depth.
If there is a path available in the input it gives the route and the distance it takes to reach the goal state and if there is no path it returns infinity.(i.e)
If the fringe becomes empty and the state is not found, then there is no path between the source and the destination then it returns infinity.

How to run the code:
It can be excuted by the command  {python find_route.py 'input1.txt' 'Source' 'Destination'}


Sample Output:
1)python find_route.py 'input1.txt' 'Luebeck' 'Stuttgart'

('Luebeck->Hamburg', 63)
('Hamburg->Hannover', 153)
('Hannover->Kassel', 165)
('Kassel->Frankfurt', 185)
('Stuttgart->Frankfurt', 200)
 766

2)python find_route.py 'input1.txt' 'Luebeck' 'London'

No path exists
Infinite
