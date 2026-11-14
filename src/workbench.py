"""Deterministic CSC-40072 reproductions using the Python standard library.

This 2026 portfolio implementation is separate from the original assignment.
The linear-system and gradient-descent inputs reproduce non-personalised worked
examples in that assignment. The Bayes example is an explicitly synthetic study
example. These small routines are for learning, not a general numerical library.
"""
from __future__ import annotations

import json
import math
from numbers import Real
from typing import Sequence


def _finite(value: Real, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a finite real number")
    try:
        result = float(value)
    except (OverflowError, ValueError) as error:
        raise ValueError(f"{name} must be a finite real number") from error
    if not math.isfinite(result):
        raise ValueError(f"{name} must be a finite real number")
    return result


def solve_linear_system(
    matrix: Sequence[Sequence[Real]],
    rhs: Sequence[Real],
    *,
    relative_tolerance: Real = 1e-12,
) -> list[float]:
    """Solve A x = b by Gaussian elimination with partial pivoting.

    Input arrays are copied. A pivot no larger than relative_tolerance times the
    largest input coefficient is treated as numerically singular. This simple
    threshold does not estimate condition number; prefer a numerical library for
    large, sparse or ill-conditioned problems.
    """
    tolerance = _finite(relative_tolerance, "relative_tolerance")
    if not 0 < tolerance < 1:
        raise ValueError("relative_tolerance must be between zero and one")
    try:
        rows = [list(row) for row in matrix]
        values = list(rhs)
    except TypeError as error:
        raise ValueError("matrix and rhs must be sequences") from error
    count = len(rows)
    if not count or len(values) != count or any(len(row) != count for row in rows):
        raise ValueError("matrix must be nonempty and square, with a matching rhs")
    a = [[_finite(value, "coefficient") for value in row] for row in rows]
    b = [_finite(value, "rhs") for value in values]
    scale = max(abs(value) for row in a for value in row)
    if scale == 0:
        raise ValueError("matrix is singular or numerically singular")
    for column in range(count):
        pivot = max(range(column, count), key=lambda row: abs(a[row][column]))
        if abs(a[pivot][column]) / scale <= tolerance:
            raise ValueError("matrix is singular or numerically singular")
        a[column], a[pivot] = a[pivot], a[column]
        b[column], b[pivot] = b[pivot], b[column]
        for row in range(column + 1, count):
            factor = a[row][column] / a[column][column]
            a[row][column] = 0.0
            for j in range(column + 1, count):
                a[row][j] = _finite(a[row][j] - factor * a[column][j], "elimination result")
            b[row] = _finite(b[row] - factor * b[column], "elimination rhs")
    solution = [0.0] * count
    for row in range(count - 1, -1, -1):
        numerator = b[row] - math.fsum(a[row][j] * solution[j] for j in range(row + 1, count))
        solution[row] = _finite(numerator / a[row][row], "solution")
    return solution


def gradient_descent(
    start: Real = 5.0, learning_rate: Real = 0.1, iterations: int = 3
) -> list[dict[str, float | int]]:
    """Return initial state plus updates for f(x) = x² + 4x + 6.

    The derivative is 2x+4. Rates strictly between 0 and 1 give convergence for
    this particular quadratic in exact arithmetic. At most 10,000 updates are
    accepted; zero updates returns only the initial state.
    """
    x = _finite(start, "start")
    rate = _finite(learning_rate, "learning_rate")
    if not 0 < rate < 1:
        raise ValueError("learning_rate must be strictly between zero and one")
    if isinstance(iterations, bool) or not isinstance(iterations, int) or not 0 <= iterations <= 10_000:
        raise ValueError("iterations must be an integer between zero and 10000")
    trace = []
    for step in range(iterations + 1):
        shifted = _finite(x + 2, "shifted x")
        objective = _finite(shifted * shifted + 2, "objective")
        gradient = _finite(2 * shifted, "gradient")
        trace.append({"step": step, "x": x, "objective": objective, "gradient": gradient})
        if step != iterations:
            x = _finite(x - rate * gradient, "updated x")
    return trace


def bayes_posterior(prior: Real, likelihood: Real, false_positive_rate: Real) -> float:
    """Compute P(H | E) from P(H), P(E | H), and P(E | not H).

    Zero-probability evidence has no defined posterior and raises ValueError.
    The complement hypothesis is assumed to exhaust the remaining probability.
    """
    p = _finite(prior, "prior")
    sensitivity = _finite(likelihood, "likelihood")
    false_positive = _finite(false_positive_rate, "false_positive_rate")
    if any(not 0 <= value <= 1 for value in (p, sensitivity, false_positive)):
        raise ValueError("probabilities must be between zero and one inclusive")
    numerator = p * sensitivity
    evidence = numerator + (1 - p) * false_positive
    if evidence == 0:
        raise ValueError("posterior is undefined for zero-probability evidence")
    return numerator / evidence


def demonstration() -> dict:
    matrix = [[8, 7, 3], [-7, -4, -4], [-6, 5, -4]]
    rhs = [18, -11, -15]
    solution = solve_linear_system(matrix, rhs)
    return {
        "edition": "2026 portfolio reproduction; separate from assessed coursework",
        "linear_algebra": {
            "source": "Assignment Part 1(A), non-personalised linear system",
            "matrix": matrix,
            "rhs": rhs,
            "solution": solution,
            "max_absolute_residual": max(abs(math.fsum(a * x for a, x in zip(row, solution)) - value) for row, value in zip(matrix, rhs)),
        },
        "optimisation": {
            "source": "Assignment worked quadratic example",
            "function": "f(x) = x^2 + 4x + 6",
            "analytic_minimum": {"x": -2, "objective": 2},
            "learning_rate": 0.1,
            "trace": gradient_descent(),
        },
        "probability": {
            "source": "Synthetic study example created in 2026; not an assignment result",
            "prior": 0.1,
            "likelihood": 0.8,
            "false_positive_rate": 0.2,
            "posterior": bayes_posterior(0.1, 0.8, 0.2),
        },
    }


if __name__ == "__main__":
    print(json.dumps(demonstration(), indent=2, allow_nan=False))
