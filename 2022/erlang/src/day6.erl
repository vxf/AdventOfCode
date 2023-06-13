-module(day6).

-export([solve/1]).
-export([part1/1]).
-export([part2/1]).

solve(InputFile) ->
    [Input] = advent_file:readlines(InputFile),
    part1(Input),
    part2(Input).

part1(Input) ->
    X = find_marker(Input, 4),
    io:fwrite("~w~n", [X]).

part2(Input) ->
    X = find_marker(Input, 14),
    io:fwrite("~w~n", [X]).

find_marker(B, N) ->
    {H, T} = lists:split(N, B),
    find_marker(queue:from_list(H), T, N, N).
find_marker(Q, [C|B], M, N) ->
    case length(lists:usort(queue:to_list((Q)))) of
        N ->
            M;
        _Else ->
            {_, R} = queue:out(queue:in(C, Q)),
            find_marker(R, B, M+1, N)
    end.
