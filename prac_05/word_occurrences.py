"""
Yunsun Park
CP1404 Practical
Word Occurrences

Estimate: 40 minutes
Actual:  40 minutes
"""

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count("Hi, my name is Yunsun."))