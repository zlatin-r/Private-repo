n = int(input())
words = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word not in words:
        words[word] = []
    words[word].append(synonym)

for w, d in words.items():
    print(f"{w} - {', '.join(d)}")
