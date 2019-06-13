
import java.util.*;

/**
 * @author Architha
 *
 */
public class LogicalExpression
{
   
    private String symlist = null;             // null if sentence is a more complex expression
    private String connective = null;               // null if sentence is a _UNIQUE_ symbol
    private Vector<LogicalExpression> subexpressions = null;     // a vector of LogicalExpressions ( basically a vector of unique symbols and subexpressions )
		
    //constructor
    public LogicalExpression()
    {
        this.subexpressions = new Vector<LogicalExpression>();
    }

    // another constructor that will ( or is supposed to ) create
    // a new logical Expression, essentially making a copy
    public LogicalExpression(LogicalExpression oldExpression)
    {

        if (oldExpression.getUniqueSymbol() == null)
        {
            this.symlist = oldExpression.getUniqueSymbol();
        } 
        else
        {

            this.connective = oldExpression.getConnective();

            for (Enumeration e = oldExpression.getSubexpressions().elements(); e.hasMoreElements();)
            {
                LogicalExpression nextExpression = (LogicalExpression) e.nextElement();

                this.subexpressions.add(nextExpression);
            }
        }

    }
    
    /* this method replaces _part_ of read_word()
     * this method sets the symbol for the LogicalExpression
     * it checks to make sure that it starts with one of the appropriate letters,
     * then checks to make sure that the rest of the string is either digits or '_'
     */
    public void setUniqueSymbol(String newSymbol)
    {
        boolean valid = true;

        //remove the leading whitespace
        newSymbol.trim();

        if (this.symlist != null)
        {
            System.out.println("setUniqueSymbol(): - this LE already has a unique symbol!!!"
                    + "\nswapping :->" + this.symlist + "<- for ->" + newSymbol + "<-\n");
        } 
        else if (valid)
        {
            this.symlist = newSymbol;
            //testing
            //System.out.println(" setUniqueSymbol() - added-" + newSymbol + "- to the LogicalExpression! ");
        }
    }

    /* this method replaces _part_ of read_word() from the example code 
     * it sets the connective for this LogicalExpression
     * 
     * and returns the rest of the string to collect the symbols for it
     */
    public String setConnective(String inputString)
    {

        String connect;
        
        //testing
	//System.out.println("setConnective() - beginning -" + inputString + "-");
			
	// trim the whitespace at the beginning of the string if there is any
	// there shouldn't be
        inputString.trim();
        
        // if the first character of the inputString is a '('
	// - remove the ')' and the ')' and any whitespace after it.
        if (inputString.startsWith("("))
        {
            inputString = inputString.substring(inputString.indexOf('('), inputString.length());
            
            //trim the whitespace
            inputString.trim();
        }

        //testing
	//System.out.println("here: setConnective1- inputString:" + inputString + "--");
        if (inputString.contains(" "))
        {
            // remove the connective out of the string
            connect = inputString.substring(0, inputString.indexOf(" "));
            inputString = inputString.substring((connect.length() + 1), inputString.length());

            //inputString.trim();
				
	    //testing
       	    //System.out.println("I have the connective -" + connect + "- and i've got symbols -" + inputString + "-");
        } 
        else
        {
            // just set to get checked and empty the inputString
            // huh?
            connect = inputString;
            inputString = "";
        }

        // if connect is a proper connective
        if (connect.equalsIgnoreCase("if")
                || connect.equalsIgnoreCase("iff")
                || connect.equalsIgnoreCase("and")
                || connect.equalsIgnoreCase("or")
                || connect.equalsIgnoreCase("xor")
                || connect.equalsIgnoreCase("not"))
        {
            // ok, first word in the string is a valid connective

            // set the connective
            this.connective = connect;

            //testing
            //System.out.println( "setConnective(): I have just set the connective\n->" + connect + "<-\nand i'm returning\n->" + inputString + "<-" );
            return inputString;

        } 
        else
        {
            System.out.println("unexpected character! : INVALID connective! - setConnective():-" + inputString);
            this.exit_function(0);
        }
        
        // invalid connective - no clue who it would get here
        System.out.println(" INVALID connective! : setConnective:-" + inputString);
        return inputString;
    }

    public void setSubexpression(LogicalExpression newSub)
    {
        this.subexpressions.add(newSub);
    }

    public void setSubexpressions(Vector<LogicalExpression> symbols)
    {
        this.subexpressions = symbols;

    }

    public String getUniqueSymbol()
    {
        return this.symlist;
    }

    public String getConnective()
    {
        return this.connective;
    }

    public LogicalExpression getNextSubexpression()
    {
        return this.subexpressions.lastElement();
    }

