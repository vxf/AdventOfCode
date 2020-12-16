#![feature(test)]

extern crate test;

use std::collections::HashMap;

fn solve(d: &mut HashMap<i32, i32>, mut n: i32, start: i32, end: i32) -> i32 {
    for i in start as i32..(end-1) {
        let a = match d.get(&n) {
            None => 0,
            Some(x) => i - x,
        };
        d.insert(n, i);
        n = a;
    }
    return n;
}

fn main() {
    let l = vec![1,12,0,20,8,16];
    // let l = vec![0,3,6];
    let mut d: HashMap<i32, i32> = l[0..l.len()-1]
        .iter()
        .enumerate()
        .map(|(t,u)| (*u, t as i32))
        .collect();

    let mut n = *l.last().unwrap();

    n = solve(&mut d, n, l.len() as i32 -1, 2020);
    println!("{}", n);

    n = solve(&mut d, n, 2020, 30000000);
    println!("{}", n);

}

#[bench]
fn bench_day01(b: &mut test::Bencher) {
    b.iter(|| main());
}