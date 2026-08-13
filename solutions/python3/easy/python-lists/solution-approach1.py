# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:09 a.m.
# ──────────────────────────────────────────────────

n = int(input())

my_list = []

for _ in range(n):
    command = input().split()

    if command[0] == "insert":
        my_list.insert(int(command[1]), int(command[2]))

    elif command[0] == "print":
        print(my_list)

    elif command[0] == "remove":
        my_list.remove(int(command[1]))

    elif command[0] == "append":
        my_list.append(int(command[1]))

    elif command[0] == "sort":
        my_list.sort()

    elif command[0] == "pop":
        my_list.pop()

    elif command[0] == "reverse":
        my_list.reverse()
