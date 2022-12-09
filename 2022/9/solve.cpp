#include <iostream>
#include <fstream>
#include <vector>
#include <tuple>
#include <set>
using namespace std;

typedef vector<tuple<char, int>> input_format;
typedef tuple<int, int> knot;

void readinput(string& filename, input_format& input)
{
    {
        ifstream file(filename, ios::in);
        char d;
        int s;

        while(file >> d >> s)
            input.push_back({d, s});
    }
}

void head(knot& h, int d)
{
    int hx, hy;
    tie (hx, hy) = h;
    switch (d)
    {
        case 'L':
        hx--;
        break;
        case 'R':
        hx++;
        break;
        case 'U':
        hy++;
        break;
        case 'D':
        hy--;
        break;
    }
    h = {hx, hy};
}

void tail(knot& t, knot& h)
{
    int tx, ty, hx, hy;
    tie (tx, ty) = t;
    tie (hx, hy) = h;
    int dx = hx - tx;
    int dy = hy - ty;

    if (abs(dx*dy) == 2)
    {
        dx *= 2;
        dy *= 2;
    }

    if (dx > 1 )
        tx++;
    else if (dx < -1 )
        tx--;
 
    if (dy > 1 )
        ty++;
    else if (dy < -1 )
        ty--;

    t = {tx, ty};
}

void sim(input_format& input, int nknots)
{
    set<tuple<int, int>> visited;
    vector<knot> knots(nknots, {0, 0});

    for (auto m: input)
    {
        int d, s;
        tie (d, s) = m;
        for (int i = 0; i < s; i++)
        {
            head(knots[0], d);
            // cout << "H: " << get<0>(knots[0]) << "," << get<1>(knots[0]) << endl;
            for (int i = 0; i < nknots - 1; i++)
                tail(knots[i+1], knots[i]);
            visited.insert(knots.back());
        }
    }

    // for (auto v: visited)
    // {
    //     int x, y;
    //     tie (x, y) = v;
    //     cout << "V: " << x << "," << y << endl;
    // }

    cout << visited.size() << endl;
}

void part1(input_format& input)
{
    sim(input, 2);
}

void part2(input_format& input)
{
    sim(input, 10);
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
