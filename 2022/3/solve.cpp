#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> readinput()
{
    vector<string> input;
    string filename = "input.txt";
    char o, r;

    {
        ifstream file(filename, ios::in);
        string line;
        while(file >> line)
            input.push_back(line);
    }

    return input;
}

int calc(char c)
{
    if (c >= 'a')
        return c - 'a' + 1;
    else
        return c - 'A' + 27;
}

void part1(vector<string> input)
{
    int sum = 0;
    for (auto s: input)
    {
        int l = s.size() / 2;
        string i;
    
        sort(s.begin(), s.begin()+l);
        sort(s.begin()+l, s.end());
        set_intersection(s.begin(), s.begin()+l,
                            s.begin()+l, s.end(),
                            back_inserter(i));

        sum += calc(i.back());
    }
    cout << sum << endl;
}

int main()
{
    vector<string> input = readinput();
    part1(input);

    return 0;
}
