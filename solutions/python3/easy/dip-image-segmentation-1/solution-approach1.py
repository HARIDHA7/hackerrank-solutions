# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/dip-image-segmentation-1/problem?isFullScreen=true
# Problem     Image Segmentation #1
# Difficulty  Easy
# Subdomain   Digital Image Analysis
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:30 a.m.
# Technique   breadth-first-search-connected-components
# Time        O(R * C)
# Space       O(R * C)
# Insight     The algorithm identifies connected components in a binary grid by performing a breadth-first search starting from each unvisited pixel labeled as one.
# Interview   Before: "How would you count distinct objects in a binary image?" After: "I use BFS to traverse each 4-connected component, marking visited pixels to ensure each object is counted exactly once. This approach runs in O(R * C) time and space, where R and C are the grid dimensions."
# Pitfalls    (1) Confusing 4-connectivity with 8-connectivity by including diagonal neighbors in the direction list.  (2) Failing to mark the starting pixel as visited before adding it to the queue, leading to infinite loops or redundant processing.  (3) Incorrectly handling grid boundaries when checking neighbors, which causes index out of bounds errors.
# ──────────────────────────────────────────────────

from collections import deque

grid = [
    "000110001010",
    "111011110001",
    "111010010010",
    "100000000100"
]

rows = len(grid)
cols = len(grid[0])

visited = [[False] * cols for _ in range(rows)]

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

count = 0

for r in range(rows):
    for c in range(cols):

        if grid[r][c] == '1' and not visited[r][c]:

            count += 1

            q = deque([(r, c)])
            visited[r][c] = True

            while q:
                x, y = q.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if (0 <= nx < rows and
                        0 <= ny < cols and
                        grid[nx][ny] == '1' and
                        not visited[nx][ny]):

                        visited[nx][ny] = True
                        q.append((nx, ny))

print(count)
