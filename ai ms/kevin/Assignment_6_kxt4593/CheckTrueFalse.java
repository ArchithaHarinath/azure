
import java.io.*;
import java.util.*;

import static java.lang.System.exit;
import java.util.logging.Logger;
import java.util.logging.Level;


/**
 * @author james spargo
 *
 */
public class CheckTrueFalse {

    /**
     * @param args
     */
    public static final String resultfile = "result.txt";
    public static int count=0;
	
	
    public static int p[][] = new int[5][5];
    public static int m[][] = new int[5][5];
    public static int s[][] = new int[5][5];
    public static int b[][] = new int[5][5];
	
	
    public static ArrayList<String> symbol1 = new ArrayList();
    public static ArrayList<String> symbol2 = new ArrayList();
	
    public static HashMap model = new HashMap();
    public static boolean negativestmt=false;
    public static void main(String[] args) {

        if (args.length != 3) {
            //takes three arguments
            System.out.println("Usage: " + args[0] + " [wumpus-rules-file] [additional-knowledge-file] [input_file]\n");
            exit_function(0);
        }
        //INITIALIZING m,p,s AND b ARRAYS 
        int i, j;

        for (i = 1; i <5; i++) {
            for (j = 1; j < 5; j++) {
                p[i][j] = -1;
                m[i][j] = -1;
                s[i][j] = -1;
                b[i][j] = -1;
            }
        }

        
        String buffer;
        BufferedReader inputStream;
        BufferedWriter outputStream;

        
        LogicalExpression knowledge_base = new LogicalExpression();
        LogicalExpression statement = new LogicalExpression();

        //open wumpus-rules-file.txt
        try {

            inputStream = new BufferedReader(new FileReader(args[0]));

            //load the wumpus rules
            System.out.println("loading the wumpus rules...");
            //System.out.println(args[0]);
            knowledge_base.setConnective("and");
            //System.out.println(args[0]);
            while ((buffer = inputStream.readLine()) != null) {
                
                int set =0;
                int value = 1;
                String line = buffer;
                String sym = line;
                if (!(buffer.startsWith("#") || (buffer.equals("")))) {
                  initvalues(buffer);
                    LogicalExpression subExpression = readExpression(buffer);
                    knowledge_base.setSubexpression(subExpression);
                } 
				
		     else {
                    // nothing 
                }
            }

            //close the input file
            inputStream.close();

        } catch (Exception e) {
            System.out.println("failed to open " + args[0]);
            e.printStackTrace();
            exit_function(0);
        }
        
        try {
            inputStream = new BufferedReader(new FileReader(args[1]));

            //load the additional knowledge
            System.out.println("loading the additional knowledge...");

            
            while ((buffer = inputStream.readLine()) != null) {
                int value = 1;
                int set=0;
                String line = buffer;
                String sym = line;
                if (!(buffer.startsWith("#") || (buffer.equals("")))) {
                    
                     initvalues(buffer);
                    
                    LogicalExpression subExpression = readExpression(buffer);
                    knowledge_base.setSubexpression(subExpression);
                } else {
                    // nothing 
                }
            }

            //close the input file
            inputStream.close();

        } catch (Exception e) {
            System.out.println("failed to open " + args[1]);
            e.printStackTrace();
            exit_function(0);
        }
        
        if (!valid_expression(knowledge_base)) {
            System.out.println("invalid knowledge base");
            exit_function(0);
        }

        // print the knowledge_base
        knowledge_base.print_expression("\n");

        // read the statement file
        try {
            inputStream = new BufferedReader(new FileReader(args[2]));

            System.out.println("\n\nLoading the statement file...");
            
            while ((buffer = inputStream.readLine()) != null) {

                if (!buffer.startsWith("#")) {
                    //the line is not a comment

                    statement = readExpression(buffer);
                    break;
                } 
				
				else {
                    
                }
            }

            //close the input file
            inputStream.close();

        } catch (Exception e) {
            System.out.println("failed to open " + args[2]);
            e.printStackTrace();
            exit_function(0);
        }
        
        if (!valid_expression(statement)) {
            System.out.println("invalid statement");
            exit_function(0);
        }

        
        statement.print_expression("");
        
        System.out.println("\n");
        
       
       for(i=1;i<=4;i++)
       {
           for(j=1;j<=4;j++)
           {
               if(m[i][j]==-1)
               {
                   symbol1.add("M_"+i+"_"+j);
                   model.put("M_"+i+"_"+j, false);
               }
               if(p[i][j]==-1)
               {
                   symbol1.add("P_"+i+"_"+j);
                   model.put("P_"+i+"_"+j, false);
               }
               if(s[i][j]==-1)
               {
                   symbol1.add("S_"+i+"_"+j);
                   model.put("S_"+i+"_"+j, false);
               }
               if(b[i][j]==-1)
               {
                   symbol1.add("B_"+i+"_"+j);
                   model.put("B_"+i+"_"+j, false);
               }
                              
           }
       }
      
        symbol2=new ArrayList(symbol1);
        //tt entails 
        boolean ans=ttentails(knowledge_base,statement,symbol1,model);
        negativestmt=true;
        count=0;
        boolean notans=ttentails(knowledge_base,statement,symbol2,model);
        negativestmt=false;
        
        
        //let us evaluate the final result of this entailment process
        //prints the output on the console
        String eval="";
        if(ans && !notans)
            eval="definitely true";
        else if(!ans && notans)
            eval="definitely false";
        else if(ans && notans)
            eval="both true and false";
        else if(!ans && !notans)
            eval="possibly true, possibly false";
        System.out.println("OUTPUT:");
        System.out.println(eval);
        
        
        try {
            //print the output to a output file
            BufferedWriter output=new BufferedWriter(new FileWriter(resultfile));
            output.write(eval+"\n");
            output.close();
        } catch (IOException ex) {
            System.out.println("cannot write to the output file");
            Logger.getLogger(CheckTrueFalse.class.getName()).log(Level.SEVERE, null, ex);
            
        }
       

    } //end of main


