
import java.util.*;

/**
 * @author James Spargo
 *
 */
public class LogicalExpression {

    public static boolean Finalresult;
     public static Stack<String> symbolstack=new Stack();
    
    
    
	    private String uniqueSymbol = null; 	
	        private String connective = null; 		
       	    private Vector<LogicalExpression> subexpressions = null;   
	
		  public LogicalExpression()
		{
				this.subexpressions = new Vector<LogicalExpression>();
		}
		
	

	
		public LogicalExpression( LogicalExpression oldExpression ) {
			
			if( oldExpression.getUniqueSymbol() == null) {
				this.uniqueSymbol = oldExpression.getUniqueSymbol();
			} else {
				
				this.connective = oldExpression.getConnective();
			
				
				for( Enumeration e = oldExpression.getSubexpressions().elements(); e.hasMoreElements(); ) {
					LogicalExpression nextExpression = (LogicalExpression)e.nextElement();
					
					this.subexpressions.add( nextExpression );
				}
			}
			
		}
	
		
		public void setUniqueSymbol( String newSymbol ) 
            {
			boolean valid = true;

			//remove the leading whitespace
			newSymbol.trim();
			
			if( this.uniqueSymbol != null ) 
                  {
			      System.out.println("setUniqueSymbol(): - this LE already has a unique symbol!!!" +
							"\nswapping :->" + this.uniqueSymbol + "<- for ->" + newSymbol +"<-\n");
			} 
                  else if( valid ) 
                  {
					this.uniqueSymbol = newSymbol;
					
			} 
		}

		
		public String setConnective( String inputString ) {
			
			String connect;
			inputString.trim();
			if( inputString.startsWith("(") ) {
				inputString = inputString.substring( inputString.indexOf('('), inputString.length() );
				inputString.trim();
			}
			

			if( inputString.contains( " " ) ) {
				// remove the connective out of the string
				connect = inputString.substring( 0, inputString.indexOf( " " )) ;
				inputString = inputString.substring( ( connect.length() + 1 ), inputString.length() );
				
				
			} else {
				connect = inputString;
				inputString = "";
			}
			
			// if connect is a proper connective
			if ( connect.equalsIgnoreCase( "if" ) ||
					connect.equalsIgnoreCase( "iff" ) ||
					connect.equalsIgnoreCase( "and" ) ||
					connect.equalsIgnoreCase("or") ||
					connect.equalsIgnoreCase("xor") || 
					connect.equalsIgnoreCase( "not" ) ) {
				
				// set the connective
				this.connective = connect;
				
				return inputString;
				
			} else {
				System.out.println( "unexpected character! : INVALID connective! - setConnective():-" + inputString );
				this.exit_function( 0 );
			}
			
			System.out.println(" INVALID connective! : setConnective:-" + inputString );
			return inputString;
		}
		
		public void setSubexpression( LogicalExpression newSub ) {
			this.subexpressions.add(newSub);
		}
		
		public void setSubexpressions( Vector<LogicalExpression> symbols ) {
			this.subexpressions = symbols;
			
		}
		
		public String getUniqueSymbol(){
			return this.uniqueSymbol;
		}
		
		public String getConnective() {
			return this.connective;
		}
		
		public LogicalExpression getNextSubexpression() {
			return this.subexpressions.lastElement();
		}
		
		public Vector getSubexpressions() {
			return this.subexpressions;
		}

		

		public void print_expression( String separator ) {

		  if ( !(this.uniqueSymbol == null) )
		  {
			  System.out.print( this.uniqueSymbol.toUpperCase() );
		  } else {
			  
			  LogicalExpression nextExpression;
			  
			  // print the connective
			  System.out.print( "(" + this.connective.toUpperCase() );

			  // enumerate over the 'symbols' ( LogicalExpression objects ) and print them
			  for( Enumeration e = this.subexpressions.elements(); e.hasMoreElements(); ) {
				  nextExpression = ( LogicalExpression )e.nextElement();
				  
				  System.out.print(" ");
				  nextExpression.print_expression("");
				  System.out.print( separator );
				  }
			  
			  System.out.print(")");
			  }
		}

        private static void exit_function(int value) {
                System.out.println("exiting from LogicalExpression");
                  System.exit(value);
                }
        
