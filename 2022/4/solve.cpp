#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <tuple>
using namespace std;

typedef vector<tuple<int, int, int, int>> input_format;

input_format readinput()
{
    input_format input;
    string filename = "input.txt";
    char o, r;

    {
        ifstream file(filename, ios::in);
        string line;
        int a, b, c, d;
        while(file >> line)
        {
            sscanf(line.c_str(), "%u-%u,%u-%u", &a, &b, &c, &d);
            input.push_back({a, b, c, d});
        }
    }

    return input;
}

void part1(input_format input)
{
    int p = 0;
    for (auto l: input)
    {
        int a, b, c, d;
        tie (a, b, c, d) = l;

        if (a <= c && b >= d ||  c <= a && d >= b)
            p++;
    }

    cout << p << endl;
}

void part2(input_format input)
{
    int p = 0;
    for (auto l: input)
    {
        int a, b, c, d;
        tie (a, b, c, d) = l;

        if (a < c)
        {
            swap(a, c);
            swap(b, d);
        }

        if (a <= d)
            p++;
    }

    cout << p << endl;
}

int main()
{
    input_format input = readinput();
    part1(input);
    part2(input);

    return 0;
}
