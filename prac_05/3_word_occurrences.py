"""
Estimate: 20 minutes
Actual:   20 minutes
"""

word_to_count = {}
text = input("Text: ").lower()
words = text.split()
for word in words:
    occurrence = word_to_count.get(word, 0)
    word_to_count[word] = occurrence + 1

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
