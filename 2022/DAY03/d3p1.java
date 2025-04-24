import java.util.*;
import java.io.IOException;
import java.io.File;

public class d3p1{
    public static char priority(String input){
        for(int i=0;i<input.length()/2;i++){
            for(int j=input.length()/2;j<input.length();j++){
                if(input.charAt(i) == input.charAt(j)){
                    return (char) input.charAt(i);
                }
            }
        }
        return '0';
    }
    public static void main(String[] args){
        try{
            File data = new File("C:\\Users\\janj\\.vscode\\VSCODE\\AOC23\\2022\\DAY3\\data.txt");
            Scanner myScanner = new Scanner(data);
            short fileSize = 300;
            int endPriority = 0;
            for(int i=0;i<fileSize;i++){
                String line = myScanner.nextLine();
                char prior = priority(line);
                if(prior == Character.toLowerCase(prior)){
                    endPriority += (int) prior - 96;
                }else{
                    endPriority += (int) prior - 38;
                }
            }
            System.out.println(endPriority);
        } catch (IOException e) {
            e.printStackTrace(); 
        }
    }
}