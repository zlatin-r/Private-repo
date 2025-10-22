n = int(input())
special_numbers = [5, 7, 11]

for i in range(1, n + 1):
    lst_digits = list(str(i))
    sum_numbers = sum(map(int, lst_digits))

    if sum_numbers in special_numbers:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
