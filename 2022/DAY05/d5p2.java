import java.util.*;
import java.io.File;
import java.io.IOException;

public class d5p2{
    public static void main(String[] args){
        try {
            File data = new File("C:\\Users\\janj\\.vscode\\VSCODE\\AOC23\\2022\\DAY5\\data.txt");
            Scanner myScanner = new Scanner(data);
            byte n = 9;
            String[][] arrayStacks = new String[n][8];
            short loopRounds = 502;
            for(byte i=0;i<8;i++){
                String line = myScanner.nextLine();
                for(byte j=0;j<n;j++){
                    arrayStacks[j][i] = line.substring(4*j, 4*j+4);
                }
            }
            @SuppressWarnings("unchecked")
            Stack<String>[] stacks = new Stack[n];
            for(byte j=0;j<n;j++){
                stacks[j] = new Stack<>();
                for(byte i=7;i>=0;i--){
                    if (stacks[j] != null && arrayStacks[j][i] != null && arrayStacks[j][i].trim().isEmpty() == false) {
                        stacks[j].push(arrayStacks[j][i]);
                    }
                }
            }
            ArrayList<String> removed = new ArrayList<String>();
            for(short i=0;i<loopRounds;i++){
                List<String> line = new ArrayList<>(Arrays.asList(myScanner.nextLine().split(" ")));
                line.remove(0);
                line.remove(1);
                line.remove(2);
                for(int j=0;j<Integer.parseInt(line.get(0));j++){
                    removed.add(stacks[Integer.parseInt(line.get(1))-1].pop());
                }
                
                for(int j=removed.size()-1;j>=0;j--){
                    stacks[Integer.parseInt(line.get(2))-1].push(String.valueOf(removed.get(j)));
                    removed.remove(j);
                }
                
            }
            String endString = "";
            for(byte i=0;i<9;i++){
                String add = stacks[i].pop().replace("]", "").replace("[", "");
                endString += add;
            }
            System.out.println(endString);
            myScanner.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}