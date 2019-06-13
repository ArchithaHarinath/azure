
import java.io.*;
import java.util.*;
import java.util.logging.Logger;
import java.util.logging.Level;

/**
 * @author Architha
 *
 */
public class CheckTrueFalse
{
   
    public static final String result = "result.txt";
    public static int c = 0;
    public static int pit[][] = new int[5][5];
    public static int monster[][] = new int[5][5];
    public static int stench[][] = new int[5][5];
    public static int breeze[][] = new int[5][5];
    public static ArrayList<String> s = new ArrayList();
    public static ArrayList<String> s1 = new ArrayList();
    public static HashMap board = new HashMap();
    public static boolean stmt = false;


    public static void main(String[] args)
    {

        if (args.length != 3)
        {
            //takes three arguments
            System.out.println("Usage: " + args[0] + " [wumpus-rules-file] [additional-knowledge-file] [input_file]\n");
            exit_function(0);
        }

        //create some buffered IO streams
        String buffer;
        BufferedReader inputStream;
        BufferedWriter outputStream;
        
        //create the knowledge base and the statement
        LogicalExpression knowledge_base = new LogicalExpression();
        LogicalExpression statement = new LogicalExpression();

        //open wumpus-rules-file.txt
        try
        {

            inputStream = new BufferedReader(new FileReader(args[0]));

            //load the wumpus rules
            System.out.println("loading the wumpus rules...");
            //System.out.println(argstench[0]);
            knowledge_base.setConnective("and");
            //System.out.println(argstench[0]);
            while ((buffer = inputStream.readLine()) != null)
            {

                int set = 0;
                int value = 1;
                String line = buffer;
                String sym = line;
                if (!(buffer.startsWith("#") || (buffer.equals(""))))
                {
                    initvalues(buffer);
                    LogicalExpression subExpression = readExpression(buffer);
                    knowledge_base.setSubexpression(subExpression);
                }
                else 
                {
		//the line is a comment. do nothing and read the next line
		}


            }
            //close the input file
            inputStream.close();

        } 
        catch (Exception e)
        {
            System.out.println("failed to open " + args[0]);
            e.printStackTrace();
            exit_function(0);
        }
        //end reading wumpus rules
        
        //read the additional knowledge file
        try
        {
            inputStream = new BufferedReader(new FileReader(args[1]));

            //load the additional knowledge
            System.out.println("loading the additional knowledge...");
            // the connective for knowledge_base is already set.  no need to set it again.
	    // i might want the LogicalExpression.setConnective() method to check for that
	    //knowledge_base.setConnective("and");
			
            while ((buffer = inputStream.readLine()) != null)
            {
                int value = 1;
                int set = 0;
                String line = buffer;
                String sym = line;
                if (!(buffer.startsWith("#") || (buffer.equals(""))))
                {

                    initvalues(buffer);

                    LogicalExpression subExpression = readExpression(buffer);
                    knowledge_base.setSubexpression(subExpression);
                } 
                else
                {
                    //the line is a comment. do nothing and read the next line
                }
            }

            //close the input file
            inputStream.close();

        } 
        catch (Exception e)
        {
            System.out.println("failed to open " + args[1]);
            e.printStackTrace();
            exit_function(0);
        }
        //end reading additional knowledge
        
        //check for a valid knowledge_base
        if (!valid_expression(knowledge_base))
        {
            System.out.println("invalid knowledge base");
            exit_function(0);
        }

        // print the knowledge_base
        knowledge_base.print_expression("\n");

        // read the statement file
        try
        {
            inputStream = new BufferedReader(new FileReader(args[2]));

            System.out.println("\n\nLoading the statement file...");
            //buffer = inputStream.readLine();
			
	    // actually read the statement file
	    // assuming that the statement file is only one line long


            while ((buffer = inputStream.readLine()) != null)
            {

                if (!buffer.startsWith("#"))
                {
                    //the line is not a comment

                    statement = readExpression(buffer);
                    break;
                } 
                else
                {
                    //the line is a commend. no nothing and read the next line

                }
            }

            //close the input file
            inputStream.close();

        } 
        catch (Exception e)
        {
            System.out.println("failed to open " + args[2]);
            e.printStackTrace();
            exit_function(0);
        }
        // end reading the statement file
		
	// check for a valid statement

        if (!valid_expression(statement))
        {
            System.out.println("invalid statement");
            exit_function(0);
        }
        //print the statement
        statement.print_expression("");
        //print a new line
        System.out.println("\n");
        
        //testing
	//System.out.println("I don't know if the statement is definitely true or definitely false.");
        int i, j;
        for (i = 1; i < 5; i++)
        {
            for (j = 1; j < 5; j++)
            {
                pit[i][j] = -1;
                monster[i][j] = -1;
                stench[i][j] = -1;
                breeze[i][j] = -1;
            }
        }

        for (i = 1; i <= 4; i++)
        {
            for (j = 1; j <= 4; j++)
            {
                if (monster[i][j] == -1)
                {
                    s.add("M_" + i + "_" + j);
                    board.put("M_" + i + "_" + j, false);
                }
                if (pit[i][j] == -1)
                {
                    s.add("P_" + i + "_" + j);
                    board.put("P_" + i + "_" + j, false);
                }
                if (stench[i][j] == -1)
                {
                    s.add("S_" + i + "_" + j);
                    board.put("S_" + i + "_" + j, false);
                }
                if (breeze[i][j] == -1)
                {
                    s.add("B_" + i + "_" + j);
                    board.put("B_" + i + "_" + j, false);
                }

            }
        }

        s1 = new ArrayList(s);
        boolean trueresult = ttentails(knowledge_base, statement, s, board);
        stmt = true;
        c = 0;
        boolean nottrueresult = ttentails(knowledge_base, statement, s1, board);
        stmt = false;
        String status = "";
        if (trueresult && nottrueresult)
        {
           status = "both true and false";
        }
        else if (!trueresult && !nottrueresult)
        {
           status = "possibly true, possibly false";
        }
        else if (!trueresult && nottrueresult)
        {
           status = "definitely false";
        }
        else if (trueresult && !nottrueresult)
        {
           status = "definitely true";
        } 
        
        System.out.println("OUTPUT:");
        System.out.println(status);

       /* try
        {
            //print the output to a output file
            BufferedWriter output = new BufferedWriter(new FileWriter(result));
            output.write(status + "\n");
            output.close();
        } 
        catch (IOException ex)
        {
            System.out.println("cannot write to the output file");
            Logger.getLogger(CheckTrueFalse.class.getName()).log(Level.SEVERE, null, ex);

        }*/

    } //end of main
    
public static LogicalExpression readExpression(String input_string)
    {
        LogicalExpression result = new LogicalExpression();
        
        //testing
          //System.out.println("readExpression() beginning -"+ input_string +"-");
          //testing
          //System.out.println("\nread_exp");


        input_string = input_string.trim();
        input_string = input_string.trim();

        
        if (input_string.startsWith("("))
        {
            //its a subexpression

            String symbolString = "";

            // remove the '(' from the input string
            symbolString = input_string.substring(1);
            //symbolString.trim();
            
            //testing
            //System.out.println("readExpression() without opening paren -"+ symbolString + "-");


            if (!symbolString.endsWith(")"))
            {
                // missing the closing paren - invalid expression
                System.out.println("missing ')' !!! - invalid expression! - readExpression():-" + symbolString);
                exit_function(0);

            } 
            else
            {
                //remove the last ')'
                //it should be at the end
                symbolString = symbolString.substring(0, (symbolString.length() - 1));
                symbolString.trim();
                
                //testing
              //System.out.println("readExpression() without closing paren -"+ symbolString + "-");
              
              // read the connective into the result LogicalExpression object					  

                symbolString = result.setConnective(symbolString);
                
                //testing
              //System.out.println("added connective:-" + result.getConnective() + "-: here is the string that is left -" + symbolString + "-:");
              //System.out.println("added connective:->" + result.getConnective() + "<-");


            }

            //read the subexpressions into a vector and call setSubExpressions( Vector );
            result.setSubexpressions(read_subexpressions(symbolString));

        } 
        else
        {
             	
            // the next symbol must be a unique symbol
            // if the unique symbol is not valid, the setUniqueSymbol will tell us.
            result.setUniqueSymbol(input_string);

            //testing
            //System.out.println(" added:-" + input_string + "-:as a unique symbol: readExpression()" );

        }

        return result;
    }
    
