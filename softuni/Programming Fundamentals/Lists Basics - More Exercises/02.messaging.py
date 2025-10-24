numbers = list(map(int, input().split()))
text = list(input())  # convert to list to easily remove chars
message = []

for number in numbers:
    index = sum(int(digit) for digit in str(number))
    index = index % len(text)  # wrap around if index >= length
    message.append(text.pop(index))  # add char and remove from text

print("".join(message))
