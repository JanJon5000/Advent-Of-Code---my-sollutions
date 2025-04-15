import java.io.File;
import java.util.*;
import java.io.IOException;

public class d3p2 {
    public static char priority(ArrayList<String> group){
        boolean[] flags = {false, false};
        String dontBother = "";
        for(int i=0;i<group.get(0).length();i++){
            if(dontBother.contains(String.valueOf(group.get(0).charAt(i)))){
                continue;
            }else{
                for(int j=0;j<group.get(1).length();j++){
                    if(group.get(1).charAt(j)==group.get(0).charAt(i)){
                        flags[0] = true;
                        break;
                    }
                }
                if(flags[0]==true){
                    for(int k=0;k<group.get(2).length();k++){
                        if(group.get(2).charAt(k)==group.get(0).charAt(i)){
                            flags[1] = true;
                            break;
                        }
                    }
                }
            if(flags[0] == true && flags[1] == true){
                return (char) group.get(0).charAt(i);
            } else {
                flags = new boolean[]{false, false};
                dontBother += group.get(0).charAt(i);
            }
                
            }
        }
        return '0';
    }
    public static void main(String[] args){
        try{
            File data = new File("C:\\Users\\janj\\.vscode\\VSCODE\\AOC23\\2022\\DAY3\\data.txt");
            Scanner myReader = new Scanner(data);
            int fileLen = 100;
            int endPriority = 0;
            for(int i=0;i<fileLen;i++){
                ArrayList<String> group = new ArrayList<>();
                for(int j=0;j<3;j++){
                    group.add(myReader.nextLine());
                }
                char prior = priority(group);
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
