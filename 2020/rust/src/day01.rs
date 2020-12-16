#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn solve1(v: &Vec<i32>) -> Result<i32, &'static str> {
    let mut l: Vec<i32> = Vec::new();
    for x in v {
        for y in &l {
            if x + y == 2020 {
                return Ok(x*y);
            }
        }
        l.push(*x);
    }
    Err("Not found")
}

fn solve2(v: &Vec<i32>) -> Result<i32, &'static str> {
    let mut l: Vec<i32> = Vec::new();
    for x in v {
        let mut m: Vec<i32> = Vec::new();
        for y in &l {
            for z in &m {
                if x + y + z == 2020 {
                    return Ok(x*y*z);
                }
            }
            m.push(*y);
        }
        l.push(*x);
    }
    Err("Not found")
}

fn main() {
    if let Ok(lines) = read_lines("../1/input.txt")
    {
        let v: Vec<i32> = lines
            .map(|x| x.unwrap().parse::<i32>().unwrap())
            .collect();

        if let Ok(r) = solve1(&v)
        {
            println!("{}", r);
        }

        if let Ok(r) = solve2(&v)
        {
            println!("{}", r);
        }
    }
}

// https://doc.rust-lang.org/rust-by-example/std_misc/file/read_lines.html
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

#[bench]
fn bench_day01(b: &mut test::Bencher) {
    b.iter(|| main());
}