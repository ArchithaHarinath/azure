                                                   ASSIGNMENT 4

Name :Kevin Thomas 

UTA ID:1001544593

Programming language used is java.

Section: 5360-001

How the code is structured:
Maxconnect4 :
	

      
1)MakeHumanPlay() -this function does the work of taking input from user and makes the next move for human player.
     
2)MakeComputerPlay4OneMove() - this function is used when the computer have to make a move for a one-move mode game.
3)printBoardAndScore() - this function shows the current score and the board's current state.
        
4)MakeComputerPlay4Interactive() - this function is used when the computer have to make a move for an interactive mode game.
        
5)printResult() - this function displays the final score and declares winner or tie.

        


AiPlayer :

      
1)findBestPlay() - this function makes a make a move based on min and max value from the below given two functions
       
2)Calculate_Min_Utility() - this function gives the min value.
     
3)Calculate_Min_Utility() - this function gives the max value.


GameBoard :
        

        
1)getscore() - this function takes the current score and send it to printBoardAndScore() to print score.
        
2)getCurrentTurn() - this function traces the current turn.
        
3)getGameBoard() - this function takes the current gameboard state and pass it to printGameBoard() function.
        
4)printGameBoard() - this function displays the current board state.
        

       

5)exit_function()- this function exits from the game.

How to run the code:

1)javac Maxconnect4.java AiPlayer.java GameBoard.java
  
2)INTERACTIVE MODE:
It can be excuted by the command  
{java Maxconnect4 interactive 'input_file' (computer/human-next) [depth]}
egs:
{java Maxconnect4 interactive input1.txt human-next 5;}

3)ONE-MOVE MODE:
It can be excuted by the command
{java Maxconnect4 one-move 'input_file' 'output_file' [depth]}
egs:
{java Maxconnect4 one-move input1.txt output.txt 10;}

4)GETTING EXECUTION TIME:
   {time java Maxconnect4 one-move 'input_file' 'output_file' [depth]}
  egs:
   {time java Maxconnect4 one-move input1.txt output.txt 10;}
  sample output:
  real    0m1.473s
  user    0m1.675s
  sys     0m0.060s


 Depth limit vs CPU runtime

Depth-1	
real    0m0.090s
user    0m0.039s
sys     0m0.005s
Depth-2	
real    0m0.098s
user    0m0.080s
sys     0m0.011s
Depth-3	
real    0m0.098s
user    0m0.089s
sys     0m0.013s
Depth-4	
real    0m0.099s
user    0m0.094s
sys     0m0.011s
Depth-5	
real    0m0.099s
user    0m0.108s
sys     0m0.012s
Depth-6	
real    0m0.178s
user    0m0.241s
sys     0m0.023s
Depth-7	
real    0m0.189s
user    0m0.303s
sys     0m0.033s
Depth-8	
real    0m0.248s
user    0m0.484s
sys     0m0.049s
Depth-9	
real    0m0.433s
user    0m0.618s
sys     0m0.053s
Depth-10	
real    0m1.473s
user    0m1.675s
sys     0m0.060s



