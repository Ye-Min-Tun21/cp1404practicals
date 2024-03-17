counts = {}
text = input("Text: ")
words = text.split()

for word in words:
    counts[word] = counts.get(word, 0) + 1

words = list(counts.keys())
words.sort()

max_length = max((len(word) for word in words))

for word in words:
    print(f"{word:{max_length}} : {counts[word]}")
