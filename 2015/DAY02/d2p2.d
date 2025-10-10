import std.stdio;
import std.file : readText;
import std.string;
import std.conv : to;
import std.algorithm : map;
import std.range : array;

int area(int l, int w, int h){
    int ans = l*w*h;
    if((l <= w && w <= h) || (w <= l && l <= h))
        ans += 2*l + 2*w;
    else if((l <= h && h <= w) || (h <= l && l <= w))
        ans += 2*l + 2*h;
    else
        ans += 2*w + 2*h;
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