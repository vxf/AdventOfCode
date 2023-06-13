-module(day4).

-export([solve/1]).
-export([part1/1]).
-export([part2/1]).

solve(InputFile) ->
    Input = [sort(parse(I)) || I <- advent_file:readlines(InputFile)],
    part1(Input),
    part2(Input).

part1(Input) ->
    X = lists:sum([1 || A <- Input, fully_contains(A)]),
    io:fwrite("~w~n", [X]).

part2(Input) ->
    X = lists:sum([1 || A <- Input, overlaps(A)]),
    io:fwrite("~w~n", [X]).

parse(L) ->
    [[list_to_integer(I) || I <- string:split(X, "-")] || X <- string:split(L, ",")].

sort([[A, B], [C, D]]) when A > C; (A == C) and (D > B) ->
    [[C, D], [A, B]];
sort(L) ->
    L.

fully_contains([[_A, B], [_C, D]]) ->
    D =< B.

overlaps([[_A, B], [C, _D]]) ->
    B >= C.
