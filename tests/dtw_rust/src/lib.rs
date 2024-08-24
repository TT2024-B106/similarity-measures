use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn dtw(sequence1: Vec<(f64, f64)>, sequence2: Vec<(f64, f64)>) -> f64 {
    let n = sequence1.len();
    let m = sequence2.len();

    let mut dtw_matrix: Vec<Vec<f64>> = vec![vec![f64::INFINITY; m + 1]; n + 1];
    dtw_matrix[0][0] = 0.0;

    for i in 1..=n {
        for j in 1..=m {
            let cost = ((sequence1[i - 1].0 - sequence2[j - 1].0).powi(2)
                + (sequence1[i - 1].1 - sequence2[j - 1].1).powi(2))
            .sqrt();
            dtw_matrix[i][j] = cost
                + dtw_matrix[i - 1][j]
                .min(dtw_matrix[i][j - 1])
                .min(dtw_matrix[i - 1][j - 1]);
        }
    }

    dtw_matrix[n][m]
}

#[pymodule]
fn dtw_rust(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(dtw, m)?)?;
    Ok(())
}

