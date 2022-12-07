#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <tuple>
using namespace std;

#define MAXINT 2147483647
#define DISK 70000000
#define UPDATE 30000000

typedef vector<string> input_format;

class Dir
{
public:
    Dir() : Dir("") {}
    Dir(string name) : _name(name), _size(-1) {}

    void subdir(string& name)
    {
        _subdirs.push_back(Dir(name));
    }

    void file(int size, string& file)
    {
        _files.push_back({size, file});
    }

    Dir* get_dir(string& name)
    {
        for (Dir& d: _subdirs)
            if (d._name == name)
                return &d;
        return nullptr;
    }

    int size()
    {
        if (_size != -1)
            return _size;
 
        int total = 0;
        for (auto f: _files)
            total += get<0>(f);
        for (auto d: _subdirs)
            total += d.size();
        
        _size = total;
        return total;
    }

    vector<Dir> _subdirs;
    vector<tuple<int, string>> _files;
    string _name;
    int _size;
};

void readinput(string& filename, input_format& input)
{
    {
        ifstream file(filename, ios::in);
        string word;

        while(file >> word)
            input.push_back(word);
    }
}

void print_path(vector<Dir*>& path)
{
    for (auto p: path)
        cout << "/" << p->_name;
    cout << endl;
}

void print_tree(Dir* tree, int level)
{
    string tab = "";
    if (level == 0)
        cout << "------------" << endl;
    for (int i = 0; i < level; i++)
        tab.push_back(' ');
    cout << tab << tree->_name << " - " << tree->size() << endl;
    for (auto f: tree->_files)
        cout << tab << get<1>(f) << " " << get<0>(f) << endl;
    for (auto d: tree->_subdirs)
        print_tree(&d, level + 1);
    if (level == 0)
        cout << "------------" << endl;
}

void run_commands(Dir& tree, input_format& input)
{
    vector<Dir*> path;

    for (auto it = input.begin(); it < input.end();)
    {
        if (*it == "$") {
            it++;
            if (*it == "cd") {
                it++;
                if (*it == "..") {
                    path.pop_back();
                }
                else if (*it == "/") {
                    path.clear();
                    path.push_back(&tree);
                }
                else {
                    path.push_back(path.back()->get_dir(*it));
                }
            }
        }
        else { // ls
            if (*it == "dir") {
                it++;
                path.back()->subdir(*it);
            }
            else { // file
                int s = stoi(*it++);
                path.back()->file(s, *it);
            }
        }
        it++;
    }
}

int part1_aux(Dir& dir)
{
    int total = 0;
    int s = dir.size();
    if (s <= 100000)
        total += s;

    for (auto p: dir._subdirs)
        total += part1_aux(p);
    
    return total;
}

void part1(Dir& tree)
{
    cout << part1_aux(tree) << endl;
    // print_tree(&tree, 0);
}

int part2_aux(Dir& dir, int release)
{
    int s = dir.size();
    int min = (s >= release) ? s : MAXINT;

    for (auto p: dir._subdirs)
    {
        s = part2_aux(p, release);
        if (s < min)
            min = s;
    }
    
    return min;
}

void part2(Dir& tree)
{
    int release = UPDATE - DISK + tree.size();

    cout << part2_aux(tree, release) << endl;
}

int main(int argc, char* argv[])
{
    input_format input;
    Dir tree;
    string filename = "input.txt";
    if (argc > 1)
        filename = argv[1];

    readinput(filename, input);
    run_commands(tree, input);
    part1(tree);
    part2(tree);

    return 0;
}
