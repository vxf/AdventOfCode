-module(advent_file).

-export([readlines/1]).

readlines(FileName) ->
    {ok, Device} = file:open(FileName, [read]),
    try get_all_lines(Device)
    after file:close(Device)
    end.

get_all_lines(Device) ->
    case io:get_line(Device, "") of
        eof  -> [];
        Line -> [string:trim(Line, trailing, "\n") | get_all_lines(Device)]
    end.
