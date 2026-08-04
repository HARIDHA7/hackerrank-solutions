# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem?isFullScreen=true
# Problem     Correlation and Regression Lines - A Quick Recap #1
# Difficulty  Medium
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-04, 10:50 a.m.
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
