import java.util.*;
import java.io.File;
import java.io.IOException;

public class d4p1{
    public static int isIn(String[] first, String[] second){
        if(Integer.parseInt(first[0])>=Integer.parseInt(second[0]) && Integer.parseInt(first[1])<=Integer.parseInt(second[1])){
            return 1;
        }
        if(Integer.parseInt(first[0])<=Integer.parseInt(second[0]) && Integer.parseInt(first[1])>=Integer.parseInt(second[1])){
            return 1;
        }
        return 0;
    }
    public static void main(String[] args){
        try {
            short fileLen = 1000;
            int endScore = 0;
            File data = new File("C:\\Users\\janj\\.vscode\\VSCODE\\AOC23\\2022\\DAY4\\data.txt");
            Scanner myScanner = new Scanner(data);
            for(short i=0;i<fileLen;i++){
                String[] placeHolder = myScanner.nextLine().split(",");
                String[][] line = {placeHolder[0].split("-"), placeHolder[1].split("-")};
                System.out.println(line[0][0] + " " + line[0][1] + ", " + line[1][0] + " " + line[1][1] + " " + isIn(line[0], line[1]));
                endScore += isIn(line[0], line[1]);
            }
            System.out.println(endScore);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}