#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

#define MAXINT 2147483647

vector<int> readinput()
{
    vector<int> input;
    string filename = "input.txt";

    {
        ifstream file(filename, ios::in);
        int number;

        while ( file >> number )
            input.push_back(number);
    }

    return input;
}

void part1(vector<int>& input)
{
    int a = MAXINT;
    int r = 0;
    for(int b: input)
    {
        if(a < b)
            r++;
        a = b;
    }
    cout << r << endl;
}

void part2(vector<int>& input)
{
    int r = 0;
    int u = MAXINT;
    auto iter = input.begin();
    int a = *iter++;
    int b = *iter++;
    for(; iter < input.end(); iter++)
    {
        int c = *iter;
        int v = a+b+c;
        if(u < v)
            r++;
        a = b; b = c; u = v;
    }
    cout << r << endl;
}

int main()
{
    vector<int> input = readinput();
    part1(input);
    part2(input);

    return 0;
}
