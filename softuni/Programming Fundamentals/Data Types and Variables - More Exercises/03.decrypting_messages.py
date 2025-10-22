key = int(input())
n = int(input())

message = ""

for i in range(n):
    letter = input()

    letter_code = ord(letter)
    letter_code += key

    new_letter = chr(letter_code)
    message += new_letter

print(message)
