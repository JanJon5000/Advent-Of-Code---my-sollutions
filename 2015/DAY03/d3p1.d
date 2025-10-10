import std.stdio;
import std.file : readText;
import std.string;
import std.conv : to;
import std.algorithm : map, countUntil;
import std.range : array;

void main(){
    string file = "data.txt";
    string fRead = readText(file);
    int counter = 0;
    int[][2] once = new int[][2];
    int[2] start = {0, 0};
    foreach(ch ; fRead){
        if(ch == '>')
            start[1] += 1;
        else if(ch == '<')
            start[1] -= 1;
        else if(ch == '^')
            start[0] += 1;
        else if(ch == 'v')
            start[0] -= 1;
        if(countUntil(once.length, once.length, start) == -1)
            v ~= start;
        else
        
    }
    
}