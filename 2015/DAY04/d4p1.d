import std.stdio;
import std.string;
import std.digest.md;
import std.conv;

void main(){
    string compare = "00000";
    string key = "yzbqklnj";
    int counter = 0;
    while(toHexString(md5Of(key ~ to!string(counter)))[0..5] != compare){
        counter++;
    }
    writeln(counter);
}