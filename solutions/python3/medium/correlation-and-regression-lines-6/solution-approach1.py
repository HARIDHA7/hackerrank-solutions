# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem?isFullScreen=true
# Problem     Correlation and Regression Lines - A Quick Recap #1
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-04, 10:50 a.m.
# Technique   pearson-correlation-coefficient-calculation
# Time        O(n)
# Space       O(n)
# Insight     The implementation calculates the Pearson correlation coefficient by computing the covariance of the two datasets divided by the product of their standard deviations.
# Interview   Before: "How would you calculate the linear relationship between two datasets?" After: "I compute the Pearson correlation coefficient in O(n) time by calculating the means and then the sum of products of deviations, ensuring the result is rounded to three decimal places as required."
# Pitfalls    (1) Failure to use floating-point division when calculating means can lead to precision loss in languages with integer division.  (2) Rounding the result prematurely before the final output can violate the requirement to round to three decimal places.  (3) Assuming the input lists are of equal length without validation could cause zip to truncate data silently.
# ──────────────────────────────────────────────────

from math import sqrt

physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

n = len(physics)

mean_x = sum(physics) / n
mean_y = sum(history) / n

num = sum((x - mean_x) * (y - mean_y) for x, y in zip(physics, history))
den = sqrt(sum((x - mean_x) ** 2 for x in physics) *
           sum((y - mean_y) ** 2 for y in history))

r = num / den

print(f"{r:.3f}")
