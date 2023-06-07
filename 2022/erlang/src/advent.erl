-module(advent).

-export([main/1]).

main(_Args) ->
    Problems = [
        {day1, "../test/data/day1_example.txt"},
        {day1, "../test/data/day1_input.txt"},
        {day2, "../test/data/day2_example.txt"},
        {day2, "../test/data/day2_input.txt"},
        {day3, "../test/data/day3_example.txt"},
        {day3, "../test/data/day3_input.txt"}
    ],
    run_problems(Problems),
    erlang:halt(0).

run_problems([{S,I}|R]) ->
    io:fwrite("~s ~s~n", [S:module_info(module), I]),
    S:solve(I),
    run_problems(R);
run_problems([]) ->
    ok.
