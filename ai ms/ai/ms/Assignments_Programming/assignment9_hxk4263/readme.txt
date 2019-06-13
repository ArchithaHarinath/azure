Name: Harsha Keerthipati
Id: 1001374263

Programming Language used: Python 2.7

How to run the code:

Task 1:
python pp.py [Observations]

Output: Output will be printed in result.txt file in the same folder.

Task 2:
python bayenet.py [queries] given [observations]

Output: Output will be printed on the console.

Code Structure:

Task 1:

Hypothesis for all the bag conditions are written in the main function. After Running the pp.py file with observations as command line arguments input, it is taken into obs list and length of the observations is calculated. Then posterior probability for each character input and probability for picking up a cherry or lime in the observation sequence is calculated in each pass and final probability for picking up a cherry and lime will be printed out into the result.txt.

Task 2:
A Bayenet Class is created which takes object as parameter where the object consists of queries and observations. The class calculates the probability of the input combination of events given any other combination of events. This class is later called after taking the input from the command line arguments.The output is printed on the command prompt or console.

References:

https://www.investopedia.com/terms/p/posterior-probability.asp

https://astro.uni-bonn.de/~kbasu/ObsCosmo/Slides2012/Lecture3_2012.pdf

https://www.cs.cmu.edu/afs/cs/academic/class/15381-s07/www/slides/032707bayesNets1.pdf

http://www.statisticshowto.com/posterior-distribution-probability/

