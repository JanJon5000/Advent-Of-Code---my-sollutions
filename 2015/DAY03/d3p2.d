import std.stdio;
import std.file : readText;
import std.string;
import std.conv : to;
import std.algorithm : canFind;

bool compare(int[2][] arr, int[2] compare){
    foreach(element ; arr){
        if(element == compare)
            return false;
    }
    return true;
}

void main(){
    string file = "data.txt";
    string fRead = readText(file);
    int counter = 1;
    int[2][] once;
    int[2] start = [0, 0];
    int[2] roboStart = [0, 0];
    once ~= start;

    foreach(ch ; fRead){
        if(counter%2==1){
            if(ch == '>')
                start[1] += 1;
            else if(ch == '<')
                start[1] -= 1;
            else if(ch == '^')
                start[0] += 1;
            else if(ch == 'v')
                start[0] -= 1;
            if(compare(once, start))
                once ~= start;
        }else{
            if(ch == '>')
                roboStart[1] += 1;
            else if(ch == '<')
                roboStart[1] -= 1;
            else if(ch == '^')
                roboStart[0] += 1;
            else if(ch == 'v')
                roboStart[0] -= 1;
            if(compare(once, roboStart))
                once ~= roboStart;
        }
        counter+=1;
    }
    writeln(once.length);
}