    public static void initvalues(String line)
   {


               int values_to_assign =1 ;
                     String symbol = line;
					 
        String symbol_initials = null;
                String[] symbol_literals = new String[3];

        if (!line.startsWith("(")) { // checks if line contains only unique symbol i.e 'B_2_3'

            values_to_assign = 1;
        } else if ((line.startsWith("(not") || line.startsWith("(NOT"))
            && !(line.startsWith("(not (") || line.startsWith("(NOT ("))) { // checks if line contains only negation of symbol
                                                                            // i.e '(not M_2_3)'
            values_to_assign = 0;
            symbol = line.substring(line.indexOf(" ") + 1, line.indexOf(")"));
        } else {
            return;
        }

        symbol_literals = symbol.split("_");
        symbol_initials = symbol_literals[0];
        int pos_x = Integer.parseInt(symbol_literals[1]);
        int pos_y = Integer.parseInt(symbol_literals[2]);

        if (symbol_initials.equals("M")) {
           m[pos_x][pos_y] = values_to_assign;
        } else if (symbol_initials.equals("P")) {
            p[pos_x][pos_y] = values_to_assign;
        } else if (symbol_initials.equals("S")) {
            s[pos_x][pos_y] = values_to_assign;
        } else if (symbol_initials.equals("B")) {
            b[pos_x][pos_y] = values_to_assign;
        } else {
            System.out.println("Oops...Incorrect knowlwdge base format!!");
        }

   }


    private static boolean ttentails(LogicalExpression knowledge_base, LogicalExpression statement, ArrayList<String> symbolal, HashMap symbolModel)
    {
        return ttcheckall(knowledge_base,statement,symbolal,symbolModel);
    }
    
   
    private static boolean ttcheckall(LogicalExpression knowledge_base, LogicalExpression statement,ArrayList<String> symbolal, HashMap symbolModel)
    {
        if(symbolal.isEmpty())
        {
            if(pltrue(knowledge_base,symbolModel,false))
            {
                return pltrue(statement,symbolModel,negativestmt);
            }
            else{
            return true;
            }
        }
        else
        {
            String firstsymbol=symbolal.remove(0);
            ArrayList<String> rem=symbolal;
            return (ttcheckall(knowledge_base,statement,rem,Extends(firstsymbol,true,symbolModel))&&(ttcheckall(knowledge_base,statement,rem,Extends(firstsymbol,false,symbolModel))));
        }
        }
    
   
 private static boolean pltrue(LogicalExpression logicalstmt,HashMap symbolModel,boolean negativestmt)
{
    boolean res=logicalstmt.solveExpression(symbolModel);
    LogicalExpression.clearstack();
    if(negativestmt)
    {
        return !res;
    }
    else
    {
        return res;
    }
}
//it assigns the value to the symbol and puts it into the symbol model  
private static HashMap Extends(String firstsymbol,boolean val,HashMap symbolModel)
{
    symbolModel.put(firstsymbol,val);
    return symbolModel;
}
 
