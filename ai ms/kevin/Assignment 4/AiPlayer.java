import java.util.*;

public class AiPlayer {

    public int depth_level;
    public GameBoard gameBoardShallow;

    
    public AiPlayer(int depth, GameBoard currentGame) {
        this.depth_level = depth;
        this.gameBoardShallow = currentGame;
    }
    
    public int findBestPlay(GameBoard currentGame) throws CloneNotSupportedException {
        int playChoice = Maxconnect4.INVALID;
        if (currentGame.getCurrentTurn() == Maxconnect4.ONE) {
            int v = Integer.MAX_VALUE;
            for (int i = 0; i < GameBoard.NOFCOLS; i++) {
                if (currentGame.isValidPlay(i)) {
                    GameBoard nextMoveBoard = new GameBoard(currentGame.getGameBoard());
                    nextMoveBoard.playPiece(i);
                    int value = Calculate_Max_Utility(nextMoveBoard, depth_level, Integer.MIN_VALUE, Integer.MAX_VALUE);
                    if (v > value) {
                        playChoice = i;
                        v = value;
                    }
                }
            }
        } else {
            int v = Integer.MIN_VALUE;
            for (int i = 0; i < GameBoard.NOFCOLS; i++) {
                if (currentGame.isValidPlay(i)) {
                    GameBoard nextMoveBoard = new GameBoard(currentGame.getGameBoard());
                    nextMoveBoard.playPiece(i);
                    int value = Calculate_Min_Utility(nextMoveBoard, depth_level, Integer.MIN_VALUE, Integer.MAX_VALUE);
                    if (v < value) {
                        playChoice = i;
                        v = value;
                    }
                }
            }
        }
        return playChoice;
    }
    private int Calculate_Min_Utility(GameBoard gameBoard, int depth_level, int alpha_value, int beta_value)
        throws CloneNotSupportedException {        
        if (!gameBoard.isBoardFull() && depth_level > 0) {
            int v = Integer.MAX_VALUE;
            for (int i = 0; i < GameBoard.NOFCOLS; i++) {
                if (gameBoard.isValidPlay(i)) {
                    GameBoard board4NextMove = new GameBoard(gameBoard.getGameBoard());
                    board4NextMove.playPiece(i);
                    int value = Calculate_Max_Utility(board4NextMove, depth_level - 1, alpha_value, beta_value);
                    if (v > value) {
                        v = value;
                    }
                    if (v <= alpha_value) {
                        return v;
                    }
                    if (beta_value > v) {
                        beta_value = v;
                    }
                }
            }
            return v;
        } else {
            return gameBoard.getScore(Maxconnect4.TWO) - gameBoard.getScore(Maxconnect4.ONE);
        }
    }    
    private int Calculate_Max_Utility(GameBoard gameBoard, int depth_level, int alpha_value, int beta_value)
        throws CloneNotSupportedException {       
        if (!gameBoard.isBoardFull() && depth_level > 0) {
            int v = Integer.MIN_VALUE;
            for (int i = 0; i < GameBoard.NOFCOLS; i++) {
                if (gameBoard.isValidPlay(i)) {
                    GameBoard board4NextMove = new GameBoard(gameBoard.getGameBoard());
                    board4NextMove.playPiece(i);
                    int value = Calculate_Min_Utility(board4NextMove, depth_level - 1, alpha_value, beta_value);
                    if (v < value) {
                        v = value;
                    }
                    if (v >= beta_value) {
                        return v;
                    }
                    if (alpha_value < v) {
                        alpha_value = v;
                    }
                }
            }
            return v;
        } else {            
            return gameBoard.getScore(Maxconnect4.TWO) - gameBoard.getScore(Maxconnect4.ONE);
        }
    }
}
