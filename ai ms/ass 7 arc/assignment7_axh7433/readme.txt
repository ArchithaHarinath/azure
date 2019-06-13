Name:Architha Harinath	
Student id:1001657433	
Net id:axh7433

					Assignment 7


Programming language used:JAVA

Steps to run the code:
1)compile: javac CheckTrueFalse.java LogicalExpression.java

After compilation the following lines mentioned below appears and ignore these lines and run the
code. 
Note: Some input files use unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.

2)run: java CheckTrueFalse wumpus_rules.txt kb3.txt c.txt


CheckTrueFalse.java

1) In the main() function:
	1) Intialize the value of the pits,monster,stench,breeze arrays.if it is true assign to
value 1 and if starts with not then 0.
	2)calls the ttentails algorithm to check whether it entails the statement or not.
2) ttentails(LogicalExpression knowledge_base, LogicalExpression statement, ArrayList<String> symal, HashMap temp) and
ttcheckall(LogicalExpression knowledge_base, LogicalExpression statement, ArrayList<String> symal, HashMap temp)
function checks the entailment of the statement. 
3) getarrayvalue(String sym) function checks whether the location is true or false. true is the location
has value 1 and false if it has -1.

LogicalExpression.java

1. getvalue(String sym, HashMap<String, Boolean> temp) function gets the value of the symbol from the hashmap temp.
2. isempty() function clears everything from the stack if it is not null 
3. isConnective(String sym) function returns true if the given symbol is a connective else returns false
4. popsym(HashMap temp) functions that pops and evaluates all the symbols from the symbol stack


