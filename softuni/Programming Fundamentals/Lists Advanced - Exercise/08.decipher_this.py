message = input().split()

decoded = [chr(int("".join(filter(str.isdigit, x)))) for x in message]

decoded_message = "".join(decoded)

print(decoded_message)
