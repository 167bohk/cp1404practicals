"""
Word Occurrences
Estimate: 20 minutes
Actual:   20 minutes
"""
from operator import itemgetter
input_text = input("Text: ")
word_to_count = {}
words = input_text.split(" ")
maximum_word_length = max(len(word) for word in words)
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
for word_key, count_value in sorted(word_to_count.items(), key=itemgetter(0)):
    print(f"{word_key:{maximum_word_length}} = {count_value}")
