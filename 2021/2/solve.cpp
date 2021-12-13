// requires -std=c++17

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <tuple>
#include <map>
using namespace std;

enum DIRECTION
{
    FORWARD,
    UP,
    DOWN
};

vector<tuple<int, int>> readinput()
{
    vector<tuple<int, int>> input;
    string filename = "input.txt";
    string dirstr;
    int d, x;
    map<string, int> m {
        {"forward", FORWARD},
        {"up", UP},
        {"down", DOWN},
    };

    {
        ifstream file(filename, ios::in);
        while(file >> dirstr >> x)
        {
            int d = m[dirstr];
            input.push_back(tuple<int, int>(d, x));
        }
    }

    return input;
}

void part1(vector<tuple<int, int>>& input)
{
    int u=0, v=0;
    for(auto [d, x]: input)
    {
        switch(d)
        {
            case FORWARD: u+=x; break;
            case UP: v-=x; break;
            case DOWN: v+=x; break;
        }
    }

    cout << u*v << endl;
}

void part2(vector<tuple<int, int>>& input)
{
    int u=0, v=0, aim=0;
    for(auto [d, x]: input)
    {
        switch(d)
        {
            case FORWARD: u+=x; v+=aim*x; break;
            case UP: aim-=x; break;
            case DOWN: aim+=x; break;
        }
    }

    cout << u*v << endl;
}

int main()
{
    vector<tuple<int, int>> input = readinput();
    part1(input);
    part2(input);

    return 0;
}