    /* this method reads in all of the unique symbols of a subexpression
	 * the only place it is called is by read_expression(String, long)(( the only read_expression that actually does something ));
	 * 
	 * each string is EITHER:
	 * - a unique Symbol
	 * - a subexpression
	 * - Delineated by spaces, and paren pairs
	 * 
	 * it returns a vector of logicalExpressions
	 * 
	 * 
	 */

    public static Vector<LogicalExpression> read_subexpressions(String input_string)
    {

        Vector<LogicalExpression> symbolList = new Vector<LogicalExpression>();
        LogicalExpression newExpression;// = new LogicalExpression();
        String newSymbol = new String();
        
        //testing
	//System.out.println("reading subexpressions! beginning-" + input_string +"-:");
	//System.out.println("\nread_sub");

        input_string.trim();

        while (input_string.length() > 0)
        {

            newExpression = new LogicalExpression();

            //testing
            //System.out.println("read subexpression() entered while with input_string.length ->" + input_string.length() +"<-");
            
            if (input_string.startsWith("("))
            {
                //its a subexpression.
		// have readExpression parse it into a LogicalExpression object

		//testing
		//System.out.println("read_subexpression() entered if with: ->" + input_string + "<-");
			
		// find the matching ')'

                int parenCounter = 1;
                int matchingIndex = 1;
                while ((parenCounter > 0) && (matchingIndex < input_string.length()))
                {
                    if (input_string.charAt(matchingIndex) == '(')
                    {
                        parenCounter++;
                    } 
                    else if (input_string.charAt(matchingIndex) == ')')
                    {
                        parenCounter--;
                    }
                    matchingIndex++;
                }

                // read untill the matching ')' into a new string
                newSymbol = input_string.substring(0, matchingIndex);

                //testing
                //System.out.println( "-----read_subExpression() - calling readExpression with: ->" + newSymbol + "<- matchingIndex is ->" + matchingIndex );
                // pass that string to readExpression,
                newExpression = readExpression(newSymbol);

                // add the LogicalExpression that it returns to the vector symbolList
                symbolList.add(newExpression);

                // trim the logicalExpression from the input_string for further processing
                input_string = input_string.substring(newSymbol.length(), input_string.length());

            } 
            else
            {
                //its a unique symbol ( if its not, setUniqueSymbol() will tell us )

                // I only want the first symbol, so, create a LogicalExpression object and
                // add the object to the vector
                
                if (input_string.contains(" "))
                {
                    //remove the first string from the string
                    newSymbol = input_string.substring(0, input_string.indexOf(" "));
                    input_string = input_string.substring((newSymbol.length() + 1), input_string.length());

                    //testing
                    //System.out.println( "read_subExpression: i just read ->" + newSymbol + "<- and i have left ->" + input_string +"<-" );
                } 
                else
                {
                    newSymbol = input_string;
                    input_string = "";
                }

                //testing
                //System.out.println( "readSubExpressions() - trying to add -" + newSymbol + "- as a unique symbol with ->" + input_string + "<- left" );
                newExpression.setUniqueSymbol(newSymbol);

                //testing
                //System.out.println("readSubexpression(): added:-" + newSymbol + "-:as a unique symbol. adding it to the vector" );
                symbolList.add(newExpression);

                //testing
                //System.out.println("read_subexpression() - after adding: ->" + newSymbol + "<- i have left ->"+ input_string + "<-");
            }

            //testing
            //System.out.println("read_subExpression() - left to parse ->" + input_string + "<-beforeTrim end of while");
            input_string.trim();

            if (input_string.startsWith(" "))
            {
                //remove the leading whitespace
                input_string = input_string.substring(1);
            }

            //testing
            //System.out.println("read_subExpression() - left to parse ->" + input_string + "<-afterTrim with string length-" + input_string.length() + "<- end of while");
        }
        return symbolList;
    }
    