    public Vector getSubexpressions()
    {
        return this.subexpressions;
    }

    /************************* end getters and setters *************/

    public void print_expression(String separator)
    {

        if (!(this.symlist == null))
        {
            System.out.print(this.symlist.toUpperCase());
        } 
        else
        {
            // else the symbol is a nested logical expression not a unique symbol
            LogicalExpression nextExpression;

            // print the connective
            System.out.print("(" + this.connective.toUpperCase());

            // enumerate over the 'symbols' ( LogicalExpression objects ) and print them
            for (Enumeration e = this.subexpressions.elements(); e.hasMoreElements();)
            {
                nextExpression = (LogicalExpression) e.nextElement();

                System.out.print(" ");
                nextExpression.print_expression("");
                System.out.print(separator);
            }

            System.out.print(")");
        }
    }

    private static void exit_function(int value)
    {
        System.out.println("exiting from LogicalExpression");
        System.exit(value);
    }
    
    public static boolean endSolution;
    public static Stack<String> tempsstack = new Stack();
    public static void isempty()
    {
        if (tempsstack != null)

        {
            tempsstack.clear();
        }
    }
    public boolean solution(HashMap temp)
    {
        if (this.getUniqueSymbol() != null)
        {
            tempsstack.push(this.getUniqueSymbol());

        } 
        else
        {
            LogicalExpression nextexp;
            tempsstack.push(this.getConnective());
            for (Enumeration e = this.subexpressions.elements(); e.hasMoreElements();)
            {
                nextexp = (LogicalExpression) e.nextElement();
                nextexp.solution(temp);

            }

            endSolution = popsym(temp);
        }
        return endSolution;
    }

    public boolean isConnective(String sym)
    {
        if (sym.equalsIgnoreCase("if") || sym.equalsIgnoreCase("iff") || sym.equalsIgnoreCase("and") || sym.equalsIgnoreCase("or") || sym.equalsIgnoreCase("xor") || sym.equalsIgnoreCase("not"))
        {
            return true;
        }
        return false;
    }

    public boolean getvalue(String sym, HashMap<String, Boolean> temp)
    {
        if (sym.equalsIgnoreCase("t"))
        {
            return true;
        } 
        else if (sym.equalsIgnoreCase("f"))
        {
            return false;
        } 
        else if (temp.get(sym) == null)
        {
            return CheckTrueFalse.getarrayvalue(sym);

        } 
        else
        {
            return temp.get(sym);
        }
    }
    
    public boolean popsym(HashMap temp)
    {
        boolean res = false;
        String sym;
        String connective;
        ArrayList<String> symlist = new ArrayList();

        do
        {
            sym = tempsstack.pop();
            symlist.add(sym);
        } while (!isConnective(sym));

        symlist.remove(sym);
        connective = sym;
        if (connective.equalsIgnoreCase("xor"))
        {

            res = false;
            int no_sym = 0;
            while (!symlist.isEmpty())
            {
                if (getvalue(symlist.remove(0), temp))
                {
                    no_sym++;
                }
            }
            if (no_sym == 1)
            {
                res = true;
            }

        } 
        else if (connective.equalsIgnoreCase("iff"))
        {
            res = false;
            if (symlist.size() == 2)
            {
                boolean s1 = getvalue(symlist.get(0), temp);
                boolean s2 = getvalue(symlist.get(1), temp);

                if ((s1 && s2) || (!s1 && !s2))
                {
                    res = true;
                }
            }
        } 
        else if (connective.equalsIgnoreCase("if"))
        {
            res = true;
            if (symlist.size() == 2)
            {

                boolean s1 = getvalue(symlist.get(0), temp);
                boolean s2 = getvalue(symlist.get(1), temp);
                if (getvalue(symlist.get(1), temp) && !getvalue(symlist.get(0), temp))
                {
                    res = false;
                }
            }

        } 
        else if (connective.equalsIgnoreCase("not"))
        {
            res = true;
            res = !getvalue(symlist.remove(0), temp);

        }        
        else if (connective.equalsIgnoreCase("and"))
        {
            res = true;
            while (!symlist.isEmpty() && res)
            {
                res = res && getvalue(symlist.remove(0), temp);
            }
        } 
        else if (connective.equalsIgnoreCase("or"))
        {
            res = false;
            while (!symlist.isEmpty() && !res)
            {
                res = res || getvalue(symlist.remove(0), temp);
            }
        } 
        else
        {
            System.out.println("incorrect connective");
        }
        
        if (res)
        {
            tempsstack.push("t");
        } 
        else
        {
            tempsstack.push("f");
        }

        return res;
    }
 
}
