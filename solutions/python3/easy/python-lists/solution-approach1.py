# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:09 a.m.
# Technique   command-pattern-dispatch
# Time        O(N * M) where N is the number of comma…
# Space       O(M) where M is the maximum number of e…
# Insight     The implementation uses a conditional dispatch pattern to map string-based command inputs directly to corresponding Python list methods.
# Interview   Before: "How would you handle a sequence of dynamic list operations?" After: "I would use a command-pattern dispatch to map input strings to list methods, noting that operations like sort take O(M log M) and insert/remove take O(M) time, where M is the current list size."
# Pitfalls    (1) The remove method raises a ValueError if the specified integer is not present in the list.  (2) The pop method raises an IndexError if called on an empty list.  (3) The insert method does not raise an error for out-of-bounds indices but instead appends or prepends the element.
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
