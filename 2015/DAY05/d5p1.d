import std.stdio;
import std.file;
import std.string;
import core.stdc.string : strlen;
import std.conv;

bool isNice(char[] s){
    bool forbidden = true;
    bool doubleLetter = false;
    bool vowels3 = false;
    int counter = 0;
    char before = '0';
    writeln(s);
    for(int i=0;i<column(s);i++){
        write(to!string(before) ~ to!string(s[i]) ~ " ");
        if(before == s[i])
            doubleLetter = true;  
        if(to!string(before) ~ to!string(s[i]) == "ab" || to!string(before) ~ to!string(s[i]) == "cd" || to!string(before) ~ to!string(s[i]) == "pq" || to!string(before) ~ to!string(s[i]) == "xy")
            forbidden = false;    
        before = s[i];
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
            counter+=1;
        if(counter >= 3)
            vowels3 = true;   
    }
    writeln(s, " ", forbidden, " ", doubleLetter, " ", vowels3);
    return (forbidden && doubleLetter && vowels3);
}

void main(){
    auto file = File("data.txt");
    int sum = 0;
    foreach(line ; file.byLine())
        sum += (isNice(line.chomp));
    writeln(sum);
}