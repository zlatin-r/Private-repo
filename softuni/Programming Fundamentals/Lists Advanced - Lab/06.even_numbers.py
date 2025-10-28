numbers = list(map(int, input().split(", ")))
found_idxs_or_no = map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers)))
even_idxs = list(filter(lambda a: a != "no", found_idxs_or_no))

print(even_idxs)
