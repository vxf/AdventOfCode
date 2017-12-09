-module(ch5_2).
-export([main/0, main/1]).

solve(Sheet) ->
  solve(array:from_list(Sheet), 0, 0, length(Sheet)).

solve(P, PC, C, S) when PC >= 0, PC < S ->
  I = array:get(PC, P),
  Q = array:set(PC, case I < 3 of false -> I - 1; true -> I + 1 end, P),
  solve(Q, PC + I, C + 1, S);
solve(_, _, C, _) ->
  C.
  
bin_to_integer(B) ->
  {I, _} = string:to_integer(binary:bin_to_list(B)),
  I.

main() ->
  {ok, Binary} = file:read_file("input.txt"),
  Sheet = [bin_to_integer(X) || X <- binary:split(Binary, <<"\n">>,[global]), X =/= <<>>],
  main(Sheet).

main(Sheet) ->
  solve(Sheet).
