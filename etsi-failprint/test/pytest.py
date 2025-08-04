import subprocess
def test_cli_runs():
    result = subprocess.run([
        "failprint",
        "--input", "examples/X.csv",
        "--ytrue", "examples/y_true.csv",
        "--ypred", "examples/y_pred.csv",
        "--output", "markdown"
    ], capture_output=True)
    assert result.returncode == 0  # CLI ran successfully