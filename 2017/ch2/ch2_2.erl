-module(ch2_2).
-export([main/0, main/1]).

%% find_div(L) ->
%%   [H | T] = lists:sort(fun(A, B) -> B < A end, L),
%%   find_div([H | T], T).
 
%% find_div([_ | [H | T]], []) ->
%%   find_div([H | T], T);
%% find_div([Ha | _], [Hb | _]) when (Ha rem Hb) =:= 0 ->
%%   Ha div Hb;
%% find_div([Ha | Ta], [_ | Tb]) ->
%%   find_div([Ha | Ta], Tb).

find_div(L) ->
  [D] = [A div B || A <- L, B <- L, A > B, (A rem B) =:= 0],
  D.

solve(Sheet) ->
  lists:sum([find_div(L) || L <- Sheet]).
  
bin_to_integer(B) ->
  {I, _} = string:to_integer(binary:bin_to_list(B)),
  I.

main() ->
  {ok, Binary} = file:read_file("input.txt"),
  Sheet = [[bin_to_integer(Y) || Y <- binary:split(X, <<"\t">>,[global])] || X <- binary:split(Binary, <<"\n">>,[global]), X =/= <<>>],
  main(Sheet).

main(Sheet) ->
  solve(Sheet).
