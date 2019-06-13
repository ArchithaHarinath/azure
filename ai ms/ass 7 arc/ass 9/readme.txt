Name: Architha Harinath
Student ID: 1001657433
Net ID:axh7433

TASK1:

The Code Structure:

1)The posterior probabilities are calculated and the probability of picking next candy that can be cherry or lime is also calculated and printed to a oputput text file(result.txt). 
2)The Program has following functions:
     1)The main function gets the input from command line
     2)The initvar function instantiate the hypothesis and prior probabilities
     3)calculatePjQj_1 function computes the probability of getting cherry or lime in the next candy.


Programming Language used: Python

How to run the program:
python compute_a_posteriori.py observations

For example:
python compute_a_posteriori.py LCLCLCCCCLC

TASK2:

The Code Structure:
1)In bnet.py, the main function creates list of boolean values depending on the given input and calls computeProbability function for each table row.
2)The function computeProbability takes six parameters,the boolean values for the five variables viz., - burglary, earthquake, alarm, john calling, mary calling 
	and a list of variables that are given as condition.
3)BN.py class file contains function computeProbability.

Programming Language used:Python

How to run the program:
python bnet.py  Bt Af Mf

References:

https://www.investopedia.com/terms/p/posterior-probability.asp

https://astro.uni-bonn.de/~kbasu/ObsCosmo/Slides2012/Lecture3_2012.pdf

https://www.cs.cmu.edu/afs/cs/academic/class/15381-s07/www/slides/032707bayesNets1.pdf

http://www.statisticshowto.com/posterior-distribution-probability/
