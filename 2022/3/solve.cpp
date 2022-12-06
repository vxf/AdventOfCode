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

void part2(vector<string> input)
{
    int sum = 0;

    for (auto it = input.begin(); it < input.end(); it+=3)
    {
        auto a = *it;
        auto b = *(it+1);
        auto c = *(it+2);
        string i, j;
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        sort(c.begin(), c.end());
        set_intersection(a.begin(), a.end(),
                            b.begin(), b.end(),
                            back_inserter(i));
        set_intersection(i.begin(), i.end(),
                            c.begin(), c.end(),
                            back_inserter(j));
        sum += calc(j.back());
    }
    cout << sum << endl;
}

int main()
{
    vector<string> input = readinput();
    part1(input);
    part2(input);

    return 0;
}
