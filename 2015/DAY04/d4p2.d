import std.stdio;
import std.string;
import std.digest.md;
import std.conv;

void main(){
    string compare = "000000";
    string key = "yzbqklnj";
    int counter = 0;
    while(toHexString(md5Of(key ~ to!string(counter)))[0..6] != compare){
        counter++;
    }
    writeln(counter);
}