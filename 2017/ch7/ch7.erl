-module(ch7).
-export([main/0, main/1]).

build([]) ->
  {sets:new(), sets:new()};
build([H | T]) when length(H) =< 2 ->
  build(T);
build([H | T]) ->
  {A, B} = build(T),
  {
    sets:add_element(lists:nth(1, H), A),
    sets:union(sets:from_list(lists:nthtail(3, H)), B)
  }.

solve(Sheet) ->
  {A, B} = build(Sheet),
  sets:fold(fun (C, _) -> C end, 0, sets:subtract(A, B)).  

main() ->
  {ok, Binary} = file:read_file("input.txt"),
  Sheet = [[string:strip(binary_to_list(Y), right, 44) || Y <- binary:split(X, <<" ">>,[global])] || X <- binary:split(Binary, <<"\n">>,[global]), X =/= <<>>],
  main(Sheet).

main(Sheet) ->
  io:fwrite(solve(Sheet)).