    /* this method checks to see if a logical expression is valid or not 
	 * a valid expression either:
	 * ( this is an XOR )
	 * - is a unique_symbol
	 * - has:
	 *  -- a connective
	 *  -- a vector of logical expressions
	 *  
	 * */
    public static boolean valid_expression(LogicalExpression expression)
    {
        
        
	// checks for an empty symbol
	// if symbol is not empty, check the symbol and
	// return the truthiness of the validity of that symbol

        if (!(expression.getUniqueSymbol() == null) && (expression.getConnective() == null))
        {
            // we have a unique symbol, check to see if its valid
            return valid_symbol(expression.getUniqueSymbol());

            //testing
            //System.out.println("valid_expression method: symbol is not empty!\n");
        }

        if ((expression.getConnective().equalsIgnoreCase("if"))
                || (expression.getConnective().equalsIgnoreCase("iff")))
        {

            // the connective is either 'if' or 'iff' - so check the number of connectives
            if (expression.getSubexpressions().size() != 2)
            {
                System.out.println("error: connective \"" + expression.getConnective()
                        + "\" with " + expression.getSubexpressions().size() + " arguments\n");
                return false;
            }
        } // end 'if / iff' check
        // check for 'not'
        else if (expression.getConnective().equalsIgnoreCase("not"))
        {
            // the connective is NOT - there can be only one symbol / subexpression
            if (expression.getSubexpressions().size() != 1)
            {
                System.out.println("error: connective \"" + expression.getConnective() + "\" with " + expression.getSubexpressions().size() + " arguments\n");
                return false;
            }
        } // end check for 'not'
        // check for 'and / or / xor'
        else if ((!expression.getConnective().equalsIgnoreCase("and"))
                && (!expression.getConnective().equalsIgnoreCase("or"))
                && (!expression.getConnective().equalsIgnoreCase("xor")))
        {
            System.out.println("error: unknown connective " + expression.getConnective() + "\n");
            return false;
        }
        // end check for 'and / or / not'
        // end connective check

        // checks for validity of the logical_expression 'symbols' that go with the connective
        for (Enumeration e = expression.getSubexpressions().elements(); e.hasMoreElements();)
        {
            LogicalExpression testExpression = (LogicalExpression) e.nextElement();

            // for each subExpression in expression,
            //check to see if the subexpression is valid
            if (!valid_expression(testExpression))
            {
                return false;
            }
        }

        //testing
        //System.out.println("The expression is valid");
        
        // if the method made it here, the expression must be valid
        return true;
    }

