Name: Kevin Thomas
UTA ID: 1001544593

TASK1:

1) Programming Language - Python

2) How the Code is Structure:

->The program computes the posterior probabilities and also calculates the prbability of next candy being picked as lime or cherries
->The Program has following functions:
     ->The main function gets the input from command line
     ->The initvar function instantiate the hypothesis and prior probabilities and calculatePjQj_1 function computes the probability of getting cherry or lime in the next candy.
->At each iteration the computed probability is printed in the output file

3) How to run the program:
python compute_a_posteriori.py observations

For example:
python compute_a_posteriori.py CLCLCL

TASK2:

1) Programming Language - Python

2) How to run the program:
	e.g. python bnet.py  Bt Af Mf

3) How the code is structured?
->	BayesianNetwork.py is a class file which contains function computeProbability. 
->	In bnet.py, the main function creates list of boolean values depending on the given input and calls computeProbability function for each table row.
->      The prior probability values has been saved in the dictionary
->	The function computeProbability takes six parameters, 
	the boolean values for the five variables viz., - burglary, earthquake, alarm, john calling, mary calling 
	and a list of variables that are given as condition.
