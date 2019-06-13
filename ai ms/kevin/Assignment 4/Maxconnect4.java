import java.util.Scanner;

public class Maxconnect4 {

    public static Scanner input_stream = null;
    public static GameBoard currentGame = null;
    public static AiPlayer aiPlayer = null;
    public static int HUMAN_PIECE;
    public static int COMPUTER_PIECE;
	public static final int ONE = 1;
    public static final int TWO = 2;    
    public static int INVALID = 99;
    public static final String FILEPATH_PREFIX = "../";
    public static final String COMPUTER_FILE = "computer.txt";
    public static final String HUMAN_FILE = "human.txt";

    public enum MODE {
        INTERACTIVE,
        ONE_MOVE
    };

    public enum PLAYER_TYPE {
        HUMAN,
        COMPUTER
    };
	
    public static void main(String[] args) throws CloneNotSupportedException {        
        if (args.length != 4) {
            System.out.println("Four command-line arguments are needed:\n"
                + "Usage: java [program name] interactive [input_file] [computer-next / human-next] [depth]\n"
                + " or:  java [program name] one-move [input_file] [output_file] [depth]\n");
            exit_function(0);
        }
        
        String game_mode = args[0].toString(); 
        String inputFilePath = args[1].toString(); 
        int depthLevel = Integer.parseInt(args[3]);         
        currentGame = new GameBoard(inputFilePath);        
        aiPlayer = new AiPlayer(depthLevel, currentGame);
        if (game_mode.equalsIgnoreCase("interactive")) {
            currentGame.setGameMode(MODE.INTERACTIVE);
            if (args[2].toString().equalsIgnoreCase("computer-next") || args[2].toString().equalsIgnoreCase("C")) {                
                currentGame.setFirstTurn(PLAYER_TYPE.COMPUTER);
                MakeComputerPlay4Interactive();
            } else if (args[2].toString().equalsIgnoreCase("human-next") || args[2].toString().equalsIgnoreCase("H")){
                currentGame.setFirstTurn(PLAYER_TYPE.HUMAN);
                MakeHumanPlay();
            } else {
                System.out.println("\n" + "value for 'next turn' doesn't recognized.  \n try again. \n");
                exit_function(0);
            }
            if (currentGame.isBoardFull()) {
                System.out.println("\nI can't play.\nThe Board is Full\n\nGame Over.");
                exit_function(0);
            }
        } else if (!game_mode.equalsIgnoreCase("one-move")) {
            System.out.println("\n" + game_mode + " is an unrecognized game mode \n try again. \n");
            exit_function(0);
        } else {            
            currentGame.setGameMode(MODE.ONE_MOVE);
            String outputFileName = args[2].toString(); 
            MakeComputerPlay4OneMove(outputFileName);
        }
    }         
    private static void MakeComputerPlay4OneMove(String outputFileName) throws CloneNotSupportedException {                
        int playColumn = 99; 
        boolean playMade = false; 
        System.out.print("\nMaxConnect-4 game:\n");
        System.out.print("Game state before move:\n");        
        currentGame.printGameBoard();        
        System.out.println("Score: Player-1 = " + currentGame.getScore(ONE) + ", Player-2 = " + currentGame.getScore(TWO)
            + "\n ");
        if (currentGame.isBoardFull()) {
            System.out.println("\nI can't play.\nThe Board is Full\n\nGame Over.");
            return;
        }
        int current_player = currentGame.getCurrentTurn();        
        playColumn = aiPlayer.findBestPlay(currentGame);
        if (playColumn == INVALID) {
            System.out.println("\nI can't play.\nThe Board is Full\n\nGame Over.");
            return;
        }        
        currentGame.playPiece(playColumn);        
        System.out.println("move " + currentGame.getPieceCount() + ": Player " + current_player + ", column "
            + (playColumn + 1));
        System.out.print("Game state after move:\n");        
        currentGame.printGameBoard();        
        System.out.println("Score: Player-1 = " + currentGame.getScore(ONE) + ", Player-2 = " + currentGame.getScore(TWO)
            + "\n ");
        currentGame.printGameBoardToFile(outputFileName);
    }    
    private static void MakeComputerPlay4Interactive() throws CloneNotSupportedException {
        printBoardAndScore();
        System.out.println("\n Computer's turn:\n");
        int playColumn = INVALID;         
        playColumn = aiPlayer.findBestPlay(currentGame);
        if (playColumn == INVALID) {
            System.out.println("\nI can't play.\nThe Board is Full\n\nGame Over.");
            return;
        }        
        currentGame.playPiece(playColumn);
        System.out.println("move: " + currentGame.getPieceCount() + " , Player: Computer , Column: " + (playColumn + 1));
        currentGame.printGameBoardToFile(COMPUTER_FILE);
        if (currentGame.isBoardFull()) {
            printBoardAndScore();
            printResult();
        } else {
            MakeHumanPlay();
        }
    }    
    private static void printResult() {
        int human_score = currentGame.getScore(Maxconnect4.HUMAN_PIECE);
        int comp_score = currentGame.getScore(Maxconnect4.COMPUTER_PIECE);        
        System.out.println("\n Final Result:");
        if(human_score > comp_score){
            System.out.println("\n Congratulations!! You won this game."); 
        } else if (human_score < comp_score) {
            System.out.println("\n You lost!! Good luck for the next game.");
        } else {
            System.out.println("\n Game is tie!!");
        }
    }    
    private static void MakeHumanPlay() throws CloneNotSupportedException {      
        printBoardAndScore();
        System.out.println("\n Human's turn:\nKindly play your move here(1-7):");
        input_stream = new Scanner(System.in);
        int playColumn = INVALID;
        do {
            playColumn = input_stream.nextInt();
        } while (!isValidPlay(playColumn));
        currentGame.playPiece(playColumn - 1);
        System.out.println("move: " + currentGame.getPieceCount() + " , Player: Human , Column: " + playColumn);        
        currentGame.printGameBoardToFile(HUMAN_FILE);
        if (currentGame.isBoardFull()) {
            printBoardAndScore();
            printResult();
        } else {
            MakeComputerPlay4Interactive();
        }
    }
    private static boolean isValidPlay(int playColumn) {
        if (currentGame.isValidPlay(playColumn - 1)) {
            return true;
        }
        System.out.println("Error!!...Invalid column , Kindly enter column value between 1 - 7.");
        return false;
    }   
    public static void printBoardAndScore() {
        System.out.print("Game state :\n");
        currentGame.printGameBoard();
        System.out.println("Score: Player-1 = " + currentGame.getScore(ONE) + ", Player-2 = " + currentGame.getScore(TWO)
            + "\n ");
    }   
    private static void exit_function(int value) {
        System.out.println("exiting from MaxConnectFour.java!\n\n");
        System.exit(value);
    }
} 
