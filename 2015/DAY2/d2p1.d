import std.stdio;
import std.file : readText;
import std.string;
import std.conv : to;
import std.algorithm : map;
import std.range : array;

int area(int l, int w, int h){
    int ans = 2*l*w + 2*w*h + 2*h*l;
    if( h*l <= l*w && h*l <= h*w)
        ans += h*l;
    else if(l*w <= h*w && l*w <= h*l)
        ans += l*w;
    else
        ans += h*w;    
    return ans;
}

void main(){
    auto file = File("data.txt");
    int sum = 0;

    foreach(line ; file.byLine) {
        auto values = line.split("x");
        values[2] = values[2].chomp;
        writeln(values);
        int[] values2 = values.map!(p => to!int(p)).array;
        int partSum = area(values2[0], values2[1], values2[2]);
        writefln("%d, %d, %d = %d\n", values2[0], values2[1], values2[2], partSum);
        sum += partSum;
    }
    writeln(sum);
}