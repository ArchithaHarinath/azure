                                                                                Kevin Thomas
                                                                                1001544593
                                    ASSIGNMENT 6



CheckTrueFalse.java

1. initializing values for the arrays ,it reads a line from the kb,if it starts with not or NOT, it initializes the value of the sym to 0
   else if it is normal , it initializes it to 1.
   eg if we have M[1][2] it is 1 whereas not M[1][2] is 0
2. it calls the ttcheckall functions of the tt entails algorithm
3. a model is a row in the truth table,this function is used to create such rows for unknown symbols
   it then checks if the statement entails with the knowledge base or not
4. for a given model, it checks if the given statement is true
5. it assigns the value to the symbol and puts it into the symbol model

   
LogicalExpression.java

1. get value gets the value of the symbol from the model
2. clears everything from the symbol stack 
3. returns true if the given symbol is a connective else returns false
4. functions that pops and evaluates all the symbols from the symbol stack



Execution:
1. Compile:  javac CheckTrueFalse.java

2. Run : java CheckTrueFalse wumpus_rules.txt kb3.txt a.txt
