-module(ch3).
-export([main/0, main/1]).

solve(N) ->
  B = trunc((math:sqrt(N)-1)/2),
  A = 2*B + 1,
  M = 2 * (B + 1),
  B + 1 + abs((N - (A*A)) rem M - (B+1)).

main() ->
  main(368078).

main(N) ->
  io:write(solve(N)).
