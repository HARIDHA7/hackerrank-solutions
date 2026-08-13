# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-trigram/problem?isFullScreen=true
# Problem     The Trigram
# Difficulty  Easy
# Subdomain   Natural Language Processing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:26 a.m.
# ──────────────────────────────────────────────────

import sys

if __name__ == '__main__':
    text = sys.stdin.read()

    # Convert all whitespace to a single space
    text = ' '.join(text.split())

    # Split into sentences
    sentences = text.split('.')

    counts = {}
    first_order = []

    for sentence in sentences:
        words = sentence.strip().lower().split()

        # Create trigrams only inside the same sentence
        for i in range(len(words) - 2):
            trigram = ' '.join(words[i:i + 3])

            if trigram not in counts:
                counts[trigram] = 0
                first_order.append(trigram)

            counts[trigram] += 1

    # Find most frequent trigram.
    # Since first_order is in occurrence order,
    # keep the first one when frequencies are equal.
    answer = first_order[0]

    for trigram in first_order:
        if counts[trigram] > counts[answer]:
            answer = trigram

    print(answer)
