-module(advent).

-export([main/1]).

main(_Args) ->
    Solutions = [
        day1,
        day2,
        day3,
        day4,
        day5,
        day6
    ],
    run_problems(Solutions),
    erlang:halt(0).

run_problems([S|R]) ->
    ModuleName = atom_to_list(S:module_info(module)),

    ExampleFile = string:replace("../test/data/{}_example.txt", "{}", ModuleName),
    io:fwrite("~s ~s~n", [ModuleName, ExampleFile]),
    S:solve(ExampleFile),

    InputFile = string:replace("../test/data/{}_input.txt", "{}", ModuleName),
    io:fwrite("~s ~s~n", [ModuleName, InputFile]),
    S:solve(InputFile),

    run_problems(R);
run_problems([]) ->
    ok.
