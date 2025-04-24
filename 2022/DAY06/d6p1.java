import java.util.*;
import java.io.File;
import java.io.IOException;

public class d6p1{
    public static int countDistinct(String word){
        int num = 0;
        Set<String> placeholder = new HashSet<>();
        for(int i=0;i<word.length();i++)
            placeholder.add(String.valueOf(word.charAt(i)));
        System.out.println(placeholder);
        num = placeholder.size();
        return num;
    }
    public static void main(String[] args){
        try{
            int counter = 0;
            File data = new File("C:\\Users\\janj\\.vscode\\VSCODE\\AOC23\\2022\\DAY06\\data.txt");
            Scanner myScanner = new Scanner(data);
            String line = myScanner.nextLine();
            for(int i=4;i<line.length();i++){
                String sub = line.substring(i-4, i);
                if(countDistinct(sub) == 4){
                    counter = i;
                    break;
                }
            }
            System.out.println(counter);
            myScanner.close();
        } catch(IOException e) {
            e.printStackTrace();
        }
    }
}