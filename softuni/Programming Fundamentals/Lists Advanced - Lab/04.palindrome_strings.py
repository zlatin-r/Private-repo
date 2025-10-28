def is_palindrome(word):
    return word == word[::-1]


words = input().split()
key = input()

words = [w for w in words if is_palindrome(w)]
key_words = words.count(key)

print(words)
print(f"Found palindrome {key_words} times")
