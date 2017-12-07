-module(ch1).
-export([main/0]).

solve(L) ->
  solve([lists:nth(length(L), L) | L], L).

solve(_, []) ->
  0;
solve([H | Ta], [H | Tb]) ->
  H - $0 + solve(Ta, Tb);
solve([_ | Ta], [_ | Tb]) ->
  solve(Ta, Tb).

main() ->
  {ok, File} = file:read_file("input.txt"),
  Content = unicode:characters_to_list(File),
  {C, _} = lists:split(length(Content) -1, Content),
  main(C).

main(C) ->
  io:write(solve(C)).