        public static void clearstack()
        {
            if(symbolstack!=null)
			
                symbolstack.clear();
        }

   
   
   
        public boolean solveExpression(HashMap symbolModel)
        {
            if(this.getUniqueSymbol()!=null)
            {   
                symbolstack.push(this.getUniqueSymbol());
                
            }
            else
            {
             LogicalExpression nextexp;
			 
             //pushing the connectives into the stack
             symbolstack.push(this.getConnective());
             for(Enumeration e=this.subexpressions.elements();e.hasMoreElements();)
             {
                 nextexp=(LogicalExpression)e.nextElement();
                 nextexp.solveExpression(symbolModel);
                 
             }
             
            Finalresult=POPnEvalsymbol(symbolModel);
            }
            return Finalresult;
        }
        
        
        public boolean isConnective(String sym)
        {
            if(sym.equalsIgnoreCase("if")||sym.equalsIgnoreCase("iff")||sym.equalsIgnoreCase("and")||sym.equalsIgnoreCase("or")||sym.equalsIgnoreCase("xor")||sym.equalsIgnoreCase("not"))
            {
                return true;
            }
            return false;
        }
        
        public boolean getvalue(String sym, HashMap<String,Boolean> symbolModel)
        {
            if(sym.equalsIgnoreCase("t"))
               return true;
            else if(sym.equalsIgnoreCase("f"))
                return false;
            else if(symbolModel.get(sym)==null)
            { 
                return CheckTrueFalse.getarrayvalue(sym);
                
            }
            else
            {
                return symbolModel.get(sym);
            }
        }
        
        public boolean POPnEvalsymbol(HashMap symbolModel)
        {
            boolean res=false;
            String sym;
            String connective;
            ArrayList<String> uniqueSymbol=new ArrayList();
            
            
            
            do{
                sym=symbolstack.pop();
                uniqueSymbol.add(sym);
            }
            while(!isConnective(sym));
            
            
            uniqueSymbol.remove(sym);
            connective=sym;
            //if the connective is a if connective
            if(connective.equalsIgnoreCase("if"))
            {
                res=true;
                //for if to exist, we need two symbols
                 if(uniqueSymbol.size()==2)
                 {
                     
                    boolean s1=getvalue(uniqueSymbol.get(0),symbolModel);
                    boolean s2=getvalue(uniqueSymbol.get(1),symbolModel);
                     //if s2 and not of s1
                     if(getvalue(uniqueSymbol.get(1),symbolModel)&&!getvalue(uniqueSymbol.get(0),symbolModel))
                     {
                         res=false;
                     }
                 }
                 
            }
            else if(connective.equalsIgnoreCase("iff"))
            {
                res=false;
                //requires two symbols
                if(uniqueSymbol.size()==2)
                {
                    boolean s1=getvalue(uniqueSymbol.get(0),symbolModel);
                    boolean s2=getvalue(uniqueSymbol.get(1),symbolModel);
                    
                    if((s1&&s2)||(!s1&&!s2))
                    {
                        res=true;
                    }
                }
            }
            else if(connective.equalsIgnoreCase("and"))
            {
                res=true;
                
                while (!uniqueSymbol.isEmpty() && res) {
                res = res && getvalue(uniqueSymbol.remove(0), symbolModel);
                 }
            }
            else if(connective.equalsIgnoreCase("or"))
            {
                res = false;
                //for or to exists any one can be true 
            while (!uniqueSymbol.isEmpty() && !res) {
                res = res || getvalue(uniqueSymbol.remove(0), symbolModel);
            }
            }
            else if(connective.equalsIgnoreCase("not"))
            {
                //gives us the negated value of the symbol
                res = true;
            res = !getvalue(uniqueSymbol.remove(0), symbolModel);
                
                
                
            }
            else if(connective.equalsIgnoreCase("xor"))
            {
                
                res = false;
            int no_sym = 0;
            while (!uniqueSymbol.isEmpty()) {
                if (getvalue(uniqueSymbol.remove(0), symbolModel)) {
                    no_sym++;
                }
            }
            if (no_sym== 1) {
                res = true;
            }
            
             
            }
                          
                
            else {
            //else it is a connective that is not if, iff, and , or, not or xor
             System.out.println("incorrect connective");
                   
                    
        }
        if (res) {
            symbolstack.push("t");
        } else {
            symbolstack.push("f");
        }
        
        return res;
	}
}
