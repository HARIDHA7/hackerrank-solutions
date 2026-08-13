# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/predicting-office-space-price/problem?isFullScreen=true
# Problem     Polynomial Regression: Office Prices
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:03 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import itertools


def polynomial_features(x, degree=3):
    features = [1.0]

    n = len(x)

    for d in range(1, degree + 1):
        for comb in itertools.combinations_with_replacement(range(n), d):
            value = 1.0
            for i in comb:
                value *= x[i]
            features.append(value)

    return features


def gaussian_elimination(A, b):
    n = len(b)

    for i in range(n):
        # Find pivot
        pivot = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[pivot][i]):
                pivot = j

        A[i], A[pivot] = A[pivot], A[i]
        b[i], b[pivot] = b[pivot], b[i]

        # Eliminate
        for j in range(i + 1, n):
            if abs(A[i][i]) < 1e-12:
                continue

            factor = A[j][i] / A[i][i]

            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

            b[j] -= factor * b[i]

    # Back substitution
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        if abs(A[i][i]) < 1e-12:
            x[i] = 0.0
            continue

        value = b[i]

        for j in range(i + 1, n):
            value -= A[i][j] * x[j]

        x[i] = value / A[i][i]

    return x


def main():
    input = sys.stdin.readline

    F, N = map(int, input().split())

    X = []
    Y = []

    for _ in range(N):
        row = list(map(float, input().split()))
        X.append(row[:F])
        Y.append(row[F])

    # Create polynomial features up to degree 3
    PX = [polynomial_features(row, 3) for row in X]

    M = len(PX[0])

    # Normal equation:
    # (X^T X) beta = X^T y

    A = [[0.0] * M for _ in range(M)]
    B = [0.0] * M

    for i in range(N):
        for j in range(M):
            B[j] += PX[i][j] * Y[i]

            for k in range(M):
                A[j][k] += PX[i][j] * PX[i][k]

    # Small regularization to improve numerical stability
    for i in range(M):
        A[i][i] += 1e-8

    coefficients = gaussian_elimination(A, B)

    T = int(input())

    for _ in range(T):
        row = list(map(float, input().split()))

        features = polynomial_features(row, 3)

        prediction = 0.0
        for i in range(M):
            prediction += coefficients[i] * features[i]

        print(f"{prediction:.2f}")


if __name__ == "__main__":
    main()
