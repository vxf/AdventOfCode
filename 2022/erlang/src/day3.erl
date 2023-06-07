-module(day3).

-export([solve/1]).
-export([part1/1]).
-export([part2/1]).

solve(InputFile) ->
    Input = advent_file:readlines(InputFile),
    part1(Input),
    part2(Input).

part1(Input) ->
    X = lists:sum(lists:map(fun score_intersect/1, lists:map(fun rucksack_split/1, Input))),
    io:fwrite("~w~n", [X]).

part2(Input) ->
    X = lists:sum(lists:map(fun score_intersect/1, group(3, Input))),
    io:fwrite("~w~n", [X]).

rucksack_split(Line) ->
    tuple_to_list(lists:split(string:length(Line) div 2, Line)).

score_intersect(I) ->
    score(set_first(sets:intersection(lists:map(fun sets:from_list/1, I)))).

set_first(Set) ->
    lists:last(sets:to_list(Set)).

group(N, []) ->
    [];
group(N, List) ->
    {H, T} = lists:split(N, List),
    [H | group(N, T)].

score(C) when C < $a ->
    C - $A + 27;
score(C) ->
    C - $a + 1.
