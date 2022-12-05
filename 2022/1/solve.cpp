#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

#define SUM(v) accumulate(v.begin(), v.end(), 0)

vector<vector<int>> readinput()
{
    vector<vector<int>> input;
    string filename = "input.txt";

    {
        ifstream file(filename, ios::in);
        string line = "";
        vector<int>* g;

        do
        {
            if (line == "")
            {
                input.push_back(vector<int>());
                g = &input.back();
            }
            else
            {
                g->push_back(stoi(line));
            }
        }
        while (getline(file, line));
    }

    return input;
}

void part12(vector<vector<int>>& input)
{
    int top[] = {0, 0, 0, 0}; 
    for(vector<int>& v: input)
    {
        top[0] = SUM(v);
        for (int i = 0; i < 3 && top[i] > top[i+1]; i++)
            swap(top[i], top[i+1]);
    }
    cout << top[3] << endl;
    cout << (top[1]+top[2]+top[3]) << endl;
}

int main()
{
    vector<vector<int>> input = readinput();
    part12(input);

    return 0;
}
