#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <tuple>
using namespace std;

typedef string input_format;

string readinput()
{
    input_format input;
    string filename = "input.txt";

    {
        ifstream file(filename, ios::in);
        file >> input;
    }

    return input;
}

int marker(string& input, int msize)
{
    vector<char> buf;
    buf.resize(msize);
    for (int i = 0; i < msize; i++)
        buf[i] = '!';

    int i = 0;
    for (auto c: input)
    {
        buf[i % msize] = c;
        i++;
        if (i < msize)
            continue;
        vector<char> buf2 = buf;
        sort(buf2.begin(), buf2.end());
        if(adjacent_find(buf2.begin(), buf2.end()) == buf2.end())
            break;
    }

    return i;
}

void part1(string& input)
{
    cout << marker(input, 4) << endl;
}

void part2(string& input)
{
    cout << marker(input, 14) << endl;
}

int main()
{
    string input = readinput();
    part1(input);
    part2(input);

    return 0;
}
