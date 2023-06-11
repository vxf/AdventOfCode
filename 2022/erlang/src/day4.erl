-module(day4).

-export([solve/1]).
-export([part1/1]).
-export([part2/1]).

solve(InputFile) ->
    Input = lists:map(fun(I) -> sort(parse(I)) end, advent_file:readlines(InputFile)),
    part1(Input),
    part2(Input).

part1(Input) ->
    X = lists:map(fun fully_contains/1, Input),
    Y = length(lists:filter(fun(A) -> A end, X)),
    io:fwrite("~w~n", [Y]).

part2(Input) ->
    X = lists:map(fun overlaps/1, Input),
    Y = length(lists:filter(fun(A) -> A end, X)),
    io:fwrite("~w~n", [Y]).

parse(L) ->
    lists:map(fun(X) ->
        lists:map(fun list_to_integer/1, string:split(X, "-"))
    end, string:split(L, ",")).

sort([[A, B], [C, D]]) when A > C; (A == C) and (D > B) ->
    [[C, D], [A, B]];
sort(L) ->
    L.

fully_contains([[_A, B], [_C, D]]) ->
    D =< B.

overlaps([[_A, B], [C, _D]]) ->
    B >= C.
