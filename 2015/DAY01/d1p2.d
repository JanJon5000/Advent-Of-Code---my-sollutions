import std.stdio : writeln;
import std.file : readText;

void main(){
    string fileInput;
    try {
        fileInput = readText("data.txt");
    } catch (Exception e) {
        writeln("Error reading a file ", e.msg);
    }

    int ans = 1;
    int counter = 0;
    for(int i=0;i<fileInput.length;i++){
        if(fileInput[i] == '('){
            counter += 1;
        }else if(fileInput[i] == ')'){
            counter -= 1;
        }

        if(counter == -1){
            ans = i+1;
            break;
        }
    }
    writeln(ans);
}