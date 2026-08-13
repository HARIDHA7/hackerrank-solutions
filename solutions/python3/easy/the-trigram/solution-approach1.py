# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-trigram/problem?isFullScreen=true
# Problem     The Trigram
# Difficulty  Easy
# Subdomain   Natural Language Processing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-13, 10:26 a.m.
# Technique   sentence-split-sliding-window-hash-map
# Time        O(N)
# Space       O(N)
# Insight     The algorithm splits the input into sentences, tokenizes each into words, and tracks the first occurrence of each trigram using a dictionary to maintain insertion order.
# Interview   Before: "How do I handle trigrams spanning across sentence boundaries?" After: "The problem requires trigrams to exist within a single sentence, so we split by '.' first. Using a dictionary to store counts ensures O(N) time complexity while preserving the first-occurrence order for ties."
# Pitfalls    (1) Failing to remove the trailing dot from the last word of a sentence before trigram extraction.  (2) Including words from different sentences in a single trigram, violating the sentence-boundary constraint.  (3) Incorrectly handling case sensitivity by failing to normalize all words to lowercase before counting.
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
