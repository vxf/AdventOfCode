-module(ch2).
-export([main/0, main/1]).

solve(Sheet) ->
  lists:sum([lists:max(L) - lists:min(L) || L <- Sheet]).
  
bin_to_integer(B) ->
  {I, _} = string:to_integer(binary:bin_to_list(B)),
  I.

main() ->
  {ok, Binary} = file:read_file("input.txt"),
  Sheet = [[bin_to_integer(Y) || Y <- binary:split(X, <<"\t">>,[global])] || X <- binary:split(Binary, <<"\n">>,[global]), X =/= <<>>],
  main(Sheet).

main(Sheet) ->
  solve(Sheet).
