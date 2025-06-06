import std.stdio : writeln;
import std.file : readText;
int directions(string input){
    int ans = 0;
    for(int i=0;i<input.length;i++){
        if(input[i] == '('){
            ans += 1;
        }else if(input[i] == ')'){
            ans -= 1;
        }
    }
    return ans;    
}

void main(){
    string fileInput;
    try {
        fileInput = readText("data.txt");
        writeln(directions(fileInput));
    } catch (Exception e) {
        writeln("Error reading a file ", e.msg);
    }
}