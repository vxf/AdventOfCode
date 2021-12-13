// requires -std=c++17

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
using namespace std;

#define BITNUM 12

vector<bitset<BITNUM>> readinput()
{
    vector<bitset<BITNUM>> input;
    string filename = "input.txt";
    std::bitset<BITNUM> line;

    {
        ifstream file(filename, ios::in);
        while(file >> line)
            input.push_back(line);
    }

    return input;
}

void part1(vector<bitset<BITNUM>>& input)
{
    int t = input.size();
    vector<int> f = {0,0,0,0,0,0,0,0,0,0,0,0};
    std::bitset<BITNUM> gamma, epsilon;

    for(auto b: input)
        for(int i=0; i<BITNUM; i++)
            f[i] += b[i];

    for(int i=0; i<BITNUM; i++)
    {
        gamma[i] = f[i]*2 >= t;
        epsilon[i] = f[i]*2 <= t;
    }

    cout << gamma.to_ulong()*epsilon.to_ulong() << endl;
}

int oxco2(vector<bitset<BITNUM>>& input, vector<bool>& mask, int p)
{
    int f = 0, i = 0;
    for(auto b: input)
    {
        if(mask[i])
            f += b[p];
        i++;
    }

    return f;
}

int filter(vector<bitset<BITNUM>>& input, vector<bool>& mask, int p, bool fo)
{
    int t = 0, i = 0;
    for(auto b: input)
    {
        if(mask[i] && b[p]!=fo)
            mask[i] = false;
        if(!mask[i])
            t++;
        i++;
    }

    return input.size() - t;
}

int findlast(vector<bool>& mask)
{
    int i = 0;
    for(;!mask[i] && i<mask.size(); i++){}
    return i;
}

void part2(vector<bitset<BITNUM>>& input)
{
    int s = input.size();
    vector<bool> mask(s, true);
    int o_level;
    int c_level;

    int t = s;
    for(int p=BITNUM-1; t>1 && p>=0; p--)
    {
        int f = oxco2(input, mask, p);
        bool fo = f*2 >= t;

        t = filter(input, mask, p, fo);
    }
    o_level = input[findlast(mask)].to_ulong();

    mask = vector<bool>(s, true);
    t = s;
    for(int p=BITNUM-1; t>1 && p>=0; p--)
    {
        int f = oxco2(input, mask, p);
        bool fc = f*2 < t;

        t = filter(input, mask, p, fc);
    }
    c_level = input[findlast(mask)].to_ulong();

    cout << o_level*c_level << endl;
}

int main()
{
    vector<bitset<BITNUM>> input = readinput();
    part1(input);
    part2(input);

    return 0;
}
