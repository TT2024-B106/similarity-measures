use pyo3::prelude::*;
use std::f64;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn distance(p: Vec<f64>, q: Vec<f64>) -> PyResult<f64> {
    if p.len() != q.len() {
        return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
            "Error: Arrays must always have the same size."
        ));
    }

    let squares_sum = p.iter()
        .zip(q.iter())
        .map(|(a, b)| (a - b).powi(2))
        .sum::<f64>();

    Ok(squares_sum.sqrt())
}

/// A Python module implemented in Rust.
#[pymodule]
fn stmeasures(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(distance, m)?)?;

    Ok(())
}