    public static boolean valid_symbol(String symbol)
    {
        if (symbol == null || (symbol.length() == 0))
        {

            return false;
        }

        for (int counter = 0; counter < symbol.length(); counter++)
        {
            if ((symbol.charAt(counter) != '_')
                    && (!Character.isLetterOrDigit(symbol.charAt(counter))))
            {

                System.out.println("String: " + symbol + " is invalid! Offending character:---" + symbol.charAt(counter) + "---\n");

                return false;
            }
        }

        // the characters of the symbol string are either a letter or a digit or an underscore,
        //return true
        return true;
    }

    private static void exit_function(int value)
    {
        System.out.println("exiting from checkTrueFalse");
        System.exit(value);
    }

    
        public static void initvalues(String line)
    {

        int assignment = 1;
        String symbol = line;
        String symbol_i = null;
        String[] symbol_lit = new String[3];

        
        if (!line.startsWith("("))
        { 
            assignment = 1;
        } 
        else if ((line.startsWith("(not") || line.startsWith("(NOT"))
                && !(line.startsWith("(not (") || line.startsWith("(NOT (")))
        { 
            assignment = 0;
            symbol = line.substring(line.indexOf(" ") + 1, line.indexOf(")"));
        } 
        else
        {
            return;
        }

        symbol_lit = symbol.split("_");
        symbol_i = symbol_lit[0];
        int location_x = Integer.parseInt(symbol_lit[1]);
        int location_y = Integer.parseInt(symbol_lit[2]);

        if (symbol_i.equals("M"))
        {
            monster[location_x][location_y] = assignment;
        } 
        else if (symbol_i.equals("P"))
        {
            pit[location_x][location_y] = assignment;
        } 
        else if (symbol_i.equals("S"))
        {
            stench[location_x][location_y] = assignment;
        } 
        else if (symbol_i.equals("B"))
        {
            breeze[location_x][location_y] = assignment;
        } 
        else
        {
            System.out.println("Oops...Incorrect knowlwdge base format!!");
        }

    }

    private static boolean ttentails(LogicalExpression knowledge_base, LogicalExpression statement, ArrayList<String> symal, HashMap temp)
    {
        return ttcheckall(knowledge_base, statement, symal, temp);
    }

    private static boolean ttcheckall(LogicalExpression knowledge_base, LogicalExpression statement, ArrayList<String> symal, HashMap temp)
    {
        if (symal.isEmpty())
        {
            if (pltrue(knowledge_base, temp, false))
            {
                return pltrue(statement, temp, stmt);
            } 
            else
            {
                return true;
            }
        } 
        else
        {
            String firstsymbol = symal.remove(0);
            ArrayList<String> rem = symal;
            return (ttcheckall(knowledge_base, statement, rem, Extends(firstsymbol, true, temp)) && (ttcheckall(knowledge_base, statement, rem, Extends(firstsymbol, false, temp))));
        }
    }

    private static boolean pltrue(LogicalExpression logicalstmt, HashMap temp, boolean stmt)
    {
        boolean res = logicalstmt.solution(temp);
        LogicalExpression.isempty();
        if (stmt)
        {
            return !res;
        } 
        else
        {
            return res;
        }
    }
    private static HashMap Extends(String firstsymbol, boolean val, HashMap temp)
    {
        temp.put(firstsymbol, val);
        return temp;
    }
    
    static boolean getarrayvalue(String sym)
    {
        String[] symbol = new String[3];
        symbol = sym.split("_");
        String l=symbol[0];
        int x=Integer.parseInt(symbol[1]);
        int y=Integer.parseInt(symbol[2]);
        if (l.equals("P"))
        {
            if (pit[x][y] == 1)
            {
                return true;
            } 
            else
            {
                return false;
            }

        }
        else if (l.equals("M"))
        {
            if (monster[x][y] == 1)
            {
                return true;
            }
            else
            {
                return false;
            }
        } 
         else if (l.equals("B"))
        {
            if (breeze[x][y] == 1)
            {
                return true;
            } 
            else
            {
                return false;
            }

        } 
         else if (l.equals("S"))
        {
            if (stench[x][y] == 1)
            {
                return true;
            } 
            else
            {
                return false;
            }

        }
        else
        {
            System.out.println("Unacceptable format of symbol");
        }
        return false;

    }
   }