    public static LogicalExpression readExpression(String input_string) {
        LogicalExpression result = new LogicalExpression();

        input_string = input_string.trim();

        if (input_string.startsWith("(")) {
            //its a subexpression

            String symbolString = "";

            // remove the '(' from the input string
            symbolString = input_string.substring(1);
            //symbolString.trim();

            if (!symbolString.endsWith(")")) {
                // missing the closing paren - invalid expression
                System.out.println("missing ')' !!! - invalid expression! - readExpression():-" + symbolString);
                exit_function(0);

            } else {
                //remove the last ')'
                //it should be at the end
                symbolString = symbolString.substring(0, (symbolString.length() - 1));
                symbolString.trim();
			  
                symbolString = result.setConnective(symbolString);

            }

            //read the subexpressions into a vector and call setSubExpressions( Vector );
            result.setSubexpressions(read_subexpressions(symbolString));

        } else {
          
            result.setUniqueSymbol(input_string);

        }

        return result;
    }

   
    public static Vector<LogicalExpression> read_subexpressions(String input_string) {

        Vector<LogicalExpression> symbolList = new Vector<LogicalExpression>();
        LogicalExpression newExpression;// = new LogicalExpression();
        String newSymbol = new String();

        input_string.trim();

        while (input_string.length() > 0) {

            newExpression = new LogicalExpression();

            //testing
            //System.out.println("read subexpression() entered while with input_string.length ->" + input_string.length() +"<-");
            if (input_string.startsWith("(")) {
               
                int parenCounter = 1;
                int matchingIndex = 1;
                while ((parenCounter > 0) && (matchingIndex < input_string.length())) {
                    if (input_string.charAt(matchingIndex) == '(') {
                        parenCounter++;
                    } else if (input_string.charAt(matchingIndex) == ')') {
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

            } else {
                //its a unique symbol ( if its not, setUniqueSymbol() will tell us )

                // I only want the first symbol, so, create a LogicalExpression object and
                // add the object to the vector
                if (input_string.contains(" ")) {
                    //remove the first string from the string
                    newSymbol = input_string.substring(0, input_string.indexOf(" "));
                    input_string = input_string.substring((newSymbol.length() + 1), input_string.length());

                    //testing
                    //System.out.println( "read_subExpression: i just read ->" + newSymbol + "<- and i have left ->" + input_string +"<-" );
                } else {
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

            if (input_string.startsWith(" ")) {
                //remove the leading whitespace
                input_string = input_string.substring(1);
            }

            //testing
            //System.out.println("read_subExpression() - left to parse ->" + input_string + "<-afterTrim with string length-" + input_string.length() + "<- end of while");
        }
        return symbolList;
    }

    public static boolean valid_expression(LogicalExpression expression) {

   
        if (!(expression.getUniqueSymbol() == null) && (expression.getConnective() == null)) {
            // we have a unique symbol, check to see if its valid
            return valid_symbol(expression.getUniqueSymbol());

            //testing
            //System.out.println("valid_expression method: symbol is not empty!\n");
        }

       
        if ((expression.getConnective().equalsIgnoreCase("if"))
                || (expression.getConnective().equalsIgnoreCase("iff"))) {

            // the connective is either 'if' or 'iff' - so check the number of connectives
            if (expression.getSubexpressions().size() != 2) {
                System.out.println("error: connective \"" + expression.getConnective()
                        + "\" with " + expression.getSubexpressions().size() + " arguments\n");
                return false;
            }
        } // end 'if / iff' check
        // check for 'not'
        else if (expression.getConnective().equalsIgnoreCase("not")) {
            // the connective is NOT - there can be only one symbol / subexpression
            if (expression.getSubexpressions().size() != 1) {
                System.out.println("error: connective \"" + expression.getConnective() + "\" with " + expression.getSubexpressions().size() + " arguments\n");
                return false;
            }
        } // end check for 'not'
        // check for 'and / or / xor'
        else if ((!expression.getConnective().equalsIgnoreCase("and"))
                && (!expression.getConnective().equalsIgnoreCase("or"))
                && (!expression.getConnective().equalsIgnoreCase("xor"))) {
            System.out.println("error: unknown connective " + expression.getConnective() + "\n");
            return false;
        }
        // end check for 'and / or / not'
        // end connective check

        // checks for validity of the logical_expression 'symbols' that go with the connective
        for (Enumeration e = expression.getSubexpressions().elements(); e.hasMoreElements();) {
            LogicalExpression testExpression = (LogicalExpression) e.nextElement();

            // for each subExpression in expression,
            //check to see if the subexpression is valid
            if (!valid_expression(testExpression)) {
                return false;
            }
        }

        //testing
        //System.out.println("The expression is valid");
        // if the method made it here, the expression must be valid
        return true;
    }

   
    public static boolean valid_symbol(String symbol) {
        if (symbol == null || (symbol.length() == 0)) {

         
            return false;
        }

        for (int counter = 0; counter < symbol.length(); counter++) {
            if ((symbol.charAt(counter) != '_')
                    && (!Character.isLetterOrDigit(symbol.charAt(counter)))) {

                System.out.println("String: " + symbol + " is invalid! Offending character:---" + symbol.charAt(counter) + "---\n");

                return false;
            }
        }

        // the characters of the symbol string are either a letter or a digit or an underscore,
        //return true
        return true;
    }

    private static void exit_function(int value) {
        System.out.println("exiting from checkTrueFalse");
        System.exit(value);
    }
     static boolean getarrayvalue(String sym)
    {
        String[] line=new String[3];
        int x;
        int y;
        String l;
        line=sym.split("_");
        l=line[0];
        x=Integer.parseInt(line[1]);
        y=Integer.parseInt(line[2]);
        if(l.equals("M"))
        {
            if(m[x][y]==1)
            {return true;
            }
            else
                return false;
        }
        else if(l.equals("P"))
        {
            if(p[x][y]==1)
                return true;
            else
                return false;
            
        }
        else if(l.equals("S"))
        {
            if(s[x][y]==1)
                return true;
            else
                return false;
            
        }
        else if(l.equals("B"))
        {
            if(b[x][y]==1)
                return true;
            else
                return false;
            
        }
        else
        {
            System.out.println("Unacceptable format of symbol");
        }
        return false;
        
    }

    

    
}
