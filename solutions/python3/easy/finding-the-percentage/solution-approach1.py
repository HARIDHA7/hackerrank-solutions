# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
# Problem     Finding the percentage
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:08 a.m.
# Technique   hash-map-average-calculation
# Time        O(N * M)
# Space       O(N * M)
# Insight     The solution maps student names to lists of floating-point marks and computes the arithmetic mean by dividing the sum of the list by its length.
# Interview   Before: "I would iterate through the list and calculate the average manually." After: "Using a dictionary provides O(1) lookup for the student, and calculating the average takes O(M) time where M is the number of marks, resulting in O(N * M) total time complexity for N students."
# Pitfalls    (1) Failing to format the output to exactly two decimal places using f-string formatting.  (2) Assuming the input marks are integers when the problem requires floating-point precision.  (3) Attempting to access a query_name that does not exist in the dictionary.
# ──────────────────────────────────────────────────

n = int(input())

students = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    students[name] = marks

query_name = input()

average = sum(students[query_name]) / len(students[query_name])

print(f"{average:.2f}")
