# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/stat-warmup/problem?isFullScreen=true
# Problem     Basic Statistics Warmup
# Difficulty  Easy
# Subdomain   Statistics and Machine Learning
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:18 a.m.
# Technique   sorting-and-frequency-counting
# Time        O(N log N)
# Space       O(N)
# Insight     The implementation calculates descriptive statistics by sorting the array for median determination and using a hash map to identify the smallest mode among those with maximum frequency.
# Interview   Before: "How would you compute the mode and confidence interval for a large dataset?" After: "I would use a hash map for O(N) frequency counting and sort the array in O(N log N) to find the median, then apply the standard normal distribution formula for the 95% confidence interval."
# Pitfalls    (1) Failing to sort the array before calculating the median leads to incorrect middle-element selection.  (2) Selecting the wrong mode when multiple elements share the maximum frequency by not enforcing the numerically smallest requirement.  (3) Using the wrong standard deviation formula by failing to divide the sum of squared differences by N.
# ──────────────────────────────────────────────────

import math
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

# Mean
mean = sum(arr) / n

# Median
arr.sort()

if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

# Mode
freq = Counter(arr)
max_freq = max(freq.values())
mode = min(x for x in freq if freq[x] == max_freq)

# Standard deviation
variance = sum((x - mean) ** 2 for x in arr) / n
sd = math.sqrt(variance)

# 95% Confidence Interval
margin = 1.96 * sd / math.sqrt(n)
lower = mean - margin
upper = mean + margin

print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)
print(f"{sd:.1f}")
print(f"{lower:.1f} {upper:.1f}")
