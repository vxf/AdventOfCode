-module(day1).

-export([solve/1]).
-export([part1/1]).
-export([part2/1]).

solve(InputFile) ->
    Input = all_calories(advent_file:readlines(InputFile)),
    part1(Input),
    part2(Input).

part1(Input) ->
    X = lists:max(lists:map(fun lists:sum/1, Input)),
    io:fwrite("~w~n", [X]).

part2(Input) ->
    X = lists:sum(top(lists:map(fun lists:sum/1, Input), 3)),
    io:fwrite("~w~n", [X]).

top(L, N) ->
    lists:sublist(lists:reverse(lists:sort(L)), N).

all_calories([]) ->
    [];
all_calories(R) ->
    {L, S} = group_calories(R),
    [L | all_calories(S)].
    
group_calories([]) ->
    {[], []};
group_calories([""|S]) ->
    {[], S};
group_calories([C|R]) ->
    {I, _} = string:to_integer(C),
    {L, S} = group_calories(R),
    {[I | L], S}.
