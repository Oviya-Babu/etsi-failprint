import argparse
from etsi.failprint.core import analyze
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Run failprint analysis from CLI")
    parser.add_argument('--input', required=True, help='Path to input features CSV file')
    parser.add_argument('--ytrue', required=True, help='Path to ground truth labels CSV')
    parser.add_argument('--ypred', required=True, help='Path to predicted labels CSV')
    parser.add_argument('--output', default='markdown', help='Output format (markdown/html/json)')

    args = parser.parse_args()

    X = pd.read_csv(args.input)
    y_true = pd.read_csv(args.ytrue).squeeze()
    y_pred = pd.read_csv(args.ypred).squeeze()

    report = analyze(X, y_true, y_pred, output=args.output)
    print(report)

if __name__ == "__main__":
    main()
