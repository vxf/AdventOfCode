-module(day5).

-export([solve/1]).
-export([part1/1]).
-export([part2/1]).

solve(InputFile) ->
    Input = parse(advent_file:readlines(InputFile)),
    part1(Input).
    % part2(Input).

part1({Piles, Moves}) ->
    X = [H || [H|_] <- rearrange(Piles, Moves, fun lists:reverse/2)],
    io:fwrite("~s~n", [X]).

part2({Piles, Moves}) ->
    X = [H || [H|_] <- rearrange(Piles, Moves, fun lists:append/2)],
    io:fwrite("~s~n", [X]).

parse(L) ->
    {P, M, Size} = parse_split(L, []),
    Piles = parse_piles(P, lists:duplicate(Size, [])),
    Moves = parse_moves(M),
    {Piles, Moves}.

parse_split([""|M], [I|P]) ->
    {P, M, (length(I)+1) div 4};
parse_split([L|T], P) ->
    parse_split(T, [L|P]).

parse_piles([], Q) ->
    Q;
parse_piles([[_|L]|T], Q) ->
    M = parse_pile_line(L, Q),
    % io:fwrite("1:: ~s~n", [M]),
    parse_piles(T, M).

parse_pile_line([$\s|_], [B|[]]) ->
    [B];
parse_pile_line([A|_], [B|[]]) ->
    [[A|B]];
parse_pile_line([$\s|T], [B|U]) ->
    {_, V} = lists:split(3, T),
    [B | parse_pile_line(V, U)];
parse_pile_line([A|T], [B|U]) ->
    {_, V} = lists:split(3, T),
    [[A|B] | parse_pile_line(V, U)].

parse_moves([]) ->
    [];
parse_moves([H|T]) ->
    [_, Moves, _, From, _, To] = string:lexemes(H, " "),
    [{
        list_to_integer(Moves),
        list_to_integer(From),
        list_to_integer(To)
    }|parse_moves(T)].

rearrange(Piles, [], _) ->
    Piles;
rearrange(Piles, [{N,F,T}|Moves], Put) ->
    {S, P} = pile_take(Piles, N, F),
    rearrange(pile_put(P, S, T, Put), Moves, Put).

pile_take([], _, _) ->
    [];
pile_take([P|Piles], N, 1) ->
    {A, B} = lists:split(N, P),
    {A, [B|pile_take(Piles, N, 0)]};
pile_take([P|Piles], N, F) when F > 1 ->
    {S, Q} = pile_take(Piles, N, F-1),
    {S, [P|Q]};
pile_take([P|Piles], N, F) ->
    [P|pile_take(Piles, N, F-1)].

pile_put([P|Piles], S, 1, Put) ->
    [Put(S,P)|Piles];
pile_put([P|Piles], S, F, Put)  ->
    [P|pile_put(Piles, S, F-1, Put)].
