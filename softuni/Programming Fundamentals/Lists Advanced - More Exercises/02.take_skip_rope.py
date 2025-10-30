message = input()

result = []
index = 0

letters_list = [ch for ch in message if not ch.isdigit()]
num_lst = [int(ch) for ch in message if ch.isdigit()]

take_lst = num_lst[::2]
skip_lst = num_lst[1::2]

for take, skip in zip(take_lst, skip_lst):
    result.extend(letters_list[index:index + take])

    index += take + skip

print("".join(result))
