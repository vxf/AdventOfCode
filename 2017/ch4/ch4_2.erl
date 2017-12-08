-module(ch4_2).
-export([main/0, main/1]).

solveLine(_, true) ->
  0;
solveLine([], false) ->
  1;
solveLine([H | T], false) ->
  solveLine(T, lists:member(H,T)).

solve(Sheet) ->
  lists:sum([solveLine([lists:sort(W) || W <- L], false) || L <- Sheet]).  

main() ->
  {ok, Binary} = file:read_file("input.txt"),
  Sheet = [[unicode:characters_to_list(Y) || Y <- binary:split(X, <<" ">>,[global])]
    || X <- binary:split(Binary, <<"\n">>,[global]), X =/= <<>>],
  main(Sheet).

main(Sheet) ->
  solve(Sheet).
