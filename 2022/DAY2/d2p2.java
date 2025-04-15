import java.util.*;
import java.io.File;
import java.io.IOException;

public class d2p2{
    public static int score(String ch){
        switch(ch){
            case "X":
            return 0;
            case "Y":
            return 3;
            case "Z":
            return 6;
        }
        System.out.println("Error");
        return 0;
    }
    public static int whichOutcome(int theirMove, int myOutcome){ 
        int[][] outcome = {{3, 1, 2}, {1, 2, 3}, {2, 3, 1}}; // rock: (scrissors, rock, paper), paper: (rock, paper, scissors), scissors: (paper, scissors, rock)
        return outcome[theirMove][myOutcome];
    }
    public static void main(String[] args){
        try{
            int endScore = 0;
            File data = new File("C:\\Users\\janj\\.vscode\\VSCODE\\AOC23\\2022\\DAY2\\data.txt");
            Scanner myReader = new Scanner(data);
            ArrayList<String> myOutcomes = new ArrayList<>(Arrays.asList("X", "Y", "Z"));
            ArrayList<String> theirMoves = new ArrayList<>(Arrays.asList("A", "B", "C"));
            for(int i=0;i<2500;i++){
                String[] line = myReader.nextLine().split(" ");
                endScore += score(line[1]) + whichOutcome(theirMoves.indexOf(line[0]), myOutcomes.indexOf(line[1]));
            }
            System.out.println(endScore);
        } catch (IOException e){
            e.printStackTrace();
        } 
    }
}