-module(day2).

-export([solve/1]).
-export([part1/1]).
-export([part2/1]).

solve(InputFile) ->
    Input = lists:map(fun parse_line/1, advent_file:readlines(InputFile)),
    part1(Input),
    part2(Input).

part1(Input) ->
    X = lists:sum(lists:map(fun score/1, Input)),
    io:fwrite("~w~n", [X]).

part2(Input) ->
    X = lists:sum(lists:map(fun(P) -> score(next_play(P)) end, Input)),
    io:fwrite("~w~n", [X]).

parse_line(L) ->
    [[A], [B]] = string:lexemes(L, " "),
    {A-$A, B-$X}.

score({A, B}) ->
    B + 1 + ((B - A + 4) rem 3) * 3.

next_play({A, B}) ->
    {A, (A + B - 1 + 3) rem 3}.
