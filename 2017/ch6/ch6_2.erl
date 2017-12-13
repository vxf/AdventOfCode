-module(ch6_2).
-export([main/0, main/1]).

dist(M) ->
  {P, Max} = maxp(M),
  dist(M, P, Max, length(M), 0). 

dist([], _, _, _, _) ->
  [];
dist([_ | T], P, Max, L, C) when C == P ->
  [        (Max div L) | dist(T, P, Max, L, C+1)];
dist([H | T], P, Max, L, C) when C < P, C + L =< P + (Max rem L) ->
  [H + 1 + (Max div L) | dist(T, P, Max, L, C+1)];
dist([H | T], P, Max, L, C) when C > P, C =< P + (Max rem L) ->
  [H + 1 + (Max div L) | dist(T, P, Max, L, C+1)];
dist([H | T], P, Max, L, C) ->
  [H +     (Max div L) | dist(T, P, Max, L, C+1)].

solve(M) ->
  solve([M], {-1, false}).

solve(_, {P, true}) ->
  P + 1;
solve([M | T], {_, false}) ->
  N = dist(M),
  % io:write(N),
  % io:fwrite("~n"),
  solve([N | [M | T]], index(N, [M | T])).

index(E, L) ->
  index(E, L, 0).
index(_, [], _) ->
  {-1, false};
index(E, [E | _], C) ->
  {C, true};
index(E, [_ | T], C) ->
  index(E, T, C+1).

%% max function that also returns the position on the list, 0-based
maxp(M) ->
  maxp(M, 0, -1, -1).
maxp([], _, P, N) ->
  {P, N};
maxp([H | T], C, _, N) when H > N ->
  maxp(T, C+1, C, H);
maxp([_ | T], C, P, N) ->
  maxp(T, C+1, P, N).

%% translates a binary ascii number into integer
bin_to_integer(B) ->
  {I, _} = string:to_integer(binary:bin_to_list(B)),
  I.

main() ->
  % solve([0,2,7,0]).
  % solve([11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]).
  % dist([11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]).
  %dist([1,0,2,12,5,4,10,10,9,9,6,6,12,6,4,15]).
  {ok, Binary} = file:read_file("input.txt"),
  Sheet = [bin_to_integer(X) || X <- binary:split(Binary, <<"\t">>,[global]), X =/= <<>>],
  main(Sheet).

main(Sheet) ->
  solve(Sheet).
