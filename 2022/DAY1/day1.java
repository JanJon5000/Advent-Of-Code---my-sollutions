
import java.nio.file.Paths;
import java.nio.file.Path;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.NoSuchElementException;

public class day1 {
    public static void main(String[] args) {
        try{
            Path path = Paths.get("C:\\Users\\janj\\.vscode\\VSCODE\\AOC23\\2022\\DAY1\\data.txt");
            File data = new File("C:\\Users\\janj\\.vscode\\VSCODE\\AOC23\\2022\\DAY1\\data.txt");
            Scanner myReader = new Scanner(data);
            int maxCalories = 0;
            while(myReader.hasNextLine()){
                int localMaxCalories = 0;
                String nextLine = myReader.nextLine();
                while(nextLine.length()>2){
                    localMaxCalories += toInt(nextLine);
                    maxCalories = Math.max(localMaxCalories, maxCalories);
                    try{
                        nextLine = myReader.nextLine();
                    } catch (NoSuchElementException e) {
                        break;
                    }
                       
                }
            }
            System.out.println(maxCalories);
       
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static int toInt(String word){
        int result = 0;
        word = word.replace("\n", "");
        for(int i=0; i < word.length(); i++){
            result += (int)word.charAt(i) - 48;
            if(i<word.length()-1){
                result *= 10;
            }
        }
        return result;
    }
}