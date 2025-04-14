import java.io.File;
import java.io.IOException;
import java.util.*;

public class d2p1{
    public static int scoreOutcome(int myMove, int theirMove){
        int[][] outcome = {{3, 0, 6}, {6, 3, 0}, {0, 6, 3}};
        return outcome[myMove][theirMove];
        }
    public static void main(String[] args){
        try{
            File data = new File("C:\\Users\\janj\\.vscode\\VSCODE\\AOC23\\2022\\DAY2\\data.txt");
            Scanner myReader = new Scanner(data);
            ArrayList<String> myMoves = new ArrayList<>(Arrays.asList("X", "Y", "Z"));
            ArrayList<String> theirMoves = new ArrayList<>(Arrays.asList("A", "B", "C"));
            int endScore = 0;
            for(int i=0;i<2500;i++){
                String[] line = myReader.nextLine().split(" ");
                endScore += 1 + myMoves.indexOf(line[1]) + scoreOutcome(myMoves.indexOf(line[1]), theirMoves.indexOf(line[0]));
                }
            System.out.println(endScore);
        } catch (IOException e){
            e.printStackTrace();
        } 
    }
}