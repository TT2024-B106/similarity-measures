use std::env;
use std::f64;
use std::fs::File;
use std::time::{Instant, Duration};
use std::io::Write;

fn distance(p: Vec<f64>, q: Vec<f64>) -> Result<f64, String> {
    if p.len() != q.len() {
        return Err(String::from("Vectors must have the same length"));
    }

    let squares_sum = p.iter()
        .zip(q.iter())
        .map(|(a, b)| (a - b).powi(2))
        .sum::<f64>();

    Ok(squares_sum.sqrt())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut n = 60;
    let args: Vec<String> = env::args().collect();

    if args.len() > 1 {
        let num_result = args[1].parse::<usize>();

        match num_result {
            Ok(num) => {
                n = num;
            }
            Err(_) => {
                println!("No valid number provided in args. Using default: 60.");
            }
        }
    }

    let mut durations: Vec<Duration> = Vec::new();

    for i in 1..=n {
        let p = vec![1.0; i];
        let q = vec![0.5; i];

        let start = Instant::now();
        match distance(p, q) {
            Ok(_) => { }, // Do nothing on success
            Err(e) => println!("Error: {}", e),
        }
        durations.push(start.elapsed());
    }

    let mut file = File::create("durations.txt")?;
    writeln!(file, "{:?}", durations)?;

    println!("Durations saved under durations.txt");

    Ok(())
}
