import std.stdio;
import std.file;
import std.string;
import core.stdc.string : strlen;
import std.conv;

bool isNice(char[] s){
    bool betweenThem = false;
    bool ddletter = false;
    writeln(s);
    if(column(s) < 4)
        return false;
    for(int i=1;i<column(s)-1;i++){
        writeln(s[i-1], " ", s[i+1]);
        if(s[i-1] == s[i+1]){
            betweenThem = true;
            break;
        }
    }
    for(int i=0;i<column(s)-1;i++){
        for(int j=i+2;j<column(s)-1;j++){
            writeln(s[i..i+2], " ", s[j..j+2]);
            if(s[i..i+2] == s[j..j+2] && i != j && i != j-1){
                ddletter = true;
            }
        }
    }
    writeln("podwojna litera: ", ddletter, " pomiedzy: ", betweenThem);
    return ddletter && betweenThem;
}

void main(){
    auto file = File("data.txt");
    int sum = 0;
    foreach(line ; file.byLine())
        sum += (isNice(line.chomp));
    writeln(sum);
}