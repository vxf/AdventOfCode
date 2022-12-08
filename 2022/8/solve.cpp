#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>
#include <tuple>
using namespace std;

#define MAXINT 2147483647

#define SUM(v) accumulate(v.begin(), v.end(), 0)

typedef vector<vector<uint8_t>> input_format;

void readinput(string& filename, input_format& input)
{
    {
        ifstream file(filename, ios::in);
        string line;

        while(file >> line)
        {
            input.emplace_back();
            vector<uint8_t>& v = input.back();
            for (auto c: line)
                v.push_back(c - '0');
        }
    }
}

void part1(input_format& input)
{
    int h = input.size();
    int w = input[0].size();
    // cout << w << "x" << h << endl;
    vector<vector<bool>> visible(h, vector<bool>(w, false));

    for (int y = 0; y < h; y++)
    {
        int v = -1;
        for (int x = 0; x < w-1; x++)
        {
            uint8_t t = input[y][x];
            if (t > v) {
                v = t;
                visible[y][x] = true;
            }
        }
    }

    for (int y = 0; y < h; y++)
    {
        int v = -1;
        for (int x = w - 1; x >= 1; x--)
        {
            uint8_t t = input[y][x];
            if (t > v) {
                v = t;
                visible[y][x] = true;
            }
        }
    }

    for (int x = 0; x < w; x++)
    {
        int v = -1;
        for (int y = 0; y < h-1; y++)
        {
            uint8_t t = input[y][x];
            if (t > v) {
                v = t;
                visible[y][x] = true;
            }
        }
    }

    for (int x = 0; x < w; x++)
    {
        int v = -1;
        for (int y = h - 1; y >= 1; y--)
        {
            uint8_t t = input[y][x];
            if (t > v) {
                v = t;
                visible[y][x] = true;
            }
        }
    }

    int s = 0;
    for (auto l: visible)
        s += SUM(l);

    // for (auto l: visible)
    // {
    //     for (auto t: l)
    //         cout << t;
    //     cout << endl;
    // }

    cout << s << endl;
}

void part2(input_format& input)
{
    int w = input.size();
    vector<vector<int>> visible = vector<vector<int>>(w, vector<int>(w, 1));
    //vector<vector<int>> visibleR;
    //visibleR = vector<vector<int>>(w, vector<int>(w, 0));

    for (int y = 0; y < w; y++)
    {
        int v = -1;
        vector<int> visibleR = vector<int>(w, 0);
        for (int x = 0; x < w-1; x++)
        {
            int t = input[y][x];
            int t2 = -1;
            int min = -1;
            for (int x2 = x+1, d = 1; x2 < w; x2++, d++)
            {
                t2 = input[y][x2];
                int v = visibleR[x2];
                if (t2 > min) {
                    min = t2;
                    if (d > v)
                        visibleR[x2] = d;
                }
            }
        }

        for (int x = 0; x < w; x++)
            visible[y][x] *= visibleR[x];
    }

    for (int y = 0; y < w; y++)
    {
        int v = -1;
        vector<int> visibleR = vector<int>(w, 0);
        for (int x = w - 1; x >= 1; x--)
        {
            int t = input[y][x];
            int t2 = -1;
            int min = -1;
            for (int x2 = x-1, d = 1; x2 >= 0; x2--, d++)
            {
                t2 = input[y][x2];
                int v = visibleR[x2];
                if (t2 > min) {
                    min = t2;
                    if (d > v)
                        visibleR[x2] = d;
                }
            }
        }

        for (int x = 0; x < w; x++)
            visible[y][x] *= visibleR[x];
    }

    for (int x = 0; x < w; x++)
    {
        int v = -1;
        vector<int> visibleR = vector<int>(w, 0);
        for (int y = 0; y < w-1; y++)
        {
            int t = input[y][x];
            int t2 = -1;
            int min = -1;
            for (int y2 = y+1, d = 1; y2 < w; y2++, d++)
            {
                t2 = input[y2][x];
                int v = visibleR[y2];
                if (t2 > min) {
                    min = t2;
                    if (d > v)
                        visibleR[y2] = d;
                }
            }
        }

        for (int y = 0; y < w; y++)
            visible[y][x] *= visibleR[y];
    }

    for (int x = 0; x < w; x++)
    {
        int v = -1;
        vector<int> visibleR = vector<int>(w, 0);
        for (int y = w - 1; y >= 1; y--)
        {
            int t = input[y][x];
            int t2 = -1;
            int min = -1;
            for (int y2 = y-1, d = 1; y2 >= 0; y2--, d++)
            {
                t2 = input[y2][x];
                int v = visibleR[y2];
                if (t2 > min) {
                    min = t2;
                    if (d > v)
                        visibleR[y2] = d;
                }
            }
        }

        for (int y = 0; y < w; y++)
            visible[y][x] *= visibleR[y];
    }

    int ideal = -1;
    for (auto l: visible)
        for (auto t: l)
            if (t > ideal)
                ideal = t;
    cout << ideal << endl;

    // for (auto l: visible)
    // {
    //     for (auto t: l)
    //         cout << t;
    //     cout << endl;
    // }
}


int main(int argc, char* argv[])
{
    input_format input;
    string filename = "input.txt";
    if (argc > 1)
        filename = argv[1];

    readinput(filename, input);
    part1(input);
    part2(input);

    return 0;
}
