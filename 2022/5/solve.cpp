#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <tuple>
using namespace std;

typedef vector<vector<char>> stack_format;
typedef vector<tuple<int, int, int>> move_format;
typedef tuple<stack_format, move_format> input_format;

void print_stacks(stack_format stacks)
{
    for (auto s: stacks)
    {
        for (auto e: s)
            cout << e << ' ';
         cout << endl;
    }
}

input_format readinput()
{
    input_format input;
    stack_format stacks;
    move_format moves;
    string filename = "input.txt";

    {
        ifstream file(filename, ios::in);
        string line;
        getline(file, line);
        int nstacks = (line.size() + 1) / 4;
        stacks.resize(nstacks);
        do
        {
            if (line.find('[') == string::npos)
                break;

            for (int i = 0; i < nstacks; i++)
            {
                char c = line[i*4+1];
                if (c != ' ')
                    stacks[i].push_back(c);
            }
        } while(getline(file, line));

        for (auto it = stacks.begin(); it != stacks.end(); it++)
            reverse(it->begin(), it->end());

        getline(file, line);

        while(getline(file, line))
        {
            int a, b, c;
            sscanf(line.c_str(), "move %u from %u to %u", &a, &b, &c);
            moves.push_back({a, b-1, c-1});
        }
    }

    return input_format({stacks, moves});
}

void part1(input_format& input)
{
    stack_format stacks;
    move_format moves;

    tie (stacks, moves) = input;

    // print_stacks(stacks);

    for (auto m: moves)
    {
        int n, s, d;
        tie (n, s, d) = m;

        for (auto it = stacks[s].end()-1; it >= stacks[s].end()-n; it--)
            stacks[d].push_back(*it);

        for (int i = 0; i < n; i++)
            stacks[s].pop_back();
    }

    // print_stacks(stacks);

    for (auto s: stacks)
        cout << s.back();
    cout << endl;
}

void part2(input_format& input)
{
    stack_format stacks;
    move_format moves;

    tie (stacks, moves) = input;

    // print_stacks(stacks);

    for (auto m: moves)
    {
        int n, s, d;
        tie (n, s, d) = m;

        for (auto it = stacks[s].end()-n; it < stacks[s].end(); it++)
            stacks[d].push_back(*it);

        for (int i = 0; i < n; i++)
            stacks[s].pop_back();
    }

    // print_stacks(stacks);

    for (auto s: stacks)
        cout << s.back();
    cout << endl;
}

int main()
{
    input_format input = readinput();
    part1(input);
    part2(input);

    return 0;
}
