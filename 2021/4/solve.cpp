// requires -std=c++2a

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <tuple>
#include <sstream>
#include <set>
using namespace std;

tuple<int, int> EMPTY = {-1,-1};
typedef vector<tuple<int,int>> board_t;

tuple<vector<int>, vector<board_t>> readinput()
{
    string filename = "input.txt";
    string line, snum;
    vector<int> numbers;
    vector<board_t> boards;
    tie(numbers, boards);

    {
        ifstream file(filename, ios::in);
        getline(file, line);
        stringstream ss(line);
        while(getline(ss, snum, ','))
            numbers.push_back(stoi(snum));

        while(getline(file, line))
        {
            board_t board(100, EMPTY);
            for(int l=0; l<5; l++)
            {
                for(int c=0; c<5; c++)
                {
                    int n;
                    file >> n;
                    board[n] = {l, c};
                }
            }
            boards.push_back(board);
        }
    }

    return tie(numbers, boards);
}

int score(vector<bool>& done, board_t& board, int n)
{
    int s = 0;
    for(int i=0;i<100;i++)
        if(!done[i] && board[i] != EMPTY)
            s += i;

    return s * n;
}

int main()
{
    auto [numbers, boards] = readinput();

    int bs = boards.size();
    vector<vector<vector<int>>> mark(bs, vector<vector<int>>(2, vector<int>(5, 0)));
    vector<bool> done(numbers.size(), false);
    vector<bool> wins(bs, false);
    int rank = 0;
    for(int n: numbers)
    {
        done[n] = true;
        for(int i=0; i<bs; i++)
        {
            if(wins[i])
                continue;
            board_t& b = boards[i];
            if(b[n] == EMPTY)
                continue;
            auto [l, c] = b[n];
            int x = ++mark[i][0][l];
            int y = ++mark[i][1][c];
            if(x == 5 || y == 5)
            {
                wins[i] = true;
                if(rank == 0 || rank == bs-1)
                    cout << score(done, b, n) << endl;
                rank++;
            }
        }
    }

    return 0;
}
