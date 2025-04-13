import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.NoSuchElementException;
import java.util.*;

public class day1part2 {
    public static void main(String[] args){
        try{
            File data = new File("C:\\Users\\janj\\.vscode\\VSCODE\\AOC23\\2022\\DAY1\\data.txt");
            Scanner myReader = new Scanner(data);
            ArrayList<Integer> maxCalories = new ArrayList<>(Arrays.asList(0, 0, 0));            
            while(myReader.hasNextLine()){
                String line = myReader.nextLine();
                line = line.replace("\n", "");
                int localMaxCalories = 0;
                while(line.length()>3){
                    localMaxCalories += Integer.parseInt(line);
                    try{
                        line = myReader.nextLine();
                    } catch (NoSuchElementException e) {
                        break;
                    }
                }
                maxCalories = isBigger(maxCalories, localMaxCalories);
            }
            int maxSum = 0;
            for(int i=0;i<maxCalories.size();i++){
                maxSum += maxCalories.get(i);
            }
            System.out.println(maxSum);
        } catch (IOException e){
            e.printStackTrace();
        }
    }
    public static ArrayList<Integer> isBigger(ArrayList<Integer> biggest, int maybeBigger){
        for(int i=0;i<biggest.size();i++){
            if(maybeBigger>biggest.get(i)){
                biggest.add(maybeBigger);
                Collections.sort(biggest, Comparator.reverseOrder());
                biggest = new ArrayList<>(biggest.subList(0, 3));
                System.out.println(biggest);
                break;
            }
        }
        return biggest;
    }
}
