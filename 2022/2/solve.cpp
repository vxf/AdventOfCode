#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>
#include <map>
#include <tuple>
using namespace std;

enum PLAY {
    ROCK,
    PAPER,
    SCISOR,
};
enum OUTCOME {
    LOSE,
    DRAW,
    WIN,
};
map<char, int> PLAY_MAP = {
    {'A', ROCK},
    {'B', PAPER},
    {'C', SCISOR},
    {'X', LOSE},
    {'Y', DRAW},
    {'Z', WIN},
};
int SCORE[] = { 1, 2, 3, 1, 2, 3 };

vector<tuple<int, int>> readinput()
{
    vector<tuple<int, int>> input;
    string filename = "input.txt";
    char o, r;

    {
        ifstream file(filename, ios::in);
        while (file >> o >> r)
        {
            input.push_back({
                PLAY_MAP[o],
                PLAY_MAP[r]}
            );
        }
    }

    return input;
}

int score(int o, int r)
{
    int s = 0;
    
    if (o == r)
        s = 3;
    else if (((o + 1) % 3) == r)
        s = 6;

    return SCORE[r] + s;
}

void part12(vector<tuple<int, int>> input)
{
    int o, r;
    int total1 = 0;
    int total2 = 0;

    for(auto round: input)
    {
        tie (o, r) = round;
        total1 += score(o, r);
        r = (o + 3 + (r - 1)) % 3;
        total2 += score(o, r);
    }
    cout << total1 << endl;
    cout << total2 << endl;
}

int main()
{
    vector<tuple<int, int>> input = readinput();
    part12(input);

    return 0;
}
