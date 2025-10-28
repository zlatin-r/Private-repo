message = input().split()

decoded_words = []

for word in message:
    digits = "".join(filter(str.isdigit, word))
    first_char = chr(int(digits))
    
    rest = word[len(digits):]
    
    if len(rest) > 1:
        rest = rest[-1] + rest[1:-1] + rest[0]
    
    decoded_words.append(first_char + rest)

decoded_message = " ".join(decoded_words)
print(decoded_message)